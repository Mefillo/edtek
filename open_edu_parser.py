# -*- coding: utf-8 -*-

import os, django
from pathlib import Path
from django.conf import settings
import re
import requests as req
from requests import api
from datetime import datetime
import pandas as pd
import codecs
import numpy as np
import json

from django.core import serializers
from django.db.utils import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()

from api.models import Course

from modules import printProgressBar, db_saver
#Test
import pdb

IMG_LINK = 'http://edtek.ru/upload/medialibrary/a8a/Surface%20Pro%203.png'

def clear_csv(csv_name):
    '''Make encoding from utf-8 to windows-1251 possible'''
    s = open(csv_name).read()
    s = s.replace('σ', 'сигма')
    s = s.replace('π', 'пи')
    s = s.replace('ā', 'a')
    s = s.replace('á', 'a')
    s = s.replace('š', 's')
    s = s.replace('ž', 'z')
    s = s.replace('ġ', 'g')
    s = s.replace('č', 'c')
    s = s.replace('●', '-')
    s = s.replace('≤', '=<')
    s = s.replace('̆', 'й')
    s = s.replace(u'\u200b', "    ")
    s = s.replace(u'\u2192', "->")
    s = s.replace(u'\u2642', "")
    s = s.replace(u'\u2640', "")
    s = s.replace(u'\u2212', "-")
    s = s.replace(u'\u0301', "'")
    s = s.replace(u'\u202f', "   ")
    s = s.replace(u'\u25a0', "-")
    
        


    f = open(csv_name, 'w')
    f.write(s)
    f.close()
   

def course_encode(text):
    '''Makes data from API JSON readable'''

    text = text.replace(': None,', ": 'None',")
    text = text.replace(': None}', ": 'None'}")
    text = text.replace(': False,',": 'False',")
    text = text.replace(': True,',": 'True',")
    text = text.replace('\"','$9872')
    text = text.replace('\'', '"')
    text = text.replace('$9872','\'')
    text = text.replace('''\\xa0''','')

    return text


def parser(file_name):
    '''Parse website OpenEdu'''

    #getting first page
    r = api.get('https://courses.openedu.ru/api/courses/v1/courses/?page=1')
    data = course_encode(str(r.json()))
    with open (file_name, 'w+') as f:
        f.write(data)
    pages = int(r.json()['pagination']['num_pages'])

    #Initiate progress bar
    printProgressBar(
        0,
        pages,
        prefix = 'Progress of parsing: ',
        suffix = 'Complete {} of {}'.format(0, pages),
        length = 30
        )

    #getting all other pages
    for i in range (2, pages+1):

        printProgressBar(
            i,
            pages,
            prefix = 'Progress of parsing: ',
            suffix = 'Complete {} of {}'.format(i, pages),
            length = 30
            )

        r = api.get('https://courses.openedu.ru/api/courses/v1/courses/?page='+str(i))
        dict_of_data = r.json()
        text_to_write = list(str(dict_of_data['results']))
        text_to_write[0] = ','
        text_to_write.append('}')
        text_to_write = course_encode(''.join(text_to_write))
        text_to_write = str.encode(''.join(text_to_write))

        with open (file_name, 'rb+') as f:
            f.seek(-2,2)
            f.write(text_to_write)

    return dict_of_data



if __name__ == "__main__":

    Path('cache/').mkdir(exist_ok=True)
    Path('csv/').mkdir(exist_ok=True)
    file_name = 'cache/cache_'+str(datetime.today())[:10]
    csv_name = 'csv/'+str(datetime.today())[:10]+'.csv'

    #Parse list of courses
    parser(file_name = file_name)

    #get json data from file
    '''with open(file_name, 'r') as f:
        dict_of_data = json.loads(f.read())'''

    #Save to db
    db_saver(dict_of_data)
    #csv_name = csv_name[:-4]+'test.csv'
    #Save to csv
    c = Course.objects.all().values()
    cour = pd.DataFrame.from_records(c)
    cour.to_csv(csv_name)

    #Clearing from all bad characters
    clear_csv(csv_name)


    
    #Save to windows1251 csv
    cours = pd.read_csv(csv_name)
    print(csv_name)
    #Replace blank images with logo
    print(cours['detail_image'].isnull().value_counts())
    cours['detail_image'] = cours['detail_image'].replace(np.nan, IMG_LINK, regex=True)
    cours['anons_image'] = cours['anons_image'].replace(np.nan, IMG_LINK, regex=True)
    print(cours['detail_image'].isnull().value_counts())
    cours.to_csv(csv_name, encoding='cp1251')
    
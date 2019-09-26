from datetime import datetime
import json
import requests
from json.decoder import JSONDecodeError
from api.models import Course
from django.db.utils import IntegrityError


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()
        print()


def get_modules_type():
    return 'null'

def get_modules_number():
    return 'null'

def get_avg_length():
    return 'null'

def get_length():
    return 'null'

def get_code(num):
    return num

def get_deadlines(start, end):
    start_valid = start != 'Нет'
    end_valid = end != 'Нет'
    if start_valid and end_valid:
        return "Да"
    else:
        return "Нет"

def get_post_entrance(deadlines):
    if deadlines == 'Да':
        return 'Нет'
    else:
        return 'Да'

def get_sync():
    return 'Асинхронные'

def get_payment():
    return 'Нет'

def get_start_date(start, i = 'check'):
    '''Check if date is valid and if it is not - set to null'''
    try:
        datetime.strptime(start, '%Y-%m-%d')
    except ValueError:
        print("Incorrect start data format, should be YYYY-MM-DD-HH-MM-SS for {} - {}. Reset to null".format(i, start))
        start = 'Нет'
    except TypeError:
        print("Incorrect start data format, should be YYYY-MM-DD-HH-MM-SS for {} - {}. Reset to null".format(i, start))
        start = 'Нет'
    return start

def get_end_date(end, i = 'check'):
    try:
        datetime.strptime(end, '%Y-%m-%d')
    except ValueError:
        print("Incorrect end data format, should be YYYY-MM-DD-HH-MM-SS for {} - {}. Reset to null".format(i, end))
        end = 'Нет'
    except TypeError:
        print("Incorrect end data format, should be YYYY-MM-DD-HH-MM-SS for {} - {}. Reset to null".format(i, end))
        end = 'Нет'

    return end


def db_saver(dict_of_data):
    """
    Save data to db from dict
    @params:
    dict_of_data    - Required   : dictionary with data (dict)
    """
    #Number of courses counter
    j = 0
    #Number of courses overall
    courses = int(dict_of_data["pagination"]["count"])
    #Ununique courses provided
    unique_count = 0
    #Initiate progress bar
    printProgressBar(
        j,
        courses,
        prefix = 'Saving to db: ',
        suffix = 'Saved {} of {}'.format(j, courses),
        length = 30
        )
    
    #Saving to db
    for i in dict_of_data['results']:

        '''
        if j == 494:
            print(('https://openedu.ru/api/courses/export/{}/{}?format=json'.format(i['org'],i['number'])))
        j+=1
        '''
        
        jlink = 'https://openedu.ru/api/courses/export/{}/{}?format=json'.format(i['org'],i['number'])
        r = requests.api.get(jlink)
        try:
            data = json.loads(json.dumps(r.json()))
        except JSONDecodeError:
            print(' Такого нет =( {}'.format(jlink))
            j+=1
            continue
        try:
            data['detail']
        except:
            start_date = get_start_date(data['started_at'], j)
            end_date = get_end_date(data['finished_at'], j)
            deadlines = get_deadlines(start_date, end_date)
            post_entrance = get_post_entrance(deadlines)
            
            if data['cert']:
                certification = 'Да'
            else:
                certification = 'Нет'

            if data['requirements'] == '':
                prerequesetes = 'Нет'
            else:
                prerequesetes = data['requirements']
            
            authors = ''
            for author in data['teachers']:
                authors = authors + author['display_name'] + ', '
            authors = authors[:-2]

            if data['hours_per_week']:
                avg_length = str(int(float(data['hours_per_week'])))+' часов в неделю'
            else:
                avg_length = 'Неизвестно'

            cour = Course(
                distributor = 'openedu',
                name = data['title'],
                description = data['description'],
                long_description = data['content'],
                organization = i['org'],
                org_link = data['external_url'],
                start_date = data['started_at'],
                end_date = data['finished_at'],
                course_id = i['id'],
                mnemocode = i['id'],
                detail_image = data['image'],
                anons_image = data['image'],
                video = data['promo_url'],
                modules_type = 'Лекция',
                modules_number = data['lectures'],
                avg_length = avg_length,
                length = str(data['duration']['value'])+ ' ' + data['duration']['code'],
                code = get_code(j),
                deadlines = deadlines,
                post_entrance = post_entrance,
                sync = get_sync(),
                payment = get_payment(),
                prerequesetes = prerequesetes,
                skills = data['results'],
                language = data['language'],
                authors = authors,
                certification = certification,
                )
            try:
                cour.save()

                printProgressBar(
                    j,
                    courses,
                    prefix = 'Progress of parsing: ',
                    suffix = 'Complete {} of {}'.format(j, courses),
                    length = 30
                    )


            except IntegrityError:
                unique_count += 1

                printProgressBar(
                    j,
                    courses,
                    prefix = 'Progress of parsing: ',
                    suffix = 'Complete {} of {}'.format(j, courses),
                    length = 30
                    )
        j+=1    

    print ('Didn`t save {} courses out of {} because they already existed'.format(unique_count, courses))


from django.shortcuts import render, HttpResponse
from api.models import Course

def api (request, num):
    c = Course.objects.all()
    return HttpResponse(content=c)
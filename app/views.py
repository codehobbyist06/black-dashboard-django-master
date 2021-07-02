# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import Data
from datetime import datetime

default_temp_list = [99,98,97,98,98,98,99,100,104,100,99,100]
default_hr_list = [60,80,70,90,100,60]
default_oxy_list = [95,96,95,96,97]

# default_temp_labels = []
# default_hr_labels = []
# default_oxy_labels = []

def get_data(request):
    data = json.loads(request.body)
    temp_data = data['temp_data']
    hr_data = data['hr_data']
    oxy_data = data['oxy_data']

    mydata = Data()
    mydata.myList_temp = temp_data
    mydata.myList_heartrate = hr_data
    mydata.myList_oxygen = oxy_data
    mydata.save()
    return HttpResponse("<h1>Thank you</h1>")

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'
    data = []
    if Data.objects.all().latest('id'):
        data = Data.objects.all().latest('id')

    if data.myList_temp:
        context['temp_data'] = data.myList_temp
        context['hr_data'] = data.myList_heartrate
        context['oxy_data'] = data.myList_oxygen
    else:
        context['temp_data'] = default_temp_list
        context['hr_data'] = default_hr_list
        context['oxy_data'] = default_oxy_list

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

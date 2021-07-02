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

data_list = [99,98,97,98,98,98,99,100,104,100,99,100]

# @login_required(login_url="/login/")
def get_data(request):
    data = json.loads(request.body)
    mylist = data['data']
    
    mydata = Data()
    mydata.myList = mylist
    mydata.save()
    return HttpResponse("<h1>Thank you</h1>")

# @login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'
    data = []
    mydata = Data()
    mydata.myList = data_list
    mydata.save()
    if Data.objects.all().latest('id'):
        data = Data.objects.all().latest('id')
        print(data.myList)

    if data.myList:
        context['data_list'] = data.myList
    else:
        context['data_list'] = data_list

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

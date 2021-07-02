# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

from app.models import Data

mydata = Data()
mydata.myList = [99,98,97,98,98,98,99,100,104,100,99,100]
mydata.save()
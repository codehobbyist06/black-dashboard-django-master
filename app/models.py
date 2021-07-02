# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Data(models.Model):
	myList_temp = models.TextField(null=True)
	myList_heartrate = models.TextField(null=True)
	myList_oxygen = models.TextField(null=True)
	# myLabels_temp = models.TextField(null=True)
	# myLabels_heartrate = models.TextField(null=True)
	# myLabels_oxygen = models.TextField(null=True)


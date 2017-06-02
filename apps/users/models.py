# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# from ..catering.models import Order, Product, Category
import re

#REGEX
NAME_REGEX = re.compile(r'^^[a-zA-Z-]{2,}$') # any letter and -, min 2.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # must be in format name@example.com
PHONE_REGEX = re.compile(r'^[(]+\d{3}[)]+\d{3}[-]+\d{4}$') # must be in format (###)###-####
PW_REGEX = re.compile(r'^(?=.+?[A-Z])(?=.+?[a-z])(?=.+?[0-9])(?=.+?[!@#$%^&*()]).{8,20}$') # 8-20 characters, 1 cap, 1 lower, 1 number, 1 symbol.

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=14)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_lvl = models.IntegerField(default=0)

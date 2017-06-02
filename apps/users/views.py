# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
# from .model import User
# from ..catering.models import Order, Product, Category

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def login(request):
    pass

def register(request):
    pass

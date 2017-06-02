# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from .models import Order, Product, Category
# from ..users.models import User
# Create your views here.

def index(request):
    return render(request, 'catering:dashboard.html')

def product_showcase(request):
    pass

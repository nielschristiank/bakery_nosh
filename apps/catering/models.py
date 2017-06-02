# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# from ..users.models import User


# class Cart(models.Model):
#     user_cart = models.OneToOneField('User')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    # order_cart = models.('Cart')
    order_user = models.ForeignKey('users.User', related_name='orders')
    made_order = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    # quantity = models.IntegerField()
    order = models.ManyToManyField(Order, related_name='product')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    product = models.ManyToManyField(Product, related_name='category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

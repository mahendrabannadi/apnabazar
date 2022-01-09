from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Category, Customer, Order, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','slug']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    class Meta:
        model = Product
        fields = ['id','category','name','description','slug','price','image','in_stock','is_active','created','updated']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','firstname','lastname','phone','email','password']

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only = True)
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ['id','product','customer','quantity','price','address','phone','date','status']
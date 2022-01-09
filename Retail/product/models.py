from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 222)
    slug = models.SlugField(max_length=222, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'product', on_delete=models.CASCADE)
    name = models.CharField(max_length=222)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=222)
    #price = models.DecimalField(max_digits=7, decimal_places=5)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'uploads/product/')
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    # @staticmethod
    # def get_all_products():
    #     return Product.objects.all

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

class Customer(models.Model):
    firstname = models.CharField(max_length=222)
    lastname = models.CharField(max_length=222)
    phone = models.CharField(max_length=22)
    email = models.EmailField()
    password = models.CharField(max_length=222)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=222, default='', blank=True)
    phone = models.CharField(max_length=18,default='', blank=True)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects\
        .filter(customer = customer_id)\
        .order_by('-date')

 

        
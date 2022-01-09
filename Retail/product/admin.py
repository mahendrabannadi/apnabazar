from django.contrib import admin

# Register your models here.
from .models import Category, Customer, Order,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','category','name','description','slug','price','image','in_stock','is_active','created','updated']
    list_filter = ['in_stock','is_active']
    list_editable = ['price','in_stock']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Customer)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','phone','email','password']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =  ['id','product','customer','quantity','price','address','phone','date','status']

#admin.site.register(Order)






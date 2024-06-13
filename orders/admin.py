from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(ProductInBasket)
class AdminUserBasket(admin.ModelAdmin):
    list_display = ['user_basket','product','quantity','total_price']
    list_display_links = ['user_basket','product','quantity','total_price']


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['product','name','phone','email','adres']
    list_display_links = ['product','name','phone','email','adres']



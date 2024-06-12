from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Сategories)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price","quantity","сategories","is_active"]


    class Meta:
        model = Product
    
admin.site.register(Product, ProductAdmin)


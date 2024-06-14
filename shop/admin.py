from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register(Сategories)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price","quantity","сategories","is_active"]

    class Meta:
        model = Product
    



# @admin.register(Categories)
# class CategoriesAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}            # Автоматическое заполнение слага URL в админке.
#     list_display = ["name",]

# @admin.register(Products)
# class ProductsAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}             # Автоматическое заполнение слага URL в админке.
#     list_display = ["name", "quantity", "price", "discount"]
#     list_editable = ["discount",]
#     search_fields = ["name", "description"]
#     list_filter = ["discount", "quantity", "category"]
#     fields = [
#         "name",
#         "category",
#         "slug",
#         "description",
#         "image",
#         ("price", "discount"),
#         "quantity",
#     ]

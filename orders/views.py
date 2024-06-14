from django.shortcuts import render

from .models import *
from shop.models import *
from users.models import *
from .forms import FormOrder

from decimal import Decimal             # ____________
from django.conf import settings
from shop.models import Product         # ____________


#  # ____________

# from django.http import JsonResponse
# from django.shortcuts import redirect, render
# from django.template.loader import render_to_string
# from .models import Cart
# from .utils import get_user_carts
# from shop.models import Products


# # Корзина
# def basket(request):
#     user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)   # *
#     lst_product = ProductInBasket.objects.filter(user_basket=user)
    
#     total_price=0
#     for price in lst_product:
#         total_price+=price.total_price
#     if request.method == 'POST': 
#         product=request.POST.get("product")
#         id_product = Product.objects.get(id=product)
#         get_product = ProductInBasket.objects.filter(product = id_product)
#         get_product.delete()
#     return render(request, "basket.html", {"products":lst_product,'price':total_price})


# Корзина
def basket(request):
    user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)   # *
    lst_product = ProductInBasket.objects.filter(user_basket=user)
    
    total_price=0
    for price in lst_product:
        total_price+=price.total_price
    if request.method == 'POST': 
        id_product=request.POST.get("product")
        product = Product.objects.get(id=id_product)
        get_product = ProductInBasket.objects.filter(product = product)  # удаление элемента
        get_product.delete()
        lst_product = ProductInBasket.objects.filter(user_basket=user)   # цена без удаленного
        total_price -= product.price
    return render(request, "basket.html", {"products":lst_product,'price':total_price})

# Очистить корзину
def delete_all(request):
    user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)   # *
    products = ProductInBasket.objects.filter(user_basket=user)
    products.delete()
    lst_product = ProductInBasket.objects.filter(user_basket=user)
    total_price = 0
    return render(request, "basket.html", {"products":lst_product,'price':total_price})


# Оформлене заказа
def order(request):
    form = FormOrder()
    return render(request, "order.html", {'form_key':form})


# Удалить всю корзину
def order(request):
    form = FormOrder()
    return render(request, "order.html", {'form_key':form})




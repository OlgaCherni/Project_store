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


# Корзина
def basket(request):
    user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)   # *
    lst_product = ProductInBasket.objects.filter(user_basket=user)
    total_price=0
    for price in lst_product:
        total_price+=price.total_price
        print(total_price)
    if request.method == 'POST': 
        lst_product.delete()
    return render(request, "basket.html", {"products":lst_product,'price':total_price})


# оформлене заказа
def order(request):
    form = FormOrder()
    return render(request, "order.html", {'form_key':form})


# Удалит элемент из корзины
def cart_remove(request):
    cart_id = request.POST.get("cart_id")
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)





# # ____________

# # Подсчет стоимости товаров в корзине.                                                        # ____________
# def get_total_price(self):
#     return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


# # Удаление товара из корзины.                                                                  # ____________
# def remove(self, product):
#     product_id = str(product.id)
#     if product_id in self.cart:
#         del self.cart[product_id]
#         self.save()


#  # Mетод для очистки корзины                                                                  # ____________
# def clear(self):
#     del self.session[settings.CART_SESSION_ID]
#     self.session.modified = True



# # ____________
# def cart_add(request):

#     product_id = request.POST.get("product_id")

#     product = Product.objects.get(id=product_id)
    
#     if request.user.is_authenticated:
#         carts = Cart.objects.filter(user=request.user, product=product)

#         if carts.exists():
#             cart = carts.first()
#             if cart:
#                 cart.quantity += 1
#                 cart.save()
#         else:
#             Cart.objects.create(user=request.user, product=product, quantity=1)

#     else:
#         carts = Cart.objects.filter(
#             session_key=request.session.session_key, product=product)

#         if carts.exists():
#             cart = carts.first()
#             if cart:
#                 cart.quantity += 1
#                 cart.save()
#         else:
#             Cart.objects.create(
#                 session_key=request.session.session_key, product=product, quantity=1)
    
#     user_cart = get_user_carts(request)
#     cart_items_html = render_to_string(
#         "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

#     response_data = {
#         "message": "Товар добавлен в корзину",
#         "cart_items_html": cart_items_html,
#     }

#     return JsonResponse(response_data)
            

# def cart_change(request):
#     cart_id = request.POST.get("cart_id")
#     quantity = request.POST.get("quantity")

#     cart = Cart.objects.get(id=cart_id)

#     cart.quantity = quantity
#     cart.save()
#     updated_quantity = cart.quantity

#     cart = get_user_carts(request)
#     cart_items_html = render_to_string(
#         "carts/includes/included_cart.html", {"carts": cart}, request=request)

#     response_data = {
#         "message": "Количество изменено",
#         "cart_items_html": cart_items_html,
#         "quaantity": updated_quantity,
#     }

#     return JsonResponse(response_data)







# # utils шаблонные переменные
# def get_user_carts(request):
#     if request.user.is_authenticated:
#         return Cart.objects.filter(user=request.user).select_related('product')
    
#     if not request.session.session_key:
#         request.session.create()
#     return Cart.objects.filter(session_key=request.session.session_key).select_related('product')
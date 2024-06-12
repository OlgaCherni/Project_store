from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .models import Product, Сategories 
from orders.models import UserBasket, ProductInBasket
from django.contrib import messages
# Create your views here.


# Главая страница
def index(request):                                                                         
    return render(request, "main.html",)


# Добавление в корзину
# def bascet_add(request, product_id):
#     product = Product.objects.get(id=product_id)
#     user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)      # *
#     get_basket = ProductInBasket.objects.filter(product=product, user_basket=user).first()
#     if request.method == 'POST':                                                           
#         name_product = request.POST.get("get_id_produkt")                                
#         quantity = request.POST.get("quantity")
#         if get_basket:
#             get_basket.quantity += int(quantity)
#             get_basket.total_price = get_basket.quantity * product.price
#             get_basket.save()
#         else:
#             new_basket = ProductInBasket.objects.create(
#                 user_basket=user,
#                 product=product,
#                 quantity=int(quantity),
#                 total_price=product.price * int(quantity)
#                 )
#             new_basket.save()
#     print("Ваш товар добавлен в корзину!!") 
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'), locals())


# Категории(борды,лыжи,аксессуары)
def category(request, id):                                                                                                  
    category_filter = Product.objects.filter(сategories=id)                                                         # экземпляр класса из моделей   Вариант: board=Tovar.objects.all().  return render(request, "boards.html", {'ky': board})
    if request.method == 'POST':                                                                                    # кнопка добавить в корзину
        name_product = request.POST.get("get_id_produkt")                                                           # из html запрос по имени инпут
        quantity = request.POST.get("quantity")                                                                     # из html запрос по имени инпут
        product = Product.objects.get(name=name_product)                                                            # из дб дай по названию продукта вернуть=предукту нажали
        user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)                            #- верни пользователя, если существует и запиши в юзер. если не существе=ует -зоднай в _
        get_basket = ProductInBasket.objects.filter(product=product, user_basket=user).first()                      # пер продукт=пролукту из продукт ин баскет. изер ин паскет=юзеру отсюда.  получить первый продукт из корзины (продукт=владелец)
        if get_basket:                                                                                              # Если выбраный пролукт существует в корзине мы добавляем еще один к количеству
            get_basket.quantity += int(quantity)
            get_basket.total_price = get_basket.quantity * product.price                                             # Стоимость общая всех одинаковых товаров
            get_basket.save()                                                                                        # Сохраняем в базе данных обновленные данные о количестве и общий прайс
        else:                                                                                                        # Иначе в корзину добавляем новый продукт
            new_basket = ProductInBasket.objects.create(
                user_basket=user,
                product=product,
                quantity=int(quantity),
                total_price=product.price * int(quantity)
            )
            new_basket.save()
            print(f"Товар {new_basket.product} добавлен в корзину!")
        messages.success(request, "Товар добавлен в корзину!")                                                 #  messages.success-успешно.сообщение. + Импорт!from django.contrib import messages!      
    return render(request, "category.html", {"category_key": category_filter})


# Один продукт
def product(request, itm_id):                                          
    tv = Product.objects.get(id=itm_id)                                # нов пер=из класса моделей получаем из бд объекты по url itm_id (передаем вторым параметром в скобках функции)!
    return render(request, "product.html", locals())                   # locals())  - выводит все переменные из функции


# Поиск по названию или описанию
def search(request):
    query = request.GET.get('query')
    # products_name = Product.objects.filter(name__icontains=query)                      # поиск по названию
    products_description  = Product.objects.filter(description__icontains=query)         # поиск по описанию
    return render(request, "search.html", locals())





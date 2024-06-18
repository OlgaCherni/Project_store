from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .models import Product, Сategories 
from orders.models import UserBasket, ProductInBasket
from django.contrib import messages
# Create your views here.


# Главая страница
def index(request):                                                                         
    return render(request, "main.html",)

# О нас
def about(request):                                                                         
    return render(request, "about.html",)

# Категории(борды,лыжи,аксессуары)
def category(request, id):                                                                                                  
    category_filter = Product.objects.filter(categories=id)                                                         # экземпляр класса из моделей   Вариант: board=Tovar.objects.all().  return render(request, "boards.html", {'ky': board})
    if request.method == 'POST':                                                                                    # кнопка добавить в корзину
        name_product = request.POST.get("get_id_product")                                                           # из html запрос по имени инпут
        product = Product.objects.get(name=name_product)                                                            # из дб дай по названию продукта вернуть=предукту нажали
        post(request, product)                                                                                      #  messages.success-успешно.сообщение. + Импорт!from django.contrib import messages!
    return render(request, "category.html", {"category_key": category_filter})

# Один продукт
def product(request, itm_id):
    product = Product.objects.get(id=itm_id)                                                                        # нов пер=из класса моделей получаем из бд объекты по url itm_id (передаем вторым параметром в скобках функции)!
    if request.method == 'POST':                                                                                    # кнопка добавить в корзину
        post(request, product)
    return render(request, "product.html", locals())                                  # locals())  - выводит все переменные из функции

 # Добавление в корзину
def post(request, product):
    quantity = request.POST.get("quantity")
    user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)                            #- верни пользователя, если существует и запиши в юзер. если не существестует создай в _
    get_basket = ProductInBasket.objects.filter(product=product, user_basket=user).first()
    if get_basket:
            get_basket.quantity += int(quantity)
            get_basket.total_price = get_basket.quantity * product.price
            get_basket.save()
    else:
        new_basket = ProductInBasket.objects.create(
            user_basket=user,
            product=product,
            quantity=int(quantity),
            total_price=product.price * int(quantity)
        )
        new_basket.save()
        print(f"Товар {new_basket.product} добавлен в корзину!")
    product_count(user, request)                                         # Счетчик корзины
    messages.success(request, "Товар добавлен в корзину!")

# Поиск по названию или описанию
def search(request):
    query = request.GET.get('query')
    # products_name = Product.objects.filter(name__icontains=query)                      # поиск по названию
    products_description  = Product.objects.filter(description__icontains=query)         # поиск по описанию
    return render(request, "search.html", locals())

 # Счетчик корзины
def product_count(user, request):
    products = ProductInBasket.objects.filter(user_basket=user)
    count = 0
    for item in products:
        count += item.quantity
    request.session["basket_count"] = count

from django.shortcuts import render, HttpResponse
from .models import Product, Сategories 
from orders.models import UserBasket, ProductInBasket

# Create your views here.

def index(request):                                                      # ГЛАВНАЯ, общий каталог
    return render(request, "main.html",)                     


def boards(request):                                                                  # СНОУБОРД
    b_product  = Сategories.objects.get(namec="Сноуборд")                                  # экземпляр класса из моделей   Варианты: board=Tovar.objects.all().  board=Сategories.objects.filter(namec=True)     return render(request, "boards.html", {'ky': board})       
    board = Product.objects.filter(сategories=b_product)                                   # нов ключ перебирает значения из экземпляра board
    if request.method == 'POST':                                                           # к заказам
        name_product = request.POST.get("get_id_produkt")                                  # имя покупки
        quantity = request.POST.get("quantity")
        print(name_product,quantity)
        product = Product.objects.get(name=name_product)
        user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)   # *
        get_basket=ProductInBasket.objects.filter(product=product).first()
        if get_basket:
            get_basket.quantity+=int(quantity)
            # get_basket.total_price*=quantity
        else:
                new_basket = ProductInBasket.objects.create(
                user_basket = user,
                product = product,
                quantity = 1,
                total_price = product.price
            )       
                new_basket.save()
        print("Ваш товар(сноуборд) добавлен в корзину!")
    return render(request, "boards.html", {"brd": board})


def skis(request):                                                                 # ЛЫЖИ
    s_product  = Сategories.objects.get(namec="Лыжи")
    ski = Product.objects.filter(сategories=s_product)
    if request.method == 'POST':                                
        name_product = request.POST.get("get_id_produkt")                                  
        product = Product.objects.get(name=name_product)
        user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)   # *
        new_basket = ProductInBasket.objects.create(
            user_basket = user,
            product = product,
            quantity = 1,
            total_price = product.price
        ) 
        new_basket.save()
        print("Ваш товар(лыжи) добавлен в корзину!")                                    
    return render(request, "skis.html", {"sk": ski})            


def accessories(request):                                                            # АКСЕССУАРЫ
    a_product  = Сategories.objects.get(namec="Аксессуары")
    accessories = Product.objects.filter(сategories=a_product)
    if request.method == 'POST':                               
        name_product = request.POST.get("get_id_produkt")                                  
        product = Product.objects.get(name=name_product)
        user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)    # *
        new_basket = ProductInBasket.objects.create(
            user_basket = user,
            product = product,
            quantity = 1,
            total_price = product.price
        ) 
        new_basket.save()
        print("Ваш товар(аксуссуары) добавлен в корзину! ") 
    return render(request, "accessories.html", {"acs":accessories})          



def product(request, itm_id):                                          # ОДИН ПРОДУКТ
    tv = Product.objects.get(id=itm_id)                                # нов пер=из класса моделей получаем из бд объекты по url itm_id (передаем вторым параметром в скобках функции)!
    return render(request, "product.html", locals())                   # locals())  - выводит все переменные из функции





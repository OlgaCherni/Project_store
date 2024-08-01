from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage, get_connection
from django.shortcuts import render, redirect
from .models import *
from shop.models import *
from users.models import *
from .forms import FormOrder


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
        product_count(lst_product, request)                                                       # Счетчик корзины
    return render(request, "basket.html", {"products":lst_product,'price':total_price})


# Очистить корзину
def delete_all(request):
    user, _ = UserBasket.objects.get_or_create(user_kay=request.session.session_key)   # *
    products = ProductInBasket.objects.filter(user_basket=user)
    products.delete()
    lst_product = ProductInBasket.objects.filter(user_basket=user)
    total_price = 0
    request.session["basket_count"] = user.productinbasket_set.count()                            # Счетчик корзины
    return render(request, "basket.html", {"products":lst_product,'price':total_price})


# Оформлене заказа
def order(request):
    form = FormOrder()
    user_key = request.session.session_key
    get_basket = UserBasket.objects.get(user_kay=user_key)
    get_user_basket = ProductInBasket.objects.filter(user_basket=get_basket)
    if request.method == 'POST':
        form = FormOrder(request.POST)
        if form.is_valid():     # Создаем новый заказ
            order = Order.objects.create(
                name = form.cleaned_data["name"],
                phone = form.cleaned_data["phone"],
                email = form.cleaned_data["email"],
                adres = form.cleaned_data["adres"],
            )
            # Создаем элементы заказа
            for item in get_user_basket:

                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    name=item.product.name,
                    price=item.product.price,
                    quantity=item.quantity
                )
                product = item.product  

                product.quantity = product.quantity - item.quantity   # Количество на складе минус Количество в заказе
                product.save()
            send_email(request, order, get_user_basket)              # *Сообщение на почту
            get_user_basket.delete()                                 # Чистим корзину
            request.session["basket_count"] = 0
            return redirect('main')
    return render(request, "order.html", {'form_key': form})

# *Сообщение на почту
def send_email(request, order, get_user_basket):
    if request.method == "POST":
        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            subject = "Ваш заказ из магазина SnowWave оформлен успешно!"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [order.email]
            message = create_mail_message(get_user_basket)
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()


def create_mail_message(get_user_basket):
    message = ""
    for item in get_user_basket:
        message += "Ваш заказ: " + item.product.name + ". Благодарим за сотрудничество!" +"\n"
    return message


# Счетчик корзины
def product_count(lst_product, request):
    count = 0
    for item in lst_product:
        count += item.quantity
    request.session["basket_count"] = count
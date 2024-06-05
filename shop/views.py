from django.shortcuts import render, HttpResponse
from .models import Product, Сategories    

# Create your views here.

def index(request):                                           # ГЛАВНАЯ, общий каталог
    return render(request, "main.html",)                     


def boards(request):                                             # СНОУБОРД
    b_product  = Сategories.objects.get(namec="Сноуборд")           # экземпляр класса из моделей   Варианты: board=Tovar.objects.all().  board=Сategories.objects.filter(namec=True)     return render(request, "boards.html", {'ky': board})       
    board = Product.objects.filter(сategories=b_product)            # нов ключ перебирает значения из экземпляра board
    if request.method == 'POST':                                # к заказам
        id_product = request.POST.get("get_id_produkt")         # к заказам
        print(id_product)                                       # к заказам
    return render(request, "boards.html", {"brd": board})           # нов ключ перебирает значения из board(экземпляра классаProduct)


def skis(request):                                             # ЛЫЖИ
    s_product  = Сategories.objects.get(namec="Лыжи")
    ski = Product.objects.filter(сategories=s_product)
    if request.method == 'POST':                                # к заказам
        id_product = request.POST.get("get_id_produkt")         # к заказам
        print(id_product)                                       # к заказам           
    return render(request, "skis.html", {"sk": ski})            


def accessories(request):                                      # АКСЕССУАРЫ
    a_product  = Сategories.objects.get(namec="Аксессуары")
    accessories = Product.objects.filter(сategories=a_product)
    if request.method == 'POST':                                # к заказам
        id_product = request.POST.get("get_id_produkt")         # к заказам
        print(id_product)                                       # к заказам              
    return render(request, "accessories.html", {"acs":accessories})          



def product(request, itm_id):                                # ОДИН ПРОДУКТ
    tv = Product.objects.get(id=itm_id)                       # нов пер=из класса моделей получаем из бд объекты по url itm_id (передаем вторым параметром в скобках функции)!
    return render(request, "product.html", locals())          # locals())  - выводит все переменные из функции





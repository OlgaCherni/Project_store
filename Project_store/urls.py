"""
URL configuration for Project_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static                                              # 3(5)шаг для отображения на странице картинок из базы данных
from django.conf import settings                                                        # 4(5)шаг для отображения на странице картинок из базы данных
from shop import views as shop
from users import views as user                                                         # или from users.views import , (все функции!)
from django.contrib.auth.views import LogoutView
from orders import views as order


urlpatterns = [
    path('admin/', admin.site.urls),                                     

    path("", shop.index, name="main"),                                                  # Главная страница
    path("about", shop.about, name="about"),                                            # О нас
    path("category/<int:id>", shop.category, name="category"),                          # Категории(борды/лыжи/аксессуары)
    
    path("product/<int:itm_id>", shop.product, name="product_page"),                    # Один продукт выводим по id из бызы данных(каждый элемент имеет уникальный id). Динамисечский url  <int:itm_id> - int *люб.нов.пер/_id.     И в *пер   tv = Product.objects.get(id=itm_id)
    path("search/", shop.search, name="search"),                                        # Поиск по сайту. Префикс/ гдеФункция Имя genb в html.

    path("reg", user.registration, name="registr"),                                     # Регистрация (суф/ прил(или views).функция1(из вьюс), +-name(краткое имя пути)обычно называют, как html файл! Потом<a href="{% url"registr" %}">
    path("login/", user.log, name="login"),                                             # Логин вход 
    path("logout/", LogoutView.as_view, name="logout"),                                 # Выход 
    
    path("basket/", order.basket, name="basket"),                                       # Корзина Изменить содержимое карзины
    path("order/", order.order, name="order"),                                          # Заказ
    path("basket/delete/", order.delete_all, name="delete_all"),                        # Очистить корзину   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)            # 5(5)шаг для отображения на странице картинок из базы данных. 
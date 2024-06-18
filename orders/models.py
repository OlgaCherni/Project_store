from django.db import models
from shop.models import Product

# Владелец корзины
class UserBasket(models.Model):
    user_kay = models.CharField(max_length=128, blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.user_kay}"

    class Meta:
        verbose_name = "Ключи Сессии Анонимный пользователь"
        verbose_name_plural = "Анонимные пользователи"


# Заказ
class ProductInBasket(models.Model):
    user_basket = models.ForeignKey(UserBasket, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name="Наименование товара")
    quantity = models.IntegerField(verbose_name='Количество', default=1)
    total_price = models.FloatField(verbose_name='Общая стоимость товара', blank=True, null=True, default=0)

    def __str__(self):
        return f"{self.user_basket}"

    class Meta:
        verbose_name = "Товары в корзине"
        verbose_name_plural = "Товары в корзине"


# Храним сделанные заказы(журнал заказов)
class Order(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    phone = models.CharField(max_length=150, verbose_name="Телефон")
    email = models.CharField(max_length=150, verbose_name="Почта")
    adres = models.CharField(max_length=150, verbose_name="Адрес")

    class Meta:
        verbose_name = "Журнал заказов"
        verbose_name_plural = "Журнал заказов"


# Заказ
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT,null=True, verbose_name="Продукт", default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")

    def __str__(self):
        return f"{self.name} - {self.quantity}"

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"








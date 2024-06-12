from django.db import models
from shop.models import Product

# Create your models here.\

class UserBasket(models.Model):                                                           # владелец корзины
    user_kay =  models.CharField(max_length=128,blank=True , null=True, default=None)
    

class ProductInBasket(models.Model):                                                      # заказ
    user_basket=models.ForeignKey(UserBasket, on_delete=models.CASCADE,null=True)         # *
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True, verbose_name="Наименование товара")
    quantity = models.IntegerField(verbose_name='Количество', default=1)
    total_price = models.FloatField(blank=True,null=True,default=0)

# Храним сделанные заказы(журнал заказов)
class Order(models.Model):
    product = models.ForeignKey(ProductInBasket, on_delete = models.CASCADE, blank=False, default=True)  # ОДИН КО МНОГИМ 
    name = models.CharField(max_length=150, verbose_name="Имя")
    phone = models.CharField(max_length=150, verbose_name="Телефон")
    email = models.CharField(max_length=150, verbose_name="Почта")
    adres = models.CharField(max_length=150, verbose_name="Адрес")






# # ____________
    
# class Cart(models.Model):                                                                      # ____________
#     total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)


# # ____________
# from django.db import models
# from shop.models import Products

# from users.models import User


# class CartQueryset(models.QuerySet):
    
#     def total_price(self):
#         return sum(cart.products_price() for cart in self)
    
#     def total_quantity(self):
#         if self:
#             return sum(cart.quantity for cart in self)
#         return 0
    

# class Cart(models.Model):       # Корзина товар в корзине

#     user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь ')   # кому пренадлежит корзина
#     product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')                # продукт в корзине 
#     quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')                     # количество добавленного товара
#     session_key = models.CharField(max_length=32, null=True, blank=True)                               # количеств
#     created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')            # дата 

#     class Meta:                                             # в админке таблица
#         db_table = 'cart'                                      # Так будет называться таблица в базе данных cart
#         verbose_name = "Корзина"
#         verbose_name_plural = "Корзина"

#     objects = CartQueryset().as_manager()

#     def products_price(self):
#         return round(self.product.sell_price() * self.quantity, 2)


#     def __str__(self):
#         if self.user:
#             return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'
            
#         return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'
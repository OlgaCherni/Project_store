from django.db import models
from shop.models import Product

# Create your models here.\

class UserBasket(models.Model):                                                           # пользователь
    user_kay =  models.CharField(max_length=128,blank=True , null=True, default=None)
    
class ProductInBasket(models.Model):                                                      # продукты в корзине
    user_basket=models.ForeignKey(UserBasket, on_delete=models.CASCADE,null=True)         # *
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True, verbose_name="Наименование товара")
    quantity = models.IntegerField( verbose_name="Количество", null=True, blank=True)
    total_price = models.FloatField(blank=True,null=True,default=0)



    


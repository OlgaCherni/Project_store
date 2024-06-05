from django.db import models

# Create your models here.

class Сategories(models.Model):                                                                 # 3 вида товара Категории: сноуборд лыжи аксессуары. Наследуемся от встроеного класса.               
    namec = models.CharField(max_length=80, verbose_name= "Категория товара")
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.namec                                                                      # Визуал в админке списоком по имени капегорий

    class Meta:                                                                                # В админ панели имя.
        verbose_name = "Категория"      
        verbose_name_plural = "Категории"


class Product(models.Model):                                                                               # ОДИН КО МНОГИМ модель Товар(разные модели по трем категориям)
    сategories = models.ForeignKey(Сategories, on_delete = models.CASCADE, blank=False, default=True)    
    name = models.CharField(max_length=150, verbose_name="Наименование")
    image = models.ImageField(upload_to ='static\imagebd', verbose_name="Картинка", null=True, blank=True)      # 1(5)шаг для отображения на странице картинок из базы данных                                                         
    price = models.IntegerField(verbose_name="Цена")
    description = models.TextField(max_length=900, blank=True, verbose_name="Описание товара")  
    quantity = models.IntegerField( verbose_name="Количество", null=True, blank=True)  
    is_active = models.BooleanField(verbose_name="В наличии", blank=False, default=True)

    def __str__(self):
        return f"Товар:{self.name}"                                                  # Визуал в админке.
    
    class Meta:                                                                      # В админ панели имя.
        verbose_name = "Продукт"      
        verbose_name_plural = "Продукты"
    

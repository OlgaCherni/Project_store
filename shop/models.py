from django.db import models

# Create your models here.

class Сategories(models.Model):                                                                 #-С 3 категории: сноуборд лыжи аксессуары. Наследуемся от встроеного класса.               
    namec = models.CharField(max_length=80, verbose_name= "Категория товара")

    class Meta:                                              # В админ можно вносить коррективы в название класса Категории
        db_table = 'category'                                # Так будет называться класс в админке, вмето ()
        verbose_name = 'Категорию'                           # альтернативное имя для db_table
        verbose_name_plural = 'Категории'                    # альтернативное имя для db_table мн.ч

    def __str__(self):
        return self.namec                                                                      # Визуал в админке списоком по имени категорий


class Product(models.Model):                                                                               #Один ко многим. Разные товары по 3 категориям.
    сategories = models.ForeignKey(Сategories, on_delete = models.CASCADE, blank=False, default=True)    
    name = models.CharField(max_length=150, verbose_name="Наименование")
    image = models.ImageField(upload_to ='static\imagebd', verbose_name="Картинка", null=True, blank=True)      # 1(5)шаг для отображения на странице картинок из базы данных                                                         
    description = models.TextField(max_length=900, blank=True, verbose_name="Описание товара") 
    price = models.IntegerField(verbose_name="Цена") 
    quantity = models.IntegerField( verbose_name="Количество", null=True, blank=True)  
    is_active = models.BooleanField(verbose_name="В наличии", blank=False, default=True)

    class Meta:                                         # В админ панели имя таблицы класса.
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)                   # кортеж. товары сортируются по id

    def __str__(self):                                  # Визуал в админке.
        return f'{self.name} Количество - {self.quantity}'                      # что будет отображаться в админке
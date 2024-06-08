from django.db import models
from django.contrib.auth.models import User           # !

# Create your models here.


class Customer(models.Model):                                # ПОЛЬЗОВАТЕЛЬ 
    name = models.CharField(max_length=50, verbose_name="Имя")                # !  name = models.OneToOneField(User, on_delete=models.CASCADE)
    second_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(max_length=50, verbose_name="Почта")
    password = models.CharField(max_length=40, verbose_name="Пороль") 
    contact_number = models.CharField(max_length=50, default="+375447756610")    # !

    def __str__(self):
        return self.name                                    # визуал в админке
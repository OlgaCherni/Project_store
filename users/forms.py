# Перекидываем это во вьюху
from django import forms
from django.contrib.auth.models import User # !


class FormRegistration(forms.Form):                                                          
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))                              
    second_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Создайте пароль'}))


class FormLogIn(forms.Form):                                                          
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ваш пароль'}))





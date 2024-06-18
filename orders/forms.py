from django import forms

# Создает форму в которую вводим данные пользователя, делающего заказ
class FormOrder(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'})) 
    # second_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))                       
    phone =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    adres = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Адрес'}))


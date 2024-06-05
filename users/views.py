from django.shortcuts import render, redirect, HttpResponse
from .forms import FormRegistration, FormLogIn        
from .models import Customer

# Create your views here.

def registration(request):
    user_form = FormRegistration()           
    if request.method == 'POST':
        user_form = FormRegistration(request.POST)                         
        if user_form.is_valid():
            fname = user_form['name']  
            fsecond_name = user_form['second_name']
            femail = user_form['email']
            fpassword = user_form['password']

            creat_user=Customer.objects.create(name=fname, second_name=fsecond_name, email=femail, password=fpassword)         # 1атрибут из модели 2из формы  
            creat_user.save()        # сохранили в базе данных +-
            return redirect("main")                          # перенаправляем - имя урла 
        else:
            return HttpResponse(f"Форма не валидна")
    else:
        return render(request, 'registration.html', {'key':user_form})     # отображаем экз с формами


def log(request):
    user_form = FormLogIn()           
    if request.method == 'POST':
        user_form = FormLogIn(request.POST)                         
        if user_form.is_valid():
            femail = user_form['email']
            fpassword = user_form['password']

            creat_user=Customer.objects.create(email=femail, password=fpassword)           
            creat_user.save()       
            return redirect("main")               # перенаправляем - имя урла 
        else:
            return HttpResponse(f"Форма не валидна")
    else:
        return render(request, "log_in.html", {'key':user_form})      # отображаем экз с формами

    



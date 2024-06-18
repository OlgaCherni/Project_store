from django.shortcuts import render, redirect, HttpResponse
from .forms import FormRegistration, FormLogIn        
from .models import Customer
from django.contrib import messages
from django.contrib.auth.views import LogoutView

# Create your views here.

def registration(request):
    user_form = FormRegistration()           
    if request.method == 'POST':
        user_form = FormRegistration(request.POST)       # создаю экземпляр формы                          
        if user_form.is_valid():                        # проверка на валод. Если форма валидна
            fname = user_form['name']  
            fsecond_name = user_form['second_name']
            femail = user_form['email']
            fpassword = user_form['password']

            creat_user=Customer.objects.create(name=fname, second_name=fsecond_name, email=femail, password=fpassword)         # 1атрибут из модели 2из формы  
            creat_user.save()                     # сохранили в базе данных +-
            messages.success(request, f"Вы успешно зарегистрированы и вошли в аккаунт")     #  messages.success-успешно.сообщение. + Импорт!from django.contrib import messages!      
            return redirect("main")                          # перенаправлили-имя урла 
        else:
            return HttpResponse(f"Форма не валидна")
    else:
        return render(request, 'registration.html', {'key':user_form})     # отображаем экз с формами


def log(request):
    user_form = FormLogIn()                              # создаю экземпляр формы                 
    if request.method == 'POST':
        user_form = FormLogIn(request.POST)                                  
        if user_form.is_valid():                          # проверка на валодацию. Если форма валидна
            femail = user_form['email']
            fpassword = user_form['password']

            creat_user=Customer.objects.create(email=femail, password=fpassword)           
            creat_user.save() 
            messages.success(request, f" Вы успешно вошли в аккаунт")     #  messages.success-успешно.сообщение. + Импорт!from django.contrib import messages!      
            return redirect("main")               # перенаправляем на main - имя урла главной страницы
        else:
            return HttpResponse(f"Форма не валидна")
    else:
        return render(request, "log_in.html", {'key':user_form})      # отображаем экз с формами

    
class Logout_user(LogoutView):
    template_name='main'



# # ____________

# # Декоратор доступа
# @login_required       # Декоратор доступа запрещает доступ неавторизованным пользователям
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)       #  instance=request.user-лчная инфа пользователя. files=request.FILES-чтоб форма могла примять файлы(фото профиля)
#         if form.is_valid():                            
#             form.save()
#             messages.success(request, "Профайл успешно обновлен")
#             return HttpResponseRedirect(reverse('user:profile'))
#     else:
#         form = ProfileForm(instance=request.user)        # пользователь вошел-подтягиваем его инфу имя, фамилия... параметр instance=request.user

#     orders = Order.objects.filter(user=request.user).prefetch_related(
#                 Prefetch(
#                     "orderitem_set",
#                     queryset=OrderItem.objects.select_related("product"),
#                 )
#             ).order_by("-id")
        

#     context = {
#         'title': 'SW - Кабинет',
#         'form': form,
#         'orders': orders,
#     }
#     return render(request, 'users/profile.html', context)

# def users_cart(request):
#     return render(request, 'users/users_cart.html')


# # Декоратор доступа
# @login_required             # Декоратор доступа на выход из аккаунта
# def logout(request):
#     messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
#     auth.logout(request)
#     return redirect(reverse('main:index'))
# from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseNotFound, Http404

# # from django.conf import settings
# from user.models import *

# def register(request):
#     context = {
#         'title': 'Регистрация | Тамбовская Ювелирная Компания',
#         'description': 'Тамбовская Ювелирная Компания, Регистрация прльзователя',
#     }
#     return render(request, "user/register.html", context)


# def login(request):
#     context = {
#         'title': 'Авторизация | Тамбовская Ювелирная Компания',
#         'description': 'Тамбовская Ювелирная Компания, Авторизация прльзователя',
#     }
#     return render(request, "user/login.html", context)


from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Создаем здесь представления. 
 
def home(request):
    return render(request,"users/home.html")



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
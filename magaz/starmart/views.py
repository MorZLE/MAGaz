from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *

# Create your views here.

menu = ['Товары', 'О нас', 'Корзина', 'Войти']


def index(request):
    good = Goods.objects.all()
    return render(request, 'starmart/index.html', {'menu': menu, 'title': 'Главная страница', 'goods': good})


def goods(request):
    return HttpResponse('Все товары')


def categories(request, cat):
    return HttpResponse(f'категория  {cat}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

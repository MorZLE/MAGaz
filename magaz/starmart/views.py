from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *

# Create your views here.

menu = [{'title': 'Товары', 'url_name': 'goods'}, {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Корзина', 'url_name': 'basket'}, {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    good = Goods.objects.all()
    return render(request, 'starmart/index.html', {'menu': menu, 'title': 'Главная страница', 'goods': good})


def goods(request):
    good = Goods.objects.all()
    cat = Categories.objects.all()
    context = {
        'menu': menu,
        'title': 'Товары',
        'goods': good,
        'cat': cat
    }
    return render(request, 'starmart/goods.html', context=context)


def show_good(request, good):
    good = Goods.pk

    context = {
        'menu': menu,
        'title': 'Товары',
        'goods': good
    }
    return render(request, 'starmart/good.html', context=context)


def categories(request, cat):
    return HttpResponse(f'Категория {cat}')


def about(request):
    context = {
        'menu': menu,
        'title': 'О нас',
    }
    return render(request, 'starmart/about.html', context=context)


def basket(request):
    context = {
        'menu': menu,
        'title': 'Корзина'
    }
    return render(request, 'starmart/basket.html', context=context)


def login(request):
    context = {
        'menu': menu,
        'title': 'Авторизация'
    }
    return render(request, 'starmart/login.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

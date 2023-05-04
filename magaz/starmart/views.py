from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *



menu = [{'title': 'Товары', 'url_name': 'goods'}, {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Корзина', 'url_name': 'basket'}, {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    cat = Categories.objects.all()
    context = {
        'menu': menu,
        'title': 'Товары',
        'cat': cat
    }
    return render(request, 'starmart/index.html', context=context)


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
    good = Goods.objects.filter(pk=good)
    cat = Categories.objects.all()
    context = {
        'menu': menu,
        'title': 'Товары',
        'good': good,
        'cat': cat
    }
    return render(request, 'starmart/good.html', context=context)


def show_category(request, cat):
    good = Goods.objects.filter(category_id=cat)
    cat = Categories.objects.all()
    context = {
        'menu': menu,
        'title': 'Товары',
        'goods': good,
        'cat': cat
    }
    return render(request, 'starmart/goods.html', context=context)


def about(request):
    cat = Categories.objects.all()
    context = {
        'menu': menu,
        'title': 'О нас',
        'cat': cat
    }
    return render(request, 'starmart/about.html', context=context)


def basket(request):
    cat = Categories.objects.all()
    context = {
        'menu': menu,
        'title': 'Корзина',
        'cat': cat
    }
    return render(request, 'starmart/basket.html', context=context)


def login(request):
    cat = Categories.objects.all()
    context = {
        'menu': menu,
        'title': 'Авторизация',
        'cat': cat
    }
    return render(request, 'starmart/login.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

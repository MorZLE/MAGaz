from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

menu = ['Главная', 'Товары', 'О нас', 'Войти']


def index(request):
    return render(request, 'starmart/index.html', {'menu': menu, 'title': 'Главная страница'})


def goods(request):
    return HttpResponse('Все товары')


def categories(request, cat):
    return HttpResponse(f'категория  {cat}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

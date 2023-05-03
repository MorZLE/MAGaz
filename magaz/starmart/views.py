from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Главная')


def goods(request):
    return HttpResponse('Все товары')


def categories(request, cat):
    return HttpResponse(f'категория  {cat}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

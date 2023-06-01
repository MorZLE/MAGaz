from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView, DetailView

from .models import *


menu = [{'title': 'Товары', 'url_name': 'goods'}, {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Корзина', 'url_name': 'basket'}, {'title': 'Войти', 'url_name': 'login'}]


class ShopHome(ListView):
    model = Goods
    context_object_name = 'goods'
    template_name = 'starmart/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cat'] = Categories.objects.all()
        context['title'] = 'Главная'
        return context


class ShopGoods(ListView):
    model = Goods
    context_object_name = 'goods'
    template_name = 'starmart/goods.html'
    good = Goods.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cat'] = Categories.objects.all()
        context['title'] = 'Товары'
        context['goods'] = self.good
        return context

    def get_queryset(self):
        return Goods.objects.filter(is_published=True)

class ShowGood(DetailView):
    model = Goods
    template_name = 'starmart/good.html'
    pk_url_kwarg = 'good'
    context_object_name = 'good'


class ShowCategory(ListView):
    model = Goods
    context_object_name = 'goods'
    template_name = 'starmart/goods.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cat'] = Categories.objects.all()
        context['title'] = 'Товары'
        return context

    def get_queryset(self):
        return Goods.objects.filter(category_id=self.kwargs['cat'], is_published=True)




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

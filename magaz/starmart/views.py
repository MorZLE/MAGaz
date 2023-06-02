from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView


from .models import *
from .utils import *


class ShopHome(DataMixin, ListView):
    model = Goods
    context_object_name = 'goods'
    template_name = 'starmart/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная')
        return dict(list(context.items())+list(c_def.items()))


class ShopGoods(DataMixin, ListView):
    model = Goods
    context_object_name = 'goods'
    template_name = 'starmart/goods.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Товары')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Goods.objects.filter(is_published=True)

class ShowGood(DataMixin, DetailView):
    model = Goods
    template_name = 'starmart/good.html'
    pk_url_kwarg = 'good'
    context_object_name = 'good'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Товары')
        return dict(list(context.items()) + list(c_def.items()))


class ShowCategory(DataMixin, ListView):
    model = Goods
    context_object_name = 'goods'
    template_name = 'starmart/goods.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Товары')
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Goods.objects.filter(category_id=self.kwargs['cat'], is_published=True)


class ShopAdmin(LoginRequiredMixin, DataMixin, ListView):
    model = Goods
    context_object_name = 'goods'
    template_name = 'starmart/admin.html'
  #  raise_exception = True
   # login_url = reverse_lazy('login')
    login_url = '/admin'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Админка")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        pass


class ShopAbout(DataMixin, ListView):
    template_name = 'starmart/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О нас")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        pass



class ShopBasket(DataMixin, ListView):
    template_name = 'starmart/basket.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Корзина")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        pass

class ShopLogin(DataMixin, ListView):
    template_name = 'starmart/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Вход")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        pass



def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

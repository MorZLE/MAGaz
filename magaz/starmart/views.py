from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import RegisterUserForm, LoginUserForm, QuantityBasketForm
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
    paginate_by = 6
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
    paginate_by = 6
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
    login_url = reverse_lazy('login')
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
    model = Basket
    context_object_name = 'basket'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Корзина")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user = self.request.session.session_key
        return Basket.objects.filter(user=user)


def basket_qu(request, product_id, value):
    basket = Basket.objects.filter(id=product_id).update(quantity=value)
    basket.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def basket_add(request, product_id):
    if request.user.is_authenticated:
       user = request.user
    else:
       user = request.session.session_key

    product = Goods.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


class ProfileUser(DataMixin, ListView):
    template_name = 'starmart/profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Профиль")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        pass


class ShopLogin(DataMixin, LoginView):
    template_name = 'starmart/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Вход")
        return dict(list(context.items()) + list(c_def.items()))


class ShopRegister(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'starmart/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')



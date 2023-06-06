from django.db.models import Count

from starmart.models import Categories

menu = [{'title': 'Товары', 'url_name': 'goods'}, {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Корзина', 'url_name': 'basket'}]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Categories.objects.annotate(Count('goods'))
        user_menu = menu.copy()
        context['menu'] = user_menu
        context['cat'] = cats
        return context

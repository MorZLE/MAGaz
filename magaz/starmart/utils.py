from django.db.models import Count

from starmart.models import Categories

menu = [{'title': 'Товары', 'url_name': 'goods'}, {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Корзина', 'url_name': 'basket'},
        {'title': 'Админка', 'url_name': 'admin'}]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Categories.objects.annotate(Count('goods'))
        user_menu = menu.copy()

        if not self.request.user.is_superuser:
            user_menu.pop(3)



        context['menu'] = user_menu
        context['cat'] = cats
        return context

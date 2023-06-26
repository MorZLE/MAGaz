from ..models import Goods,Basket


def get_all_goods():
    return Goods.objects.filter(is_published=True)


def get_cat_gooos():
    return Goods.objects.filter(category_id=self.kwargs['cat'], is_published=True)


def show_shop_basket(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = request.session.session_key
    return Basket.objects.filter(user=user)




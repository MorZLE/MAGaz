from ..models import Goods,Basket


class LogicGood:
    @staticmethod
    def get_all_goods():
        return Goods.objects.filter(is_published=True)

    @staticmethod
    def get_cat_goods(kwargs):
        return Goods.objects.filter(category_id=kwargs['cat'], is_published=True)

    @staticmethod
    def show_shop_basket(request):
        if request.user.is_authenticated:
            user = request.user
        else:
            user = request.session.session_key
        return Basket.objects.filter(user=user)




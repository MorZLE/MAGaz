from .Base_Logic import BaseLogic
from ..models import *


class LogicBasket:
    @staticmethod
    def update_good_basket(product_id, value):
        basket = Basket.objects.filter(id=product_id).update(quantity=value)
        basket.save()

    @staticmethod
    def add_basket(request, product_id):
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

    @staticmethod
    def delete_good_basket(basket_id):
        basket = Basket.objects.get(id=basket_id)
        basket.delete()

    @staticmethod
    def bay_goods_basket(request, form: dict):
        user = BaseLogic.user_authenticated(request)
        order = Order.objects.create(user=user, RecipientData=RecipientData.objects.create(**form), paid=False)
        for p in Basket.objects.filter(user=user):
            OrderItem.objects.create(order=order, product=p.product, price=p.sum(),
                                     quantity=p.quantity)
        LogicBasket.delete_user_basket(request)

    @staticmethod
    def delete_user_basket(request):
        basket = Basket.objects.filter(user=BaseLogic.user_authenticated(request))
        basket.delete()

from ..models import Goods,Basket


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

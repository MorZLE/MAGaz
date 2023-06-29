from .Base_Logic import BaseLogic
from ..models import *


class LogicProfile:
    @staticmethod
    def get_user_orders(request):
        user = BaseLogic.user_authenticated(request)
        order = Order.objects.filter(user=user)
        print(order)
        result = []
        for r in order:
            result.append(OrderItem.objects.filter(order=r))
        print(result)
        return result

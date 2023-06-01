from django.urls import path, include

from starmart.views import *


urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('goods/', ShopGoods.as_view(), name='goods'),
    path('about/', about, name='about'),
    path('basket/', basket, name='basket'),
    path('login/', login, name='login'),
    path('good/<int:good>/', ShowGood.as_view(), name='good'),
    path('cat/<int:cat>', ShowCategory.as_view(), name='cat')
]

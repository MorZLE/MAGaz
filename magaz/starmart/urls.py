from django.urls import path, include

from starmart.views import *


urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('goods/', ShopGoods.as_view(), name='goods'),
    path('about/', ShopAbout.as_view(), name='about'),
    path('basket/', ShopBasket.as_view(), name='basket'),
    path('login/', ShopLogin.as_view(), name='login'),
    path('register/', ShopRegister.as_view(), name='register'),
    path('adminka/', ShopAdmin.as_view(), name='admin'),
   # path('adminka/order', ShopAdminOrder.as_view(), name='AdminOrder'),
    path('good/<int:good>/', ShowGood.as_view(), name='good'),
    path('cat/<int:cat>', ShowCategory.as_view(), name='cat'),
    path('logout/', logout_user, name='logout'),
    path('accounts/profile/', ProfileUser.as_view(), name='profile'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('baskets/qu/<int:basket_id>&<int:value>/', basket_qu, name='basket_qu')

]

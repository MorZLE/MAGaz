from django.urls import path, include

from starmart.views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<slug:cat>', categories),
    path('goods/', goods, name='goods'),
    path('about/', about, name='about'),
    path('basket/', basket, name='basket'),
    path('login/', login, name='login'),
    path('good/<int:good>/', show_good, name='good')

]

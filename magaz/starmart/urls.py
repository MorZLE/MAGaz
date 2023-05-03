from django.urls import path, include

from starmart.views import *

urlpatterns = [
    path('', index),
    path('cats/<slug:cat>', categories),
    path('goods/', goods),
]

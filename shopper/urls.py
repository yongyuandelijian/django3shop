# shopper 的urls设置
from django.urls import path
from .views import *

urlpatterns=[
    path('.html',shopperView,name='shopper'),
    path('login.html',loginView,name='login'),
    path('logout.html',loginoutView,name='loginout'),
    path('shopcart.html',shopcartView,name='shopcart'),
    path('delete.html',shanchuView,name='delete')
]
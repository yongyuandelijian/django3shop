# showware的urls设置
from django.urls import path
from .views import *

urlpatterns=[
    path('.html',showwareView,name='showware'),
    path('/waredetail.<int:wareid>.html',waredetailView,name='waredetail')
]
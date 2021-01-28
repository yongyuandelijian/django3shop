# index的urls配置
from django.urls import path
from .views import indexView

urlpatterns=[
    # path('',indexView,name='index')  直接调用方法
    path('',indexClassView.as_view(),name='index')  # 调用类的方法
]
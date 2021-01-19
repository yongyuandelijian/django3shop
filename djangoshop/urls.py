"""djangoshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include     # 导入re_path正则匹配路径
from django.views.static import serve    # 
from django.conf import settings         # 导入配置文件信息

urlpatterns = [
    path('admin/', admin.site.urls),
    # 设置各个app的路由分发规则,
    # 需要说明的是：namespace是可选参数，它可以帮助快速定位到指定app的路由，当设置这个参数，第一个参数必须两个值，否则就会提示错误，元组第一个值指定处理app的路由，第二个值除了空可以自己命名，但是一般我们都设置为app的名称
    path('',include(('index.urls','index'),namespace='index')),
    path('showware',include(('showware.urls','showware'),namespace='showware')),
    path('shopper',include(('shopper.urls','shopper'),namespace='shopper')),
    # 配置媒体资源的路由信息
    re_path('media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT},name='media') # document_root写错了也会导致500错误
]

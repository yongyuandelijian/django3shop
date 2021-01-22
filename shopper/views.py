from django.shortcuts import render

# Create your views here.
from django.db import connection
cursor=connection.cursor()    # 利用连接创建游标
cursor.execute('select * from shoper_order_info where id=5')   # 执行sql
cursor.fetchone()   # 获取第一行数据
cursor.fetchall()   # 获取所有数据


# 登录，注销，购物车，个人中心

def shopperView():
    pass

def loginView():
    pass

def loginoutView():
    pass

def shopcartView():
    pass
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from django.db import connection
# cursor=connection.cursor()    # 利用连接创建游标
# cursor.execute('select * from shoper_order_info where id=5')   # 执行sql
# cursor.fetchone()   # 获取第一行数据
# cursor.fetchall()   # 获取所有数据


# 登录，注销，购物车，个人中心

def shopperView():
    return HttpResponse('一个炫酷的个人中心。。。')

def loginView():
    return HttpResponse('您的登录正在处理中。。。')

def loginoutView():
    return HttpResponse('注销成功。。。')

def shopcartView():
    return HttpResponse('正在展示购物车。。。')
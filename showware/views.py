from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 展示商品  商品详细

def showwareView():
    return HttpResponse('正在努力展示商品。。。')

def waredetailView(wareid):
    return HttpResponse('正在努力展示商品详情。。。',wareid)
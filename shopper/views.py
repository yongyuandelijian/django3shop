from django.shortcuts import render,redirect,reverse    # 从快捷方式导入重定向后者直接提供我都忍了，这个reverse的功能居然想等于模板中的url 就是将路由命名解析成路由地址
from django.contrib.auth.models import User     # 导入用户模型来查询数据
from django.contrib.auth import login,authenticate  # 导入凭证的验证方法，以及登录方法
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

def loginView(request):
    title="正在进行炫酷的登录"
    classContent="logins"
    if request.method=="POST":
        # 获取请求参数用户名和密码
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        if User.objects.filter(username=username):
            user=authenticate(username=username,password=password) # 如果给的凭据是有效的，则返回一个用户对象
            if user:
                login(request,user) # 使用内置login方法进行登录
                return redirect(reverse("shopper:shopper"))# 重定向到个人中心,这个reverse可不是反转，他的作用是将路由命名解析成路由地址
            else:
                state="用户名或者密码不正确"
        else:
            state="注册成功"
            d=dict(username=username,password=password,is_staff=1,is_active=1)
            user=User.objects.create_user(**d)  # 这个和create_superuser差别就是登录后台和是不是超级管理员两个字段的值不同
            # User.objects.create()   这个和上面create_user的区别是，create_user会自动给密码进行加密，而create会当成一般对象直接去创建存储到库里
            user.save()
    return render(request,'login.html',locals())


def loginoutView():
    return HttpResponse('注销成功。。。')

def shopcartView():
    return HttpResponse('正在展示购物车。。。')
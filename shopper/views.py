from django.shortcuts import render,redirect,reverse    # 从快捷方式导入重定向后者直接提供我都忍了，这个reverse的功能居然想等于模板中的url 就是将路由命名解析成路由地址
from django.contrib.auth.models import User     # 导入用户模型来查询数据
from django.contrib.auth import login,authenticate,logout  # 导入凭证的验证方法，以及登录,退出方法
from .form import *
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required

# 功能：登录，注销，购物车，个人中心
# 装饰器用来校验有没有登录，如果没有登录则需要跳转到指定界面，这个装饰器三个参数
# 1 function默认是None 定义装饰器执行的函数，一般不动
# 2 通过redirect_field_name默认值next实现了登录之后就会自动跳转回来
# 3 login_url 设置用户登录的url ,默认是setting.py中的配置属性LOGIN_URL 这个属性默认是没有的，需要自己增加
@login_required(login_url='/shopper/login.html')
def shopperView(request):
    """展示当前用户基本信息"""
    title="炫酷的个人中心"
    classContent="informations"
    pageNum=request.GET.get("pageNum",1)    # 订单信息的显示页数
    # 如果订单已经支付，则先将会话中的订单信息存储到库里
    buyTime=request.GET.get("buyTime",'')  # 系统订单支付时间
    payTime=request.session.get('payTime','')  # 支付返回的时间
    if buyTime and payTime and buyTime==payTime:
        payInfo=request.session.get('payInfo','')
        order_info.objects.create(**payInfo)
        del request.session['payTime']
        del request.session['payInfo']

    # 根据当前用户查询订单信息
    orderInfoList=order_info.objects.filter(user_id=request.user.id).order_by('-createtime')
    # 分页功能,如果传入的页码不是数字，则显示第一页，如果传入的页码不存在，则显示最后一页,最后返回要给界面的当前页面元素
    paginator=Paginator(orderInfoList,7)
    pages=None
    try:
        pages=paginator.page(pageNum)
    except PageNotAnInteger:
        pages=paginator.page(1)
    except EmptyPage:
        pages=paginator.page(paginator.num_pages)
    return render(request,'shopper.html',locals())

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

def loginView2(request):
    """使用loginForm类来实现登录功能"""
    title="正在登录"
    classContent="logins"
    # 处理http的post请求
    if request.method=="POST":
        infos=LoginForm(data=request.POST)   # 感觉和上面原始的区别就是这句话，原始从request里获取数据的，现在从loginForm中获取的
        # 验证表单数据是否准确
        if infos.is_valid():
            data=infos.cleaned_data
            username=data['username']
            password=data['password']
            # 查找User是否已有用户信息
            if User.objects.filter(username=username):
                user=authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    return redirect(reverse("shopper:shopper"))
                else:
                    state="用户名或者密码不正确"
            else:
                state="注册成功"
                d=dict(username=username,password=password,is_staff=1,is_active=1)
                user=User.objects.create_user(**d)
                user.save()
        else:
            # 获取到的信息验证不通过，以json格式输出
            error_msg=infos.errors.as_json()
            print(error_msg)
    else:
        # 处理get请求
        infos=LoginForm()
        return render(request,"login.html",locals())




def loginoutView(request):
    # 使用内置函数logout来退出用户登录状态
    logout(request)
    return redirect(reverse('index:index'))   # 重定向到首页

def shopcartView():
    return HttpResponse('正在展示购物车。。。')
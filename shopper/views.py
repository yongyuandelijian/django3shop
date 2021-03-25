from django.shortcuts import render,redirect,reverse    # 从快捷方式导入重定向后者直接提供我都忍了，这个reverse的功能居然想等于模板中的url 就是将路由命名解析成路由地址
from django.contrib.auth.models import User     # 导入用户模型来查询数据
from django.contrib.auth import login,authenticate,logout  # 导入凭证的验证方法，以及登录,退出方法
from .form import *
from .models import *
from showware.models import Ware_info
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse   # 返回json作为ajax返回的结果

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

@login_required(login_url='/shopper/login.html')
def shopcartView(request):
    """处理加入购物车或者是展示购物车的逻辑。这个设计当然也可以实现，但是如果我们设置专门的订单商品信息表更合理一些，记录下当时的商品价格以及优惠情况，这个后面再说"""
    title="快乐购物车"
    classContent="shopcarts"
    # 获取请求参数
    wareid=request.GET.get('wareid','')
    warenum=request.GET.get("warenum",1)
    userID=request.user.id
    # 如果商品id不为空，则进行新增到购物车，否则就是直接展示即可
    if wareid:
        shopcart_info.objects.update_or_create(user_id=userID,nums=warenum,ware_id=wareid)
        return redirect("shopper:shopcart")
    # 如果添加的id为空，则展示购物车全部信息
    shopcartAll=shopcart_info.objects.filter(user_id=userID)        # 查询当前用户的购物车信息
    waredict={x.ware_id:x.nums for x in shopcartAll} # 从当前用户的购物车获取商品id和购买数量
    wareInfoList=Ware_info.objects.filter(id__in=waredict.keys())   # 从商品id获取商品详细信息
    return render(request,'shopcart.html',locals())

def shanchuView(request):
    result={'state':'sucess'}
    userId=request.GET.get('userId','')
    wareId=request.GET.get('wareId','')
    # 这里的规则感觉有问题，源码是如果用户id不为空则删除这个用户下的所有购物车明细，如果用户id为空，商品不为空，则删除具体商品，但是购物车的明细是商品id,用户id
    # 所以应该修改为userid不能为空，当wareid为空的情况下，则删除这个用户下所有商品记录，如果不为空，则删除具体用户具体商品
    if userId and wareId:
        # 删除具体商品
        shopcart_info.objects.filter(user_id=userId,ware_id=wareId).delete()
    elif userId:
        # 删除用户下所有购物车商品
        shopcart_info.objects.filter(user_id=userId).delete()
    else:
        result={'state':'failed'}
    return JsonResponse(result)

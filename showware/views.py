from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Ware_info,Ware_level

# Create your views here.
# 展示商品  商品详细

def showwareView(request):
    title='炫酷的商品列表'  # 网页标题
    classContent='commoditys'  # 选中内容的样式
    jb1_fl=Ware_level.objects.values('first').distinct()
    jb_all=Ware_level.objects.all()

    # 获取请求参数，分别是左侧分类，右侧的排序，右下的分页，最上的关键字  fl  px  fy kw
    fl=request.GET.get('fl','')   # 获取get请求的变量，如果第一个参数不存在，则替换为第二个变量作为默认值
    px=request.GET.get('px','sold')  # 如果不传入则以销量排序
    fy=request.GET.get('fy','1')  # 默认请求第一页的商品信息
    kw=request.GET.get('kw','')

    # 根据请求查询商品信息,每个组合逐个从商品信息中进行过滤
    wareList=Ware_info.objects.all()
    if fl:
        fl=Ware_level.objects.filter(id=fl).first()
        wareList=wareList.filter(level=fl.second)
    if px:
        wareList=wareList.order_by('-'+px)  # 这里设定的值是销量，价格，上架时间，以及收藏数，所以默认使用倒序
    if kw:
        wareList=wareList.filter(name__icontains=kw)
    # 分页功能
    fenyeqi=Paginator(wareList,6)  # 传入结果集和每页数据数
    try:
        pages=fenyeqi.page(fy)  # 默认查询传入的页码数据
    except PageNotAnInteger:   # 如果传入的页码不合法，返回第一页的
        pages=fenyeqi.page(1)
    except EmptyPage:  # 如果传入的页码不存在，则返回最后一页的数据
        pages=fenyeqi.page(fenyeqi.num_pages)
    return render(request,'warelist.html',locals())

# urls里的路由设置了wareid的变量，这里视图方法也必须设置相同名称和类型的wareid否则会提示typeError
def waredetailView(request,wareid):
    title="炫酷的商品明细介绍"
    classContent="datails"
    wareInfo=Ware_info.objects.filter(id=wareid).first()
    recommend=Ware_info.objects.exclude(id=wareid).order_by('-sold')[:5]
    likesList=request.session.get('likes',[])
    likes=True if wareid in likesList else False
    return render(request,"waredetail.html",locals())
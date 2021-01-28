# from django.shortcuts import render
# from django.core.handlers import wsgi
from showware.models import Ware_info, Ware_level
from django.views.generic.base import TemplateView

# Create your views here.
class indexClassView(TemplateView):
    # 通过查看TemplateView的源码和他继承的类，设置以下的方法和参数
    template_name="index.html"
    template_engine=None     # 不指定或者None即使用默认
    content_type=None
    extra_context={"title","首页","classContent":""}  # 网页标题，控制网页导航栏的样式，也就是当前被选中的那个标签页的样式给谁

    # 重新定义模板上下文的获取方法
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        # 然后我们对结果字典添加进去我们需要的内容
        context['allTop8']=Ware_info.objects.order_by('-sold').all()[:8]   # 按照销售数量倒序排列的前8条数据
        context['warelevel']=Ware_level.objects.all()     # 商品级别的所有数据，用于后面的数据筛选
        # 儿童服饰下销量前5
        lb_etfs=[x.second for x in Ware_level if x.first=='儿童服饰']
        context['etfsTop5']=Ware_info.objects.filter(level__in=lb_etfs).order_by('-sold')[:5]
        # 奶粉辅食销量前5
        lb_nffs=[x.second for x in Ware_level if x.first=='奶粉辅食']
        context['nffsTop5']=Ware_info.objects.filter(level__in=lb_nffs).order_by('-sold')[:5]
        # 婴儿用品销量前5
        lb_yeyp=[x.second for x in Ware_level if x.first=='婴儿用品']
        context['yeypTop5']=Ware_info.objects.filter(level__in=lb_yeyp).order_by('-sold')[:5]
        
        return context

    # 定义http的get请求处理方式,若路由设有路由变量可以从kwargs内获取到
    def get(self,request,*args,**kwargs):
        context=self.get_context_data(**kwargs)
        return self.render_to_response(context)

    # 定义post的请求处理方式，若路由设有路由变量可以从kwargs获取到
    def post(self,request,*args,**kwargs):
        context=self.get_context_data(**kwargs)
        return self.render_to_response(context)


"""
def indexView(request):
    titile = '一个炫酷的首页'      # 网页标题
    classcontent = ''             
    wareinfo = Ware_info.objects.order_by(
        '-sold').all()[:8]      # 按照销售数量倒序排列的前8条数据
    warelevel = Ware_level.objects.all()  # 商品级别的所有数据，用于后面的数据筛选
    # 儿童服饰下销量前5
    lb_etfs = [x.second for x in Ware_level if x.first == '儿童服饰']
    sp_etfs = Ware_info.objects.filter(level__in=lb_etfs).order_by('-sold')[:5]

    # 获取奶粉辅食下的销量前5
    lb_nffs = [x.second for x in Ware_level if x.first == '奶粉辅食']
    sp_nffs = Ware_info.objects.filter(Level_in=lb_nffs).order_by('-sold')[:5]

    # 获取婴儿用品下销量前5
    lb_yeyp = [x.second for x in Ware_level if x.first == '婴儿用品']
    sp_yeyp = Ware_info.objects.filter(level_in=lb_yeyp).order_by('-sold')[:5]

    # locals()以字典的形式返回当前位置所有的局部变量
    return render(request, 'index.html', locals())
"""
from django.db import models
# 商品类型模型和商品信息模型
# Create your models here.
class Ware_level(models.Model):
    id=models.AutoField(primary_key=True)
    first=models.CharField('类型级别1',max_length=100)
    second=models.CharField('类型级别2',max_length=100)

    # 调用字符串只给返回id
    def __str__(self):
        return str(self.id)

    # 表注释
    class Meta:
        verbose_name='商品类型'
        verbose_name_plural='商品类型'

class Ware_info(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField('商品名称',max_length=300)
    size=models.CharField('商品规格',max_length=100)
    level=models.CharField('商品类型级别',max_length=100)
    price=models.FloatField('商品价格')
    discount=models.FloatField('折后价格')
    stock=models.IntegerField('库存数量')
    sold=models.IntegerField('销售数量')
    likes=models.IntegerField('被收藏数量')
    created=models.DateField('上架日期',auto_now_add=True)
    img_main=models.FileField('主图路径',upload_to=r'img_main')  # 对应到各自的目录中
    img_detail=models.FileField('详情图路径',upload_to=r'img_detail')
    createtime=models.DateTimeField('创建时间',auto_now_add=True)
    updatetime=models.DateTimeField('修改时间',auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name='商品信息'
        verbose_name_plural='商品信息'
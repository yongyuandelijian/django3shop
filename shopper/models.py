from django.db import models
# 购物车模型和订单模型以及订单和商品信息关系表
# Create your models here.
# 定义常量用来选择订单状态时使用
STATE=(
    ('0','待支付'),
    ('1','待发货'),
    ('2','配送中'),
    ('3','已签收'),
    ('4','退货中'),
    ('5','已关闭'),
)

class shopcart_info(models.Model):
    id=models.AutoField(primary_key=True)
    nums=models.IntegerField('购买数量')
    ware_id=models.IntegerField('商品id')
    user_id=models.IntegerField('用户id')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name='购物车信息'
        verbose_name_plural='购物车信息'

class order_info(models.Model):
    id=models.AutoField(primary_key=True)
    total_price=models.FloatField('订单总价')
    user_id=models.IntegerField('用户id')
    createtime=models.DateTimeField('下单时间',auto_now_add=True)
    state=models.IntegerField('订单状态',choices=STATE)

    def __str__(self):
        return str(self.id)

    class Mate:
        verbose_name='订单信息'
        verbose_name_plural='订单信息'

class order_ware(models.Model):
    id=models.AutoField(primary_key=True)
    ware_id=models.IntegerField('商品id')
    order_id=models.IntegerField('订单id')
    cur_price=models.FloatField('成交价格')
    num=models.IntegerField('购买数量')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name='订单商品明细表'
        verbose_name_plural='订单商品明细表'

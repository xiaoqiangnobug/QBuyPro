from django.db import models
from goods.models import GoodsModel
# Create your models here.
class ActiveModel(models.Model):
    title = models.CharField(verbose_name='活动名称',
                            max_length=50)
    img1 = models.ImageField(verbose_name='活动图片',
                             upload_to='actives')

    start_time = models.CharField(max_length=20,
                                verbose_name='开始是时间')
    end_time = models.CharField(max_length=20,
                                verbose_name='结束时间')

    def __str__(self):
       return self.title

    class Meta:
        db_table = 'app_active'
        verbose_name_plural = verbose_name = '活动'

class ActiveGoodsModel(models.Model):
    active = models.ForeignKey(ActiveModel,
                               related_name='actives',
                               on_delete=models.SET_NULL,
                               null=True,
                               verbose_name='活动名')
    goods = models.ForeignKey(GoodsModel,
                              related_name='actives',
                              verbose_name='商品名',
                              null=True,
                              on_delete=models.SET_NULL)
    rate = models.FloatField(verbose_name='折扣价', default=0.88)


    def __str__(self):
        return self.active.title + ':' + self.goods.name

    class Meta:
        db_table = 'app_avtive_goods'
        verbose_name_plural = verbose_name = '活动信息'
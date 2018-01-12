from django.db import models
from tt_goods.models import GoodsInfo
# Create your models here.
class CartInfo(models.Model):
    user=models.ForeignKey('tt_user.UserInfo')
    goods=models.ForeignKey(GoodsInfo)
    count=models.IntegerField()
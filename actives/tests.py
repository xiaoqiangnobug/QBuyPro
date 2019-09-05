import time

from django.test import TestCase

# Create your tests here.

from celery import shared_task
from libs import cache


@shared_task
def qbuy_task(goods_id, user_id):
    time.sleep(10)
    # 判断是否已经抢完
    if cache.is_qbuyble():
        # 判断当前用户是否已经抢过
        if not cache.exist_qbuy(user_id):
            pass
        else:
            return '%s 抢 %s 只能一次' % (user_id, goods_id)

    return '%s 抢购 %s 失败' % (user_id, goods_id)

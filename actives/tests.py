import time

from django.test import TestCase

# Create your tests here.
import time
from celery import shared_task
from libs import cache


@shared_task
def qbuy_task(user_id, goods_id):
    time.sleep(10)
    # 判断是否已经抢完
    if cache.is_qbuyble():
        # 判断当前用户是否已经抢过
        if not cache.exist_qbuy(user_id):
            cache.add_qbuy(user_id, goods_id)
            return {'msg': '抢购成功', 'code': 200}
        else:
            return {'msg': '只抢购一次', 'code': 201}

    return { 'msg': '已经售罄!', 'code': 202}

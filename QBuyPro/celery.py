from __future__ import absolute_import
import os

from celery import Celery

# from QBuyPro import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'QBuyPro.settings')

# 配置Celery,加载settings.py
app = Celery('advanceDjango',
             broker='redis://xm.imzhangao.com:6379/11',
             backend='redis://xm.imzhangao.com:6379/12',
             namespace='Celery')
app.config_from_object('django.conf:settings')

# 自动发现task任务
app.autodiscover_tasks()
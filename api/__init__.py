from rest_framework import routers

from .user import UserAPIView
from .goods import GoodsAPIView
from .active import ActiveAPIview, ActiveGoodsAPIView

# 声明API路由
api_router = routers.DefaultRouter()

# 向api路由中注册ViewSet
api_router.register('user', UserAPIView)
api_router.register('goods', GoodsAPIView)
api_router.register('active', ActiveAPIview)
api_router.register('active_goods', ActiveGoodsAPIView)
# api_router.register('active_info', ActiveAPIview_info)

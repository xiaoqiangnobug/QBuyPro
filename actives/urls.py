from django.urls import path
from .views import ActiveGoodsView, qbuy_task

app_name = 'active'
urlpatterns = [
    path('info/', ActiveGoodsView.as_view(), name='info'),
   path('qbuy/', qbuy_task, name='active')
]
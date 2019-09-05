from django.urls import path
from .views import ActiveGoodsView, quby_active

app_name = 'active'
urlpatterns = [
    path('info/', ActiveGoodsView.as_view(), name='info'),
    path('qbuy/', quby_active, name='active')
]
from django.urls import path
from .views import user_api, user_api_detail
from .views import UserAPIView
app_name = 'user'

urlpatterns = [
    path('api', user_api, name='api'),
    path('api/<int:pk>', user_api_detail, name='make'),
    path('apione/', UserAPIView.as_view(), name='apione')
]
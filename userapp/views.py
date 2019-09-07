from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from userapp.models import UserModel
from api.user import UserModelSerializer


class UserAPIView(APIView):
    def get(self, request):
        datas = UserModel.objects.all()
        # instance参数默认是空，用来接收模型类
        # 第一参数数据默认的模型类，data是数据序列化后的数又保存方法数据是以json形式存在的。
        #
        serializer = UserModelSerializer(instance=datas, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = UserModelSerializer(data=request.data)
        print('请求的数据' ,request.data)
        print('串行化的数据' ,serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.instance)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def user_api(request):
    method = request.method
    if method == "GET":
        datas = UserModel.objects.all()
        serializer = UserModelSerializer(datas, many=True)
        return Response(serializer.data)
    else:
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.instance)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def user_api_detail(request, pk):
    method = request.method
    instance = UserModel.objects.get(pk=pk)
    if method =="GET":
        serializer = UserModelSerializer(instance)
        return Response(serializer.data)
    elif method == "PUT":
        pass
    elif method == 'DELETE':
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
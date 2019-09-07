from rest_framework import serializers, viewsets
from actives.models import ActiveModel, ActiveGoodsModel
from api.goods import GoodsSerializer


# class ActiveSerialalizer_info(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = ActiveModel
#         fields = ('title', 'start_time', 'end_time', 'img1')


class ActiveGoodsSerializer(serializers.HyperlinkedModelSerializer):
    goods = GoodsSerializer()
    # actives = ActiveSerialalizer_info()

    class Meta:
        model = ActiveGoodsModel
        fields = ('goods',  'rate', 'active')


class ActiveSerialalizer(serializers.HyperlinkedModelSerializer):

    actives = ActiveGoodsSerializer(many=True)
    class Meta:
        model = ActiveModel
        fields = ('title', 'start_time', 'end_time', 'img1', 'actives')



class ActiveAPIview(viewsets.ModelViewSet):
    queryset = ActiveModel.objects.all()
    serializer_class = ActiveSerialalizer


class ActiveGoodsAPIView(viewsets.ModelViewSet):
    queryset = ActiveGoodsModel.objects.all()
    serializer_class = ActiveGoodsSerializer


# class ActiveAPIview_info(viewsets.ModelViewSet):
#     queryset = ActiveModel.objects.all()
#     serializer_class = ActiveSerialalizer_info
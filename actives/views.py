from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from .tests import qbuy_task
from .models import ActiveModel


class ActiveGoodsView(TemplateView):
    template_name = 'goods_list.html'

    def get_context_data(self, **kwargs):
        context = super(ActiveGoodsView, self).get_context_data(**kwargs)

        active = ActiveModel.objects.get(pk=2)
        print(active.img1, '*'*30)
        context['active'] = active

        return context

def quby_active(request, goods_id):
    # 验证是否登陆
    login_user = request.session.get('login_user', None)
    if not login_user:
        return JsonResponse({
            'code': 100,
            'msg': '当前用户未登陆'
        })

    # login_user = {'id', 11, 'name', 'disen'}
    user_id = login_user.get('id')
    qbuy_task.delay(user_id, goods_id)



from django.shortcuts import render

# Create your views here.
'''
视图：所谓的视图，其实就是python函数
视图函数有2个要求：
1、视图函数的第一个参数就是接收请求，这个请求其实主是HttpRequest的类对象
2、必须返回一个响应

'''

from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    # return HttpResponse('OK')

    # render渲染模版
    # request, template_name, context=None

    # 模拟数据查询
    context={
        'name': '马上双11，点击有惊喜！'
    }
    return render(request, 'book/index.html', context=context)


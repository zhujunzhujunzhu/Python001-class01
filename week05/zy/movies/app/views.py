# from django.shortcuts import render

# # Create your views here.


# def index(request):
#     render(request, '你好世界')
from django.http import HttpResponse
from django.shortcuts import render
# from .models import
from .models import Movies


def index(request):
    # print(request)
    # return HttpResponse("Hello, world.")
    table_header = [
        {'label': '名称', 'prop': 'name'},
        {'label': '类型', 'prop': 'type'},
        # {'label': '上映时间', 'prop': 'time'},
        {'label': '短评', 'prop': 'short'},
        {'label': '评分', 'prop': 'grade'}
    ]
    # list = Movies.objects.all()
    # 处理星级大于3的 也就是 评分高于6的
    list = Movies.objects.filter(grade__gt=6)

    return render(request, 'index.html', {"table_header": table_header, "list": list})

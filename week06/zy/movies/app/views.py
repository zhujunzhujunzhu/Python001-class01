# from django.shortcuts import render

# # Create your views here.


# def index(request):
#     render(request, '你好世界')
from django.http import HttpResponse
from django.shortcuts import render
import math
# from .models import
from .models import Movies
from django.core.paginator import Paginator
table_header = [
    {'label': '名称', 'prop': 'name'},
    {'label': '类型', 'prop': 'type'},
    # {'label': '上映时间', 'prop': 'time'},
    {'label': '短评', 'prop': 'short'},
    {'label': '评分', 'prop': 'grade'}
]


def index(request):
    # print(request)
    # return HttpResponse("Hello, world.")

    # list = Movies.objects.all()
    # 处理星级大于3的 也就是 评分高于6的
    list = Movies.objects.filter(grade__gt=6)

    return render(request, 'index.html', {"table_header": table_header, "list": list})


def pager(request, pindex):
    movies = Movies.objects.all()  # 获取借书表中所有的数据
    pages = range(math.ceil(Movies.objects.count() / 5))
    pages = [i+1 for i in pages]
    paginator = Paginator(movies, 5)  # 实例化Paginator, 每页显示5条数据
    if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
        pindex = 1
    else:  # 如果有返回在值，把返回值转为整数型
        int(pindex)
    page = paginator.page(pindex)  # 传递当前页的实例对象到前端
    list = page.object_list
    return render(request, 'index.html', {"table_header": table_header, "list": list, "pages": pages})

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
    list = [
        {"id": 1, 'content': '这是一个列表1'},
        {"id": 2, 'content': '这是一个列表2'},
        {"id": 3, 'content': '这是一个列表3'},
        {"id": 4, 'content': '这是一个列表4'},
        {"id": 5, 'content': '这是一个列表5'},
    ]
    return render(request, 'index.html', {'msg': '你好我是一个测试', "list": list})


def test(request):
    list = [
        {"id": 1, 'content': '这是一个列表11'},
        {"id": 2, 'content': '这是一个列表22'},
        {"id": 3, 'content': '这是一个列表33'},
        {"id": 4, 'content': '这是一个列表44'},
        {"id": 5, 'content': '这是一个列表55'},
    ]
    movies = Movies()
    print(movies)

    # 关于基本的 增删改查
    return render(request, 'test.html', {"list": list})

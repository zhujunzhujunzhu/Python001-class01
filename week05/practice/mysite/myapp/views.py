# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello, world.你好世界.")
    context = {"msg": 'hello world'}
    return render(request, 'index.html', context)

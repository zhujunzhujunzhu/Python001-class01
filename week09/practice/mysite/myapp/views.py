
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User  # 导入django自带的user表
from django.contrib import auth


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        uname = request.POST.get("uname", "")
        pwd = request.POST.get("pwd", "")
        if uname and pwd:
            c = auth.authenticate(username=uname, password=pwd)
            if c:
                return HttpResponse('登录成功')
        return HttpResponse('登录失败')


from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth

from .forms import UserForm
# from django.contrib.auth import login as lg


def login(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'login.html', locals())
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            # 表单验证通过
            user_info = form.cleaned_data
            username = user_info['username']
            password = user_info['password']
            # 验证用户名密码
            c = auth.authenticate(username=username, password=password)
            if c:
                # 重定向到首页
                request.session['valid'] = True
                # 这里session默认两个星期  设置0浏览器关闭 None是代表永不
                request.session.set_expiry(0)
                return redirect('/myapp/dashborad')
                # return redirect(name='dashborad')
        else:
            pass
        form.clean()
        return render(request, 'login.html', locals())


def dashborad(request):
    if 'valid' in request.session:
        return render(request, 'dashboard.html', locals())
    else:
        return redirect('/myapp/login')

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

'''
这一块我现在再来熟悉下的  这个最为基本的东西是什么呢
首先需要从django.urls中将path导入的 name是什么的
在自己的app中 需要再
'''

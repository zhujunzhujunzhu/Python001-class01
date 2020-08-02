'''
@Description 
@Autor 朱俊
@Date 2020-08-02 00:17:53
LastEditors 朱俊
LastEditTime 2020-08-03 07:09:35
'''
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # 已借图书查询并展示
    path("<pindex>/", views.pager, name="pager"),
]

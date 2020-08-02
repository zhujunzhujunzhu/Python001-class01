'''
@Description 
@Autor 朱俊
@Date 2020-08-02 00:17:53
@LastEditors 朱俊
@LastEditTime 2020-08-02 22:50:22
'''
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]

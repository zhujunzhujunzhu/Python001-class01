'''
@Description 
@Autor 朱俊
@Date 2020-08-02 00:17:53
@LastEditors 朱俊
@LastEditTime 2020-08-02 10:31:38
'''
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test')
]

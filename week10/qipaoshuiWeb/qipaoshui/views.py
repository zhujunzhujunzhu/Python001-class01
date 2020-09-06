from django.shortcuts import render

# Create your views here.
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Qipaoshui, QipaoshuiComment, QipaoshuiSentiments


def index(request, *args, **kwargs):
    try:
        qps_list = list(Qipaoshui.objects.values())
        context = {
            'list': json.dumps(qps_list, ensure_ascii=False)
        }
        return render(request, 'index.html', context)
    except Exception as e:
        return HttpResponseNotFound("发生了错误")


def comments(request, *args, **kwargs):
    try:
        good_id = request.GET['good_id']
        comments = list(QipaoshuiComment.objects.filter(
            good_id=good_id).values())
        context = {
            'list': json.dumps(comments, ensure_ascii=False)
        }
        return render(request, 'comments.html', context)
    except Exception as e:
        return HttpResponseNotFound("发生了错误")

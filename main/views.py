from django.shortcuts import render
from django.http import HttpResponse


# a.リクエスト情報を受け取る
def index(request):
    # b.レスポンスを生成する
    return HttpResponse('こんにちは、世界！')
# 続きは2.2～

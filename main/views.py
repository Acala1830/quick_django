from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# a.リクエスト情報を受け取る
def index(request):
    # b.レスポンスを生成する
    return HttpResponse('こんにちは、世界！')

def temp(request):
    # a.ビュー変数を準備
    context = {
        'msg': 'こんにちは、世界！'
    }
    # b.テンプレートを呼び出す
    return render(request, 'main/temp.html', context)

def list(request):
    # すべての書籍情報を取得
    books = Book.objects.all()
    return render(request, 'main/list.html',{
        'books': books
    })
# 続きはpart3の最初から
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import random
import datetime
from datetime import datetime
from django.db.models import Q
from django.db.models import Count


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

def iftag(request):
  rand = random.randint(0, 100)
  return render(request, 'main/iftag.html', {
    'random': rand
  })
  
def yesno(request):
  return render(request, 'main/yesno.html', {
    'flag': True
  })

def firstof(request):
    return render(request, 'main/firstof.html', {
        # 'a': 'おはようございます！',
        # 'b': 'こんにちは！',
         'c': 'こんばんは！'
    })
    
def forloop(request):
    return render(request, 'main/forloop.html', {
        'weeks': ['月', '火', '水', '木', '金', '土', '日']
    })
    
def forempty(request):
    return render(request, 'main/forempty.html', {
        'members': ['鈴木三郎', '佐藤洋子', '山田次郎']
    })
    
def fortag(request):
    return render(request, 'main/fortag.html')

def ifchanged(request):
    return render(request, 'main/ifchanged.html', {
        'schedule': [
            (10, 'A企画反省会'),
            (10, 'B書籍脱稿'),
            (15, 'WINGS定例会議'),
            (30, 'C企画打ち合わせ'),
        ]
    })
    
def regroup(request):
    # a.メンバー情報を準備
    return render(request, 'main/regroup.html', {
        'members': [
            {'name': '鈴木三郎', 'sex': '男', 'birth': '1980-12-23' },
            {'name': '山田次郎', 'sex': '男', 'birth': '1978-10-13' },
            {'name': '佐藤健司', 'sex': '男', 'birth': '1976-04-06' },
            {'name': '山本花子', 'sex': '女', 'birth': '1981-07-28' },
            {'name': '田中久美', 'sex': '女', 'birth': '1980-09-07' },
        ]
    })

def cycle(request):
    # a.メンバー情報を準備
    return render(request, 'main/cycle.html', {
        'members': [
            {'name': '鈴木三郎', 'sex': '男', 'birth': '1980-12-23' },
            {'name': '山田次郎', 'sex': '男', 'birth': '1978-10-13' },
            {'name': '佐藤健司', 'sex': '男', 'birth': '1976-04-06' },
            {'name': '山本花子', 'sex': '女', 'birth': '1981-07-28' },
            {'name': '田中久美', 'sex': '女', 'birth': '1980-09-07' },
        ]
    })
    
def escape(request):
    return render(request, 'main/escape.html', {
        'msg': '''<img src="https://wings.msn.to/image/wings.jpg" title="ロゴ" />
        <p>WINGSへようこそ</p>'''
    })

def temptag(request):
    return render(request, 'main/temptag.html')

def verbatim(request):
    return render(request, 'main/verbatim.html')

def master(request):
    # a.呼び出すのは子テンプレート
    return render(request, 'main/master.html', {
        'msg': 'こんにちは世界！',
    })
    
def include(request):
    return render(request, 'main/include.html', {
        'name': '鈴木',
        'current': datetime.datetime.now(),
    })
    
def static(request):
    return render(request, 'main/static.html')

def slice(request):
    return render(request, 'main/slice.html', {
        'data': ['い', 'ろ', 'は', 'に', 'ほ', 'へ']
    })
    
def date_time(request):
    return render(request, 'main/date_time.html', {
        'today': datetime.now()
    })

def filter(request):
#   books = Book.objects.filter(publisher='翔泳社')

  # AND条件
#   books = Book.objects.filter(publisher='翔泳社', price=3300)

  # 大小比較
#   books = Book.objects.filter(price__lt = 3000)

  # 部分一致
#   books = Book.objects.filter(title__contains = '独習')

  # 正規表現比較
#   books = Book.objects.filter(title__regex = r'[0-9]+')

  # NULL比較
  # books = Book.objects.filter(title__isnull = True)

  # 範囲比較
  # books = Book.objects.filter(published__range = 
  #   (date(2018, 1, 1), date(2018, 12, 31)))

  # 候補比較
  books = Book.objects.filter(publisher__in = ['翔泳社', '技術評論社', '日経BP'])

  # 日付比較（年／月／日）
  # books = Book.objects.filter(published__year = 2019)
  # books = Book.objects.filter(published__year__lte = 2019)
  # books = Book.objects.filter(published__week_day__range = (2, 6))

  return render(request, 'main/book_list.html', {
    'books': books
  })

def exclude(request):
    # 出版社が翔泳社である書籍情報を除去
    books = Book.objects.exclude(publisher='翔泳社')
    return render(request, 'main/book_list.html', {
        "books": books
    })
    
def get(request):
    # 主キーが1である書籍情報を取得
    book = Book.objects.get(pk=1)
    return render(request, 'main/book_list.html', {
        "book": book
    })
    
def filter_or(request):
    books = Book.objects.filter(
        Q(publisher='翔泳社') | Q(price__gte=2800))
    return render(request, 'main/book_list.html', {
        "books": books
    })
    
def filter_other(request):
    books = Book.objects.order_by('publisher', 'published')
    return render(request, 'main/book_list.html', {
        "books": books
    })
    
def groupby(request):
    return render(request, 'main/groupby.html', {
        'groups': Book.objects.values('publisher')
        .annotate(pub_count=Count('publisher')).order_by('-pub_count')
    })
    
def union(request):
    b1 = Book.objects.filter(publisher = '翔泳社')
    b2 = Book.objects.filter(publisher = '技術評論社')
    return render(request, 'main/list.html', {
        "books": b1.union(b2)
    })
    
def rel(request):
    return render(request, 'main/rel.html', {
        'book': Book.objects.get(pk=1)
    })
    
def rel2(request):
    return render(request, 'main/rel2.html', {
        'books' : Book.objects.all()
    })
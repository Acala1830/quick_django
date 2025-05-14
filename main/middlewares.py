import datetime


# b.ミドルウェアを生成するファクトリー関数
def log_middleware(get_response):
    # a.ミドルウェア関数
    def middleware(request):
        # d.ビューの前に行うべき処理
        start = datetime.datetime.now()
        print(f'start: {request.path}: {start}')
        # c.ビューの呼び出し
        response = get_response(request)
        # e.ビューの後に行うべき処理（終了時刻/処理時間を表示）
        end = datetime.datetime.now()
        print(f'finish: {request.path}: {end}... {end - start}ms')
        return response
    return middleware
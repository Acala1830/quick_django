from django.db import models

# a.Modelクラスを継承
class Book(models.Model):
    # b.フィールド情報を定義
    isbn = models.CharField(
        verbose_name = 'ISBNコード',
        max_length = 20
    )
    title = models.CharField(
        verbose_name = '書名',
        max_length = 100
    )
    price = models.IntegerField(
        verbose_name = '価格',
        default = 0
    )
    publisher = models.CharField(
        verbose_name = '出版社',
        max_length = 50,
        choices = [
            ('翔泳社', '翔泳社'),
            ('技術評論社', '技術評論社'),
            ('終話システム', '終話システム'),
            ('SBクリエイティブ', 'SBクリエイティブ'),
            ('日経BP', '日経BP'),
        ],
    )
    published = models.DateField(
        verbose_name = '刊行日'
    )
    # c.モデルの文字列表現
    def __str__(self):
        return f'{self.title}({self.publisher}/{self.price}円)'

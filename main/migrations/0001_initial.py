# Generated by Django 5.1.3 on 2025-01-07 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBNコード')),
                ('title', models.CharField(max_length=100, verbose_name='書名')),
                ('price', models.IntegerField(default=0, verbose_name='価格')),
                ('publisher', models.CharField(choices=[('翔泳社', '翔泳社'), ('技術評論社', '技術評論社'), ('終話システム', '終話システム'), ('SBクリエイティブ', 'SBクリエイティブ'), ('日経BP', '日経BP')], max_length=50, verbose_name='出版社')),
                ('published', models.DateField(verbose_name='刊行日')),
            ],
        ),
    ]

from django.db import models

from accounts.models import CustomUser

from django.urls import reverse
# Create your models here.
class GameBlogPost(models.Model):
    CATEGORY = (('tips','小ネタ'),
                ('rule','ルール系'),
                ('other','その他'))
    
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )

    content = models.TextField(
        verbose_name='本文'
    )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    category = models.CharField(
        verbose_name='カテゴリ',
        max_length=50,
        choices=CATEGORY
    )

    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to='photos',
        blank=True,
        null=True
    )

    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to='photos',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
    

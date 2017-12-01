from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
import re


class Tieba(models.Model):
    name = models.CharField(max_length=200, verbose_name='贴吧名称')
    url = models.CharField(max_length=500, verbose_name='网址')
    men_mun = models.IntegerField(verbose_name='关注人数', default=0)
    topic_mun = models.IntegerField(verbose_name='贴子数', default=0)

    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=500, verbose_name='标题')
    author = models.CharField(max_length=50, verbose_name='发贴人')
    origin_content = models.TextField(verbose_name='页面原始HTML', null=True)
    origin_response = models.BinaryField(verbose_name='原始数据', null=True)
    content = models.TextField(verbose_name='页面内容')
    post_date = models.DateTimeField(
        null=True, blank=True, verbose_name='发布时间')
    url = models.CharField(
        max_length=500, verbose_name='网址', db_index=True, unique=True)
    tieba = models.ForeignKey(Tieba, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['url', ]),
        ]

    def __str__(self):
        return self.title

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
from tieba import models
from django.utils import timezone
from . import items


class DjangoPipeline(object):
    def process_item(self, item, spider):
        obj = models.Topic.objects.filter(url=item['url']).first()
        if not obj:
            obj = models.Topic()
            obj.title = item['title']
            obj.author = item['author']
            obj.origin_content = item['origin_content']
            obj.origin_response = item['origin_response']
            obj.content = item['content']
            obj.url = item['url']
            if 'post_data' in item:
                obj.post_date = item['post_date'].astimezone(
                    timezone.get_current_timezone())
            obj.tieba = self.get_tieba_by_name(item['tieba'])
            obj.save()

    def get_tieba_by_name(self, name):
        obj = models.Tieba.objects.filter(name=name).first()
        if not obj:
            obj = models.Tieba()
            obj.name = name
            obj.men_mun = 0
            obj.topic_mun = 0
            obj.save()
        return obj

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    origin_content = scrapy.Field()
    origin_response = scrapy.Field()
    content = scrapy.Field()
    post_date = scrapy.Field()
    url = scrapy.Field()
    tieba = scrapy.Field()

    def __str__(self):
        return '{0},{1}'.format(self['title'], self['url'])

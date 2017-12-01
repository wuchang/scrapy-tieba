# coding:utf-8

import logging
from scrapy.dupefilters import BaseDupeFilter
from tieba import models

logger = logging.getLogger('DjangoDupeFilter')


class DjangoDupeFilter(BaseDupeFilter):
    def __init__(self):
        self.urls_seen = set()
        logger.info("DjangoDupeFilter init!")

    @classmethod
    def from_settings(cls, settings):
        return cls()

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def request_seen(self, request):
        url = request.url
        if url in self.urls_seen:
            #logger.debug('  seened:%s',url)
            return True
        else:
            self.urls_seen.add(url)
            #logger.debug('seen add:%s',url)

        r = models.Topic.objects.filter(url=url).exists()
        return r

    def open(self):
        pass

    def close(self, reason):
        pass

    def clear(self):
        pass

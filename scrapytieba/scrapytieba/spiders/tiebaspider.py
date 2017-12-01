# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors import LinkExtractor
from utils.htmlstrip import strip_tags
from datetime import datetime
import time
import json

from ..items import TiebaItem


class TiebaSpider(CrawlSpider):
    name = "tieba"
    allowed_domains = ["tieba.baidu.com"]
#    start_urls = ['https://tieba.baidu.com/f?kw=%E5%A4%AA%E6%9E%81%E6%8B%B3&ie=utf-8']
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=太极拳']
    crawl_tieba = ['太极拳吧', '打坐吧', '气功吧', '形意拳吧', '辟谷吧']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('\/f\?kw=.*&ie=utf-8&pn=\d+', ),
                           deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=(r'/p/\d+$', )), callback='parse_item'),
    )

    # def __init__(self, name=[], *args, **kwargs):
    #     if name:
    #         self.wxtoscrapy = name.split(',')

    def start_requests(self):
        print('将要爬取的贴吧 %s' % self.crawl_tieba)
        for item in self.crawl_tieba:
            url = 'https://tieba.baidu.com/f?ie=utf-8&kw=' + item
            yield scrapy.Request(url, callback=self.parse)
#    def parse(self, response):
#        print( response.url )
#        print( response.css('a.j_th_tit').extract() )

    def parse_item(self, response):
        if response.css('title::text').extract_first() == '贴吧404':
            self.logger.info('贴吧404: {0}'.format(response.url))
            return
#        print('parse_item: %s' % response.url)
        item = TiebaItem()
        item['title'] = response.css('.core_title_txt::text').extract_first()
        item['author'] = response.css('.p_author_name::text').extract_first()
        item['url'] = response.url

        # postdata
        # d = response.css(
        #     '.tail-info::text').re('\d{4}\-\d{1,2}\-\d{1,2} \d{1,2}:\d{1,2}')
        # if d:  # eg https://tieba.baidu.com/p/1009838852
        #     item['post_date'] = datetime.strptime(d[0], "%Y-%m-%d %H:%M")
        # else:
        #     d = response.css(
        #         '.l_post_bright::attr(data-field)').extract_first()
        #     if d:  # eg: http://tieba.baidu.com/p/5442547255
        #         t = json.loads(d)['content']['date']
        #         item['post_date'] = datetime.strptime(t, '%Y-%m-%d %H:%M')


#        item['origin_content'] = response.body.decode()
        item['origin_content'] = ''
        item['origin_response'] = response.body
        item['content'] = strip_tags(
            ''.join(response.css('.d_post_content').extract()))

        item['tieba'] = response.css(
            '.card_title_fname::text').extract_first().strip()

        return item


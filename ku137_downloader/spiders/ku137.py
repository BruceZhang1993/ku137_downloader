# -*- coding: utf-8 -*-
import scrapy

from ku137_downloader.items import Ku137ResourceItem


class Ku137Spider(scrapy.Spider):
    name = 'ku137'
    allowed_domains = ['www.ku137.net', 'xz.ku137.net', 'ku137.net']
    start_urls = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skip = kwargs.get('skip', None)
        self.page = kwargs.get('page', None)
        self.cate_id = kwargs.get('category', 4)
        self.start_urls = ['https://www.ku137.net/b/{}/'.format(self.cate_id)]

    def parse(self, response):
        total_page = int(response.css('.pageinfo strong::text').extract_first())
        if self.page:
            total_page = int(self.page)
        for i in range(total_page):
            yield scrapy.Request(self.start_urls[0] + 'list_%d_%d.html' % (self.cate_id, i + 1), callback=self.parse_all)

    def parse_all(self, response):
        entries = response.css('.ml1 ul.cl li')
        for entry in entries:
            page = entry.css('a::attr(href)').extract_first()
            item_id = int(page.split('/')[-1].split('.')[0])
            if self.skip and item_id > int(self.skip):
                yield scrapy.Request(page, callback=self.parse_page)

    def parse_page(self, response):
        item = Ku137ResourceItem()
        item['category'] = response.css('.Title111 h1 a::text')[0].extract()
        item['name'] = response.css('title::text').extract_first()
        item['from_uri'] = response.request.url
        item['file_urls'] = [response.css('.Title111 h1 a::attr(href)')[1].extract()]
        yield item

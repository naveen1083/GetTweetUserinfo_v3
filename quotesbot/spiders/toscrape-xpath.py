# -*- coding: utf-8 -*-
import scrapy
import pkgutil
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

data = pkgutil.get_data("quotesbot", "resources/Userlist_links_.txt")

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    with open(data, encoding='utf-8') as f:
        start_urls = [url.strip() for url in f.readlines()]
    
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
                deny=('.*')
            ),
            callback='parse_item',
            follow=True
        )
    ]
    
    def parse(self, response):
        User = response.xpath("//div[@class='ProfileHeaderCard']")
        yield {
            'URL ':User.xpath('.//h1[@class="ProfileHeaderCard-name"]/a/@href').extract_first(),
            'Name': User.xpath('.//h1[@class="ProfileHeaderCard-name"]/a/text()').extract_first(),
            'Desc': User.xpath('.//p[@class="ProfileHeaderCard-bio u-dir"]/text()').extract_first(),

        }

#         next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
#         if next_page_url is not None:
#             yield scrapy.Request(response.urljoin(next_page_url))


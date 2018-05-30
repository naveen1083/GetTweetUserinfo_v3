# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'https://twitter.com/GeertReyniers',
    ]

    def parse(self, response):
        User = response.xpath("//div[@class='ProfileHeaderCard']")
        yield {
            'url':self.url
            'Name': User.xpath('.//h1[@class="ProfileHeaderCard-name"]/a/text()').extract_first(),
            'Desc': User.xpath('.//p[@class="ProfileHeaderCard-bio u-dir"]/text()').extract_first(),

        }

#         next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
#         if next_page_url is not None:
#             yield scrapy.Request(response.urljoin(next_page_url))


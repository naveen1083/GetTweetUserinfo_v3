# -*- coding: utf-8 -*-
import scrapy
import pkgutil
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor



class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    data = pkgutil.get_data("quotesbot", "resources/Userlist_links_.txt")
    start_urls = []
    with open(data, 'r', encoding='utf-8') as f:
         for line in f.readlines():
            link = line.split(',')[0]
            start_urls.append(link)

         
    
   
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


# -*- coding: utf-8 -*-
import scrapy
import pkgutil


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    
    def start_requests(self):
        data = pkgutil.get_data("quotesbot", "resources/Userlist_links_.txt")
        with open(data, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                link = line.split(',')[0]
                yield scrapy.Request(url=url, callback=self.parse)

         
    
   
    def parse(self, response):
        User = response.xpath("//div[@class='ProfileHeaderCard']")
        yield {
            'URL ':User.xpath('.//h1[@class="ProfileHeaderCard-name"]/a/@href').extract_first(),
            'Name': User.xpath('.//h1[@class="ProfileHeaderCard-name"]/a/text()').extract_first(),
            'Desc': User.xpath('.//p[@class="ProfileHeaderCard-bio u-dir"]/text()').extract_first(),

        }



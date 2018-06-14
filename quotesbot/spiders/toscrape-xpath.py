# -*- coding: utf-8 -*-
import scrapy
import pkgutil


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    data = pkgutil.get_data("quotesbot", "resources/Userlist_links_.txt")
    
    def start_requests(self):
        for link in data.decode('utf-8').split('\n'):
            yield scrapy.Request(url=link, callback=self.parse)
            
        
    
   
    def parse(self, response):
        User = response.xpath("//div[@class='ProfileHeaderCard']")
        yield {
            'URL ':User.xpath('.//h1[@class="ProfileHeaderCard-name"]/a/@href').extract_first(),
            'Name': User.xpath('.//h1[@class="ProfileHeaderCard-name"]/a/text()').extract_first(),
            'Desc': User.xpath('.//p[@class="ProfileHeaderCard-bio u-dir"]/text()').extract_first(),

        }



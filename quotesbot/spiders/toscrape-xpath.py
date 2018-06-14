# -*- coding: utf-8 -*-
import scrapy
import pkgutil


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'

    
    def start_requests(self):
        data = pkgutil.get_data("quotesbot", "resources/Userlist_links_.txt")
        for link in data.decode('utf-8').split('\n'):
            self.log(urls)
            yield scrapy.Request(url=link, callback=self.parse)
#     def start_requests(self):
#         urls = self.getUrls()
# #         self.log(urls)
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
    
#     def getUrls(self):
#         addurls = []
#         data = pkgutil.get_data("quotesbot", "resources/Userlist_links_.txt")
#         addurls = (data.decode('utf-8')).split('\n')
# #         self.log(len(addurls))
#         url = [x.strip() for x in addurls]
# #         self.log('Total urls:'+str(len(url)))
#         return url           
        
    
   
    def parse(self, response):
        User = response.xpath("//div[@class='ProfileHeaderCard']")
        yield {
            'URL ':User.xpath('.//h1[@class="ProfileHeaderCard-name"]/a/@href').extract_first(),
            'Name': User.xpath('.//h1[@class="ProfileHeaderCard-name"]/a/text()').extract_first(),
            'Desc': User.xpath('.//p[@class="ProfileHeaderCard-bio u-dir"]/text()').extract_first(),

        }



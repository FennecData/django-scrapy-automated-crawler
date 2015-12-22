# -*- coding: utf-8 -*-
import os
import re
import time
import scrapy
import logging
import simplejson

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import TakeFirst

class SimpleSpider(CrawlSpider):
    name = "simplespider"
    settings = {}
        
    def parse_page(self,response):
        item = SimpleItem()
        item['url'] = response.url
        item['result'] = self.Xpull(response.xpath(self.settings["xpath"]))
        
        item['result'] = re.compile(r''+self.settings["clean"]).sub('',item['result'])
            
        yield item
        
    def start_requests(self):
        f = open(self.scrapdir()+"/running/"+self.name+'.json', 'r')
        self.settings = simplejson.load(f)
        f.close()
        
        for c in self.settings["urls"].split("!!"):
            yield(scrapy.Request(c, self.parse_page))
        
    def closed(self,reason):
        try:
            os.remove(self.scrapdir()+"/running/"+self.name+'.json')
        except OSError:
            pass
        
    def Xpull(self,w00t):
        if len(w00t.extract()):
            return w00t.extract()[0]
        else:
            return ''
            
    def scrapdir(self):
        return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    
class SimpleItem(scrapy.Item):
    url = scrapy.Field()
    result = scrapy.Field()
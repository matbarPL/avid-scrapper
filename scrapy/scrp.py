# -*- coding: utf-8 -*-
import scrapy

class Link(scrapy.Item):
    currency = scrapy.Field()
    average_rate = scrapy.Field()
    market_value = scrapy.Field()
    volume = scrapy.Field()
    exchange = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'pages'
    allowed_domains = ['https://conotoxia.com']
    LIMIT_PAGES = 4
    start_urls = ['https://conotoxia.com/cryptocurrencies/cryptocurrency-rates/p/'+str(i) for i in range(1, LIMIT_PAGES+1)]
    print (start_urls)
    
    def parse(self, response):
        print(response)
        trs = response.xpath('/html/body/main/div/section[1]/div/div/table//tr')
        link = Link()
        for row in trs[1:]:
            currency = ''.join(row.xpath('td[1]//text()').extract()).replace("\n","")
            link['currency'] = ''.join([x for x in currency if ord(x) < 127]).replace("\n","")
            average_rate = ''.join(row.xpath('td[2]//text()').extract()).replace("\n","")
            link['average_rate'] = ''.join([x for x in average_rate if ord(x) < 127]).replace("\n","")
            market_value = ''.join(row.xpath('td[3]//text()').extract()).replace("\n","")
            link['market_value'] = ''.join([x for x in market_value if ord(x) < 127]).replace("\n","")
            volume = ''.join(row.xpath('td[4]//text()').extract()).replace("\n","")
            link['volume'] = ''.join([x for x in volume if ord(x) < 127]).replace("\n","")
            exchange = ''.join(row.xpath('td[5]//text()').extract()).replace("\n","")
            link['exchange'] = ''.join([x for x in exchange if ord(x) < 127]).replace("\n","")
            yield link

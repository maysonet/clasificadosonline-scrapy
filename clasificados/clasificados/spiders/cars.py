# -*- coding: utf-8 -*-
import scrapy

class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['clasificadosonline.com']
    start_urls = ['http://www.clasificadosonline.com/UDTransListingADV.asp?Marca=0&TipoC=0&RESPueblos=%25&FromYear=0&ToYear=2018&LowPrice=0&HighPrice=999999999&Submit2=Buscar+-+Go&Key=&AccessM=0']

    def parse(self, response):

        next_page = response.css('td.Ver10C>a::attr(href)')[2].extract()
        if next_page is not None:
            print('Processing... ', next_page)
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

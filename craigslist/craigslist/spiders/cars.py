# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://austin.craigslist.org/search/cta/']

    def parse(self, response):
        jobs = response.xpath('//p[@class="result-info"]')
        for job in jobs:
            title = job.xpath('a/text()').extract_first()
            price = job.xpath('span[@class="result-meta"]/span[@class="result-price"]/text()').extract_first("")
            relative_url = job.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
            #print (absolute_url)
            #yield{'URL':absolute_url, 'Title':title, 'Price':price}
            yield Request(absolute_url, callback=self.parse_page, meta={'URL':absolute_url, 'Title':title, 'Price':price})
        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)
        #yield Request(absolute_next_url, callback=self.parse)
        
    def parse_page(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        price = response.meta.get('Price')
        if price == "":
            return
        price = price[1:len(price)]
        description = "".join(line for line in response.xpath('//section[@id="postingbody"]/text()').extract())
        model = response.xpath('//p[@class="attrgroup"]/span/b/text()').extract_first("")
        if len(model.split()) != 3:
            return
        year = model.split()[0]
        make = model.split()[1]
        model = model.split()[2]
        condition = response.xpath('//p[@class="attrgroup"]/span[contains(text(),"condition")]/b/text()').extract_first("")
        cylinder = response.xpath('//p[@class="attrgroup"]/span[contains(text(),"cylinder")]/b/text()').extract_first("")
        if cylinder != "":
            cylinder = cylinder.split()[0]
        fuel = response.xpath('//p[@class="attrgroup"]/span[contains(text(),"fuel")]/b/text()').extract_first("")
        odometer = response.xpath('//p[@class="attrgroup"]/span[contains(text(),"odometer")]/b/text()').extract_first("")
        paint_color = response.xpath('//p[@class="attrgroup"]/span[contains(text(),"paint color")]/b/text()').extract_first("")
        size = response.xpath('//p[@class="attrgroup"]/span[contains(text(),"size")]/b/text()').extract_first("")
        title_status = response.xpath('//p[@class="attrgroup"]/span[contains(text(),"title status")]/b/text()').extract_first("")
        transmission = response.xpath('//p[@class="attrgroup"]/span[contains(text(),"transmission")]/b/text()').extract_first("")
        type = response.xpath('//p[@class="attrgroup"]/span[contains(text(),"type")]/b/text()').extract_first("")
        latitude = response.xpath('//*[@class="viewposting"]/@data-latitude').extract_first("")
        longitude = response.xpath('//*[@class="viewposting"]/@data-longitude').extract_first("")
        yield {
            'url':url,
            'title':title,
            'price':price,
            'year':year,
            'make':make,
            'model':model,
            'condition':condition,
            'cylinder':cylinder,
            'fuel':fuel,
            'odometer':odometer,
            'size':size,
            'title_status':title_status,
            'transimission':transmission,
            'type':type,
            'latitude':latitude,
            'longitude':longitude,
            'description':description,
        }
        
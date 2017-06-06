# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CraigslistItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    title = Field()
    price = Field()
    year = Field()
    make = Field()
    model = Field()
    condition = Field()
    cylinder = Field()
    fuel = Field()
    odometer = Field()
    size = Field()
    title_status = Field()
    transimission = Field()
    type = Field()
    latitude = Field()
    longitude = Field()
    description = Field()
    image = Field()
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import log
#from scrapy import DropItem
from scrapy.conf import settings

class CraigslistPipeline(object):
    def open_spider(self, spider):
        self.connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = self.connection[settings['MONGODB_DB']]
        self.collection = self.db[settings['MONGODB_COLLECTION']]
        
    def close_spider(self, spider):
        self.connection.close()
 
    def process_item(self, item, spider):
        #self.collection.insert(dict(item))
        self.collection.insert(dict((k,v) for k, v in item.items() if v))
        log.msg('Added to database!',level=log.DEBUG, spider=spider)
        return item

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WildberriesCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    brand_name = scrapy.Field()
    goods_name = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()

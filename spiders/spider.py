# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from wildberries_crawler.items import WildberriesCrawlerItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://www.wildberries.by/catalog/muzhchinam/odezhda/dzhinsy?sort=popular']

    def parse(self, response):
        root = Selector(response)

        goods_list = root.xpath('//*[contains(@class,"dtList i-dtList j-card-item")]')  # 	//*[contains(@class,'dtList i-dtList j-card-item')]
        for goods in goods_list:
            item = WildberriesCrawlerItem()
            item["brand_name"] = goods.xpath('.//strong[contains(@class,"brand-name")]/text()').extract()[0]
            item["goods_name"] = goods.xpath('.//span[contains(@class,"goods-name")]/text()').extract()[0]
            rating = goods.xpath('.//*[contains(@class,"dtList-comments-count")]/text()').extract()
            if not rating:
                item["rating"] = 0
            else:
                item["rating"] = int(rating[0])
            item["price"] = goods.xpath('.//*[contains(@class, "lower-price")]/text()').extract()[0]
            yield item

        next_page_url = response.css('div#body-layout > div.left-bg > div.trunkOld > div#catalog >' +
                                     'div#catalog-content > div.pager > div.pageToInsert > a.next::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

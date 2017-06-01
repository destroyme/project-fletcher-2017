# -*- coding: utf-8 -*-
import scrapy
import requests
import json


class HnapiSpider(scrapy.Spider):
    name = "hckr"

    def start_requests(self):
        url = 'http://hckrnews.com/data/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        a_tags = response.xpath('//a/@href')[1:-1].extract()
        for url in a_tags:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.save_data)

    def save_data(self, response):
        for data in json.loads(response.body):
            yield data

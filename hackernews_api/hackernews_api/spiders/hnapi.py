# -*- coding: utf-8 -*-
import scrapy
import requests
import json


class HnapiSpider(scrapy.Spider):
    name = "hnapi"
    allowed_domains = ["https://hacker-news.firebaseio.com/v0/"]
    base_url = 'https://hacker-news.firebaseio.com/v0/item/'
    url_maxitem = 'https://hacker-news.firebaseio.com/v0/maxitem.json'
    maxitem = requests.get(url_maxitem).json()

    def api_urls(self, start, end=maxitem+1):
        for item in range(start, end):
            yield self.base_url + str(item) + '.json'

    def start_requests(self):
        for url in self.api_urls(1,5):
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield json.loads(response.body)

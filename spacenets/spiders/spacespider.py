import scrapy


class SpacespiderSpider(scrapy.Spider):
    name = 'spacespider'
    allowed_domains = ['https://spacenet.tn/']
    start_urls = ['http://https://spacenet.tn//']

    def parse(self, response):
        pass

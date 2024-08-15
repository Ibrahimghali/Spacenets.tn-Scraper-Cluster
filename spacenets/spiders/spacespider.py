import scrapy


class SpacespiderSpider(scrapy.Spider):
    name = 'spacespider'
    allowed_domains = ['https://spacenet.tn/']
    start_urls = ['https://spacenet.tn/74-pc-portable-tunisie']

    def parse(self, response):
        pass

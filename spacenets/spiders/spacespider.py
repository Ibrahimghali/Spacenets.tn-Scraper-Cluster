import scrapy


class SpacespiderSpider(scrapy.Spider):
    name = 'spacespider'
    allowed_domains = ['https://spacenet.tn/']
    start_urls = ['https://spacenet.tn/74-pc-portable-tunisie']

    def parse(self, response):
        laptops = response.css('div.item.col-xs-6.col-sm-4.col-md-3.col-lg-3')
        for laptop in laptops:
            absolute_url = laptops.css('h2.product_name a::attr(href)').get()
            yield response.follow(absolute_url, callback=self.parse_laptop_page)
        
        next_page = response.css('li a.js-search-link::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    


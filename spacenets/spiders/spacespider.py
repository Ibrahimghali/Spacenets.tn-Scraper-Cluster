import scrapy


class SpacespiderSpider(scrapy.Spider):
    name = 'spacespider'
    allowed_domains = ['spacenet.tn']
    start_urls = ['https://spacenet.tn/74-pc-portable-tunisie']

    def parse(self, response):
        laptops = response.css('div.item.col-xs-6.col-sm-4.col-md-3.col-lg-3')
        for laptop in laptops:
            absolute_url = laptop.css('h2.product_name a::attr(href)').get()
            yield response.follow(absolute_url, callback=self.parse_laptop_page)
        
        next_page = response.css('li a.js-search-link::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_laptop_page(self, response):
        yield {
            'name': response.css('h1::text').get().strip(),
            'price': response.css('span.price::text').get().strip(),
            #'description': response.css('div.description-content p::text').getall(),
            #'availability': response.css('div.stock-status span::text').get().strip(),
        }

import scrapy
from scrapy_redis.spiders import RedisSpider
from spacenets.items import ProductFeaturesItem

class ItemSpider(RedisSpider):
    name = 'spacenets_spider'
    allowed_domains = ['spacenet.tn']
    
    # Replace start_urls with redis_key
    redis_key = 'spacenets:start_urls'
    
    # start_urls are now pushed to Redis separately
    
    def parse(self, response):
        """
        Parse the category page and extract product links.
        """
        items = response.css('div.item.col-xs-6.col-sm-4.col-md-3.col-lg-3')
        for item in items:
            url = item.css('h2.product_name a::attr(href)').get()
            if url:
                yield response.follow(url, callback=self.parse_item_page)
        
        yield from self.handle_pagination(response, self.parse)

    def handle_pagination(self, response, callback):
        """
        Handle pagination by following the 'next' page links.
        """
        hrefs = response.css('li a.js-search-link::attr(href)').getall()
        if hrefs:
            last_href = hrefs[-1]
            if last_href:
                yield response.follow(response.urljoin(last_href), callback=callback)

    def parse_item_page(self, response):
        """
        Parse the detailed product page.
        """
        item = ProductFeaturesItem()
        item['name'] = response.css('h1::text').get(default='N/A').strip()
        item['price'] = response.css('div.current-price span::attr(content)').get(default='N/A').strip()
        item['formatted_price'] = response.css('div.current-price span::text').get(default='N/A').strip()

        keys = response.css('section.product-features dl.data-sheet dt.name::text').getall()
        values = response.css('section.product-features dl.data-sheet dd.value::text').getall()
        product_features = {key.strip(): value.strip() for key, value in zip(keys, values)}

        item['features'] = product_features
        yield item

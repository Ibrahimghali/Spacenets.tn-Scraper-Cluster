import scrapy
#from spacenets.items import LaptopItem
from spacenets.items import ProductFeaturesItem


class ItemSpider(scrapy.Spider):
    name = 'spacenets_spider'
    allowed_domains = ['spacenet.tn']  # Domain names that the spider is allowed to scrape
    start_urls = ['https://spacenet.tn/18-ordinateur-portable']
    

    def parse(self, response):
        """
        General parsing method to extract items from a category page.
        This method can be reused by various spiders handling different categories.
        """
        items = response.css('div.item.col-xs-6.col-sm-4.col-md-3.col-lg-3')
        for item in items:
            url = item.css('h2.product_name a::attr(href)').get()

            if url is not None:
                # Determine the callback based on the URL or other page content    
                yield response.follow(url, callback=self.parse_item_page)
            
        # Handle pagination
        yield from self.handle_pagination(response, self.parse)

    def handle_pagination(self, response, callback):
        """
        Handle pagination across category pages.
        """
        print("Handling pagination...")
        hrefs = response.css('li a.js-search-link::attr(href)').getall()
        if hrefs:
            last_href = hrefs[-1]
            if last_href:
                yield response.follow(response.urljoin(last_href), callback=callback)


    def parse_item_page(self, response):

        """
        Method to parse detailed information from a laptop page.
        This method is specific to the LaptopSpider and handles fields relevant to laptops.
        """
        # Create an instance of the Item
        item = ProductFeaturesItem()

        # Extract and assign the additional fields
        item['name'] = response.css('h1::text').get()
        item['price'] = response.css('div.current-price span::attr(content)').get()
        item['formatted_price'] = response.css('div.current-price span::text').get()

        # Extract the keys (names of the features)
        keys = response.css('section.product-features dl.data-sheet dt.name::text').getall()

        # Extract the values (values of the features)
        values = response.css('section.product-features dl.data-sheet dd.value::text').getall()

        # Combine keys and values into a dictionary
        product_features = {key.strip(): value.strip() for key, value in zip(keys, values)}

        # Assign the dictionary to the 'features' field of the item
        item['features'] = product_features

        # Yield the item
        yield item
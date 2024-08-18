import scrapy
from spacenets.spiders.common_spider import CommonSpider
from spacenets.items import ProductFeaturesItem

class AirConditionerSpider(CommonSpider):
    name = 'climatisation_chauffage_spider'
    start_urls = ['https://spacenet.tn/317-climatisation-chauffage']


    def parse_climatisation_chauffage_page(self, response):
        # Create an instance of AirConditionerItem to store the scraped data
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
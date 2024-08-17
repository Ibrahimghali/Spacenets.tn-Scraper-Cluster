import scrapy
from spacenets.spiders.common_spider import CommonSpider
from spacenets.items import AirConditionerItem

class AirConditionerSpider(CommonSpider):
    name = 'air_conditioner_spider'
    start_urls = ['https://spacenet.tn/160-climatiseur-tunisie-chaud-froid']


    def parse_air_conditioner_page(self, response):
        # Create an instance of AirConditionerItem to store the scraped data
        item = AirConditionerItem()

        # Extract the product features section
        features_section = response.css('section.product-features')
        
        # Create a dictionary to store the features
        product_features = {}

        # Iterate over the feature names and their corresponding values
        for feature in features_section.css('dl.data-sheet'):
            # Extract the feature name and value
            feature_names = feature.css('dt.name::text').getall()
            feature_values = feature.css('dd.value::text').getall()

            # Combine them into a dictionary
            for name, value in zip(feature_names, feature_values):
                product_features[name] = value

        # Assign the extracted features to the item
        item['product_features'] = product_features

        # Yield the item to the pipeline for further processing
        yield item
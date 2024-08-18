import scrapy

class ProductFeaturesItem(scrapy.Item):
    # Fields for additional product details
    name = scrapy.Field()
    price = scrapy.Field()
    formatted_price = scrapy.Field()
    
    # Field for product features
    features = scrapy.Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SpacenetsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    formatted_price = scrapy.Field()
    description = scrapy.Field()
    availability = scrapy.Field()
    operating_system = scrapy.Field()
    memory = scrapy.Field()
    ports = scrapy.Field()
    wireless_connectivity = scrapy.Field()
    warranty = scrapy.Field()
    screen_size = scrapy.Field()
    processor_type = scrapy.Field()
    hard_drive = scrapy.Field()
    cache = scrapy.Field()
    graphics_card = scrapy.Field()
    processor_details = scrapy.Field()
    color = scrapy.Field()
    touchscreen = scrapy.Field()
    gamer = scrapy.Field()
    graphics_card_ref = scrapy.Field()
    pc_range = scrapy.Field()

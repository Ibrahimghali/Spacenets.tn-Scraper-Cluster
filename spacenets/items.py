import scrapy

class ProductItem(scrapy.Item):
    # Define fields common to both laptops and computers
    name = scrapy.Field()
    price = scrapy.Field()
    formatted_price = scrapy.Field()
    Garranty = scrapy.Field()
    
    

class LaptopItem(ProductItem):
    # Define fields specific to laptops
    operating_system = scrapy.Field()
    memory = scrapy.Field()
    ports = scrapy.Field()
    wireless_connectivity = scrapy.Field()

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



class AirConditionerItem(ProductItem):
    
    couleur = scrapy.Field()
    mode = scrapy.Field()
    capacite = scrapy.Field()
    inverter = scrapy.Field()
    type_climatiseur = scrapy.Field()
    smart = scrapy.Field()
    classe_temperatures = scrapy.Field()





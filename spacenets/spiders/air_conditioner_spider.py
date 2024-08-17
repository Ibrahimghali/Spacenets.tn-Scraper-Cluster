import scrapy
from spacenets.spiders.common_spider import CommonSpider
from spacenets.items import AirConditionerItem

class AirConditionerSpider(CommonSpider):
    name = 'air_conditioner_spider'
    start_urls = ['https://spacenet.tn/160-climatiseur-tunisie-chaud-froid']


    def parse_air_conditioner_page(self, response):

        """
        Method to parse detailed information from a air conditioner page.
        This method is specific to the air_conditioner_spider and handles fields relevant to air conditioners.
        """
        # Create an instance of AirConditionerItem to store the scraped data
        item = AirConditionerItem()

        # Extract and assign each feature to the corresponding item field
        item['name'] = response.css('h1::text').get()
        item['price'] = response.css('div.current-price span::attr(content)').get()
        item['formatted_price'] = response.css('div.current-price span::text').get()
        item['Garranty'] = response.css('dt.name:contains("Garantie") + dd.value::text').get()

        item['couleur'] = response.css('dt.name:contains("Couleur") + dd.value::text').get()
        item['mode'] = response.css('dt.name:contains("Mode") + dd.value::text').get()
        item['capacite'] = response.css('dt.name:contains("Capacité") + dd.value::text').get()
        item['inverter'] = response.css('dt.name:contains("Inverter") + dd.value::text').get()
        item['type_climatiseur'] = response.css('dt.name:contains("Type de climatiseur") + dd.value::text').get()
        item['smart'] = response.css('dt.name:contains("Smart") + dd.value::text').get()
        item['classe_temperatures'] = response.css('dt.name:contains("Classe de Températures") + dd.value::text').get()

        # Yield the item to the pipeline for further processing
        yield item
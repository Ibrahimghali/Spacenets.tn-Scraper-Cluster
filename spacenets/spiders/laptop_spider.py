from spacenets.items import LaptopItem
from spacenets.spiders.common_spider import CommonSpider

class LaptopSpider(CommonSpider):
    name = 'laptop_spider'
    start_urls = ['https://spacenet.tn/18-ordinateur-portable']

    def parse(self, response):
        laptops = response.css('div.item.col-xs-6.col-sm-4.col-md-3.col-lg-3')
        for laptop in laptops:
            url = laptop.css('h2.product_name a::attr(href)').get()
            if url:
                yield response.follow(url, callback=self.parse_laptop_page)
        self.handle_pagination(response, self.parse)

    def parse_laptop_page(self, response):
        # Create an instance of SpacenetsItem to store the scraped data
        item = LaptopItem()
        
        # Extract various attributes of the laptop from the page using CSS selectors and store them in the item
        item['name'] = response.css('h1::text').get()
        item['price'] = response.css('div.current-price span::attr(content)').get()
        item['formatted_price'] = response.css('div.current-price span::text').get()
        item['Garranty'] = response.css('dt.name:contains("Garantie") + dd.value::text').get()

        item['operating_system'] = response.css('dt.name:contains("Système d\'exploitation") + dd.value::text').get()
        item['memory'] = response.css('dt.name:contains("Mémoire") + dd.value::text').get()
        item['ports'] = response.css('dt.name:contains("Ports") + dd.value::text').get()
        item['wireless_connectivity'] = response.css('dt.name:contains("Connectivité sans-fil") + dd.value::text').get()
        
        item['screen_size'] = response.css('dt.name:contains("Taille de l\'écran") + dd.value::text').get()
        item['processor_type'] = response.css('dt.name:contains("Type de Processeur") + dd.value::text').get()
        item['hard_drive'] = response.css('dt.name:contains("Disque Dur") + dd.value::text').get()
        item['cache'] = response.css('dt.name:contains("Cache") + dd.value::text').get()

        item['graphics_card'] = response.css('dt.name:contains("Carte Graphique") + dd.value::text').get()
        item['processor_details'] = response.css('dt.name:contains("processeur") + dd.value::text').get()
        item['color'] = response.css('dt.name:contains("Couleur") + dd.value::text').get()
        item['touchscreen'] = response.css('dt.name:contains("Tactile") + dd.value::text').get()
        
        item['gamer'] = response.css('dt.name:contains("Gamer") + dd.value::text').get()
        item['graphics_card_ref'] = response.css('dt.name:contains("Réf Carte Graphique") + dd.value::text').get()
        item['pc_range'] = response.css('dt.name:contains("Gamme PC") + dd.value::text').get()

        # Yield the item to the pipeline for further processing
        yield item

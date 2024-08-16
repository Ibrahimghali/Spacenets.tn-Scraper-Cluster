import scrapy
from spacenets.items import SpacenetsItem  

class SpacespiderSpider(scrapy.Spider):
    name = 'spacespider'
    allowed_domains = ['spacenet.tn']
    start_urls = ['https://spacenet.tn/74-pc-portable-tunisie']

    def parse(self, response):
        # Extracts each laptop item from the page
        laptops = response.css('div.item.col-xs-6.col-sm-4.col-md-3.col-lg-3')
        for laptop in laptops:
            absolute_url = laptop.css('h2.product_name a::attr(href)').get()
            if absolute_url is not None:
                yield response.follow(response.urljoin(absolute_url), callback=self.parse_laptop_page)
        
        # Get all the href values
        hrefs = response.css('li a.js-search-link::attr(href)').getall()
        
        if hrefs:
            # Access the last element
            last_href = hrefs[-1]
            if last_href is not None:
                # Follows the link to the next page and calls parse again
                yield response.follow(response.urljoin(last_href), callback=self.parse)

    def parse_laptop_page(self, response):
        item = SpacenetsItem()
        
        item['name'] = response.css('h1::text').get()
        item['price'] = response.css('div.current-price span::attr(content)').get()
        item['formatted_price'] = response.css('div.current-price span::text').get()
        item['operating_system'] = response.css('dt.name:contains("Système d\'exploitation") + dd.value::text').get()
        item['memory'] = response.css('dt.name:contains("Mémoire") + dd.value::text').get()
        item['ports'] = response.css('dt.name:contains("Ports") + dd.value::text').get()
        item['wireless_connectivity'] = response.css('dt.name:contains("Connectivité sans-fil") + dd.value::text').get()
        item['warranty'] = response.css('dt.name:contains("Garantie") + dd.value::text').get()
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

        yield item

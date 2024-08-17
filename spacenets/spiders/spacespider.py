import scrapy
from spacenets.items import ComputerItem, LaptopItem # Import the item class defined in the items.py file to store the scraped data

class SpacespiderSpider(scrapy.Spider):
    name = 'spacespider'  # Name of the spider, used when running the spider
    allowed_domains = ['spacenet.tn']  # Domain names that the spider is allowed to scrape
    start_urls = [
        'https://spacenet.tn/18-ordinateur-portable',
        'https://spacenet.tn/73-ordinateur-bureau-tunisie'
    ]  # Starting URLs for the spider

    def parse(self, response):
        # Extract each item from the page using CSS selectors
        items = response.css('div.item.col-xs-6.col-sm-4.col-md-3.col-lg-3')
        for item in items:
            # Extract the URL of each item's detail page
            absolute_url = item.css('h2.product_name a::attr(href)').get()
            if absolute_url is not None:
                # Determine the callback based on the URL or other page content
                if 'ordinateur-portable' in response.url:
                    # It's a laptop
                    yield response.follow(response.urljoin(absolute_url), callback=self.parse_laptop_page)
                elif 'ordinateur-bureau' in response.url:
                    # It's a computer
                    yield response.follow(response.urljoin(absolute_url), callback=self.parse_computer_page)

        # Get all the href values for pagination links
        hrefs = response.css('li a.js-search-link::attr(href)').getall()
        
        if hrefs:
            # Access the last element of the pagination links
            last_href = hrefs[-1]
            if last_href is not None:
                # Follow the link to the next page and call the parse method again to continue scraping
                yield response.follow(response.urljoin(last_href), callback=self.parse)


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



    def parse_computer_page(self, response):
        item = ComputerItem()
        # Populate fields specific to computers
        item['name'] = response.css('h1::text').get()
        item['price'] = response.css('div.current-price span::attr(content)').get()
        item['formatted_price'] = response.css('div.current-price span::text').get()
        item['Garranty'] = response.css('dt.name:contains("Garantie") + dd.value::text').get()
        
        item['screen_size'] = response.css('dt.name:contains("Taille de l\'écran") + dd.value::text').get()
        item['brightness'] = response.css('dt.name:contains("Luminosité") + dd.value::text').get()
        item['contrast_ratio'] = response.css('dt.name:contains("Rapport de contraste") + dd.value::text').get()
        item['response_time'] = response.css('dt.name:contains("Temps de réponse") + dd.value::text').get()
        item['screen_format'] = response.css('dt.name:contains("Format") + dd.value::text').get()
        item['connectors'] = response.css('dt.name:contains("Connecteur") + dd.value::text').get()
        item['color'] = response.css('dt.name:contains("Couleur") + dd.value::text').get()
        item['panel_type'] = response.css('dt.name:contains("Type de panneau") + dd.value::text').get()
        item['touchscreen'] = response.css('dt.name:contains("Tactile") + dd.value::text').get()
        item['gamer'] = response.css('dt.name:contains("Gamer") + dd.value::text').get()
        item['refresh_rate'] = response.css('dt.name:contains("Taux de Rafraîchissement") + dd.value::text').get()

        # Yield the item to the pipeline for further processing
        yield item

    
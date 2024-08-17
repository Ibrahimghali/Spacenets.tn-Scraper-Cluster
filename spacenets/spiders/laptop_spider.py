import scrapy
from spacenets.items import LaptopItem
from spacenets.spiders.common_spider import CommonSpider

class LaptopSpider(CommonSpider):
    # Name of the spider, used to run the spider with Scrapy commands
    name = 'laptop_spider'

    # Starting URL for the spider to begin scraping
    start_urls = ['https://spacenet.tn/18-ordinateur-portable']

    def parse(self, response):
        """
        The main parsing method that Scrapy calls with the response from the start URL.
        This method extracts the links to individual laptop pages and yields them for further parsing.
        """
        # Select all laptop items on the page
        laptops = response.css('div.item.col-xs-6.col-sm-4.col-md-3.col-lg-3')
        
        # Iterate over each laptop item and extract the URL
        for laptop in laptops:
            url = laptop.css('h2.product_name a::attr(href)').get()
            if url:
                # Follow the laptop URL and call 'parse_laptop_page' to scrape details
                yield response.follow(url, callback=self.parse_laptop_page)
        
        # Handle pagination to move to the next page, if available
        yield from self.handle_pagination(response, self.parse)
    
    def parse_laptop_page(self, response):
        """
        Method to parse the details of an individual laptop.
        It extracts various attributes of the laptop and stores them in a LaptopItem.
        """
        # Create an instance of LaptopItem to store the scraped data
        item = LaptopItem()
        
        # Extract and store the laptop's name
        item['name'] = response.css('h1::text').get()
        
        # Extract and store the laptop's price and formatted price
        item['price'] = response.css('div.current-price span::attr(content)').get()
        item['formatted_price'] = response.css('div.current-price span::text').get()

        # Extract and store the laptop's warranty information
        item['Garranty'] = response.css('dt.name:contains("Garantie") + dd.value::text').get()

        # Extract and store various specifications of the laptop
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

        # Yield the item to the pipeline for further processing or storage
        yield item

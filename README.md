# Spacenets.tn-Scraper

Certainly! Here’s a combined version of your spacespider.py and README.md contents in one file for easy copying:

python
Copy code
import scrapy
from spacenets.items import SpacenetsItem  

class SpacespiderSpider(scrapy.Spider):
    name = 'spacespider'
    allowed_domains = ['spacenet.tn']
    start_urls = ['https://spacenet.tn/74-pc-portable-tunisie']

    def parse(self, response):
        laptops = response.css('div.item.col-xs-6.col-sm-4.col-md-3.col-lg-3')
        for laptop in laptops:
            absolute_url = laptop.css('h2.product_name a::attr(href)').get()
            yield response.follow(absolute_url, callback=self.parse_laptop_page)
        
        hrefs = response.css('li a.js-search-link::attr(href)').getall()
        last_href = hrefs[-1] if hrefs else None
        if last_href:
            yield response.follow(last_href, callback=self.parse)

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
markdown
Copy code
# Spacenets Scrapy Spider

## Overview

The Spacenets Scrapy Spider is a web scraper designed to extract laptop data from the Spacenets website. This spider collects details such as name, price, operating system, memory, ports, wireless connectivity, warranty, screen size, processor type, hard drive, cache, graphics card, processor details, color, touchscreen, gamer status, graphics card reference, and PC range.

## Features

- Scrapes laptop details from the Spacenets website.
- Handles pagination to scrape multiple pages.
- Follows links to individual laptop pages for detailed information.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/spacenets-spider.git
Navigate to the Project Directory:

bash
Copy code
cd spacenets-spider
Create and Activate a Virtual Environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Spider:

bash
Copy code
scrapy crawl spacespider
Save Output to a File:

To save the scraped data to a JSON file, use the following command:

bash
Copy code
scrapy crawl spacespider -o output.json
Project Structure
markdown
Copy code
spacenets-spider/
├── spacenets/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── spacespider.py
├── requirements.txt
└── README.md
spacenets/spiders/spacespider.py: Contains the main spider code.
spacenets/items.py: Defines the data structure for the scraped items.
requirements.txt: Lists the Python packages required for the project.
Configuration
Modify spacenets/settings.py to configure Scrapy settings such as user agents, download delays, and more.

Contributing
Feel free to open issues or submit pull requests if you find any bugs or want to add new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions, please contact your email.

csharp
Copy code

You can copy the contents of this file into your project’s Python and Markdown files as needed.
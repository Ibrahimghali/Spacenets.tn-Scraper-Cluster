import scrapy

class CommonSpider(scrapy.Spider):
    def parse(self, response):
        """
        General parsing method to extract items from a category page.
        This method can be reused by various spiders handling different categories.
        """
        items = response.css('div.item.col-xs-6.col-sm-4.col-md-3.col-lg-3')
        for item in items:
            url = item.css('h2.product_name a::attr(href)').get()
            if url:
                # Determine the callback based on the URL or other page content
                if 'ordinateur-portable' in response.url:
                    # It's a laptop
                    yield response.follow(url, callback=self.parse_laptop_page)
                elif 'climatiseur-tunisie-chaud-froid' in response.url:
                    # It's an air conditioner
                    yield response.follow(url, callback=self.parse_air_conditioner_page)
        
        # Handle pagination
        yield from self.handle_pagination(response, self.parse)

    def handle_pagination(self, response, callback):
        """
        Handle pagination across category pages.
        """
        print("Handling pagination...")
        hrefs = response.css('li a.js-search-link::attr(href)').getall()
        if hrefs:
            last_href = hrefs[-1]
            if last_href:
                yield response.follow(response.urljoin(last_href), callback=callback)

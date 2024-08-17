import scrapy

class CommonSpider(scrapy.Spider):
    # Other methods and properties

    def handle_pagination(self, response, callback):

        print("handling the pagination success")
        # Extract the pagination links
        hrefs = response.css('li a.js-search-link::attr(href)').getall()
        
        if hrefs:
            # Access the last element of the pagination links
            last_href = hrefs[-1]
            if last_href:
                # Follow the link to the next page
                yield response.follow(response.urljoin(last_href), callback=callback)

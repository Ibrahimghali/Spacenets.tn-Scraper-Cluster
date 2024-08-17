import scrapy

class CommonSpider(scrapy.Spider):
    def handle_pagination(self, response, callback):
        hrefs = response.css('li a.js-search-link::attr(href)').getall()
        if hrefs:
            last_href = hrefs[-1]
            if last_href:
                yield response.follow(response.urljoin(last_href), callback=callback)

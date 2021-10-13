import scrapy, re, csv

# I might change this dict for a class
selectors = {
    "products_links": None,
    "next_page": None,
    "precio": None,
    "expensas": None,
    "direccion": None,
    "fecha_publicacion": None,
    "ambientes": None,
    "baños": None,
    "antiguedad": None,
    "descripcion": None,
    "vendedor": None,
}

class deptosSpider(scrapy.Spider):
    name = 'deptos'
    download_delay = 1
    start_urls = []

    def parse(self, response):
        product_links = response.css(selectors["product_links"])
        for item in product_links:
            yield response.follow(item, self.parse_product)

        next_page = response.css(selectors["next_page"]).get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        else:
            print('No next page available')

    def parse_product(self, response):
        yield {
            "url": response.css(selectors["url"])
            "precio": response.css(selectors["precio"])
            "expensas": response.css(selectors["expensas"])
            "direccion": response.css(selectors["direccion"])
            "fecha_publicacion": response.css(selectors["fecha_publicacion"])
            "ambientes": response.css(selectors["ambientes"])
            "baños": response.css(selectors["baños"])
            "antiguedad": response.css(selectors["antiguedad"])
            "descripcion": response.css(selectors["descripcion"])
            "vendedor": response.css(selectors["vendedor"])
        }




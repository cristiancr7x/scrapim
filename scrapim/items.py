# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class URLItem(scrapy.Item):
    # Campo para almacenar la URL recolectada
    url = scrapy.Field()
    # Campo para almacenar el dominio de la URL
    domain = scrapy.Field()
    # Campo para almacenar la palabra clave que coincidió
    keyword = scrapy.Field()

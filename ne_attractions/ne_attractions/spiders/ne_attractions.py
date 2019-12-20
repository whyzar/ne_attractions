import scrapy

class NorthEastAttractionsSpider(scrapy.Spider):
    name = 'ne_attractions'
    attractions_url = 'https://www.jurnii.com/rv_guide/us_ne_reg_attractions.php'
    start_url = [attractions_url]

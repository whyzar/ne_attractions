import scrapy

class NorthEastAttractionsSpider(scrapy.Spider):
    name = 'ne_attractions'
    attractions_url = 'https://www.jurnii.com/rv_guide/us_ne_reg_attractions.php'
    start_url = [attractions_url]

    def parse(self,response):
        data = {}
        data['title'] = response.css('h4::text').extract()
        data['address'] = response.css('p.smaller_par::text').extract()
        yield data



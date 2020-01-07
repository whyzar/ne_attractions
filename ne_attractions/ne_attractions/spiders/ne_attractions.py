import scrapy

class NorthEastAttractionsSpider(scrapy.Spider):
    # scraper class for url
    name = 'ne_attractions'
    attractions_url = 'https://www.jurnii.com/rv_guide/us_ne_reg_attractions.php'
    start_urls = [attractions_url]

    def parse(self,response):
        # Extract titles/names and data cleanup
        data = {}
        data['title'] = response.css('h4::text').extract()
        data['address'] = response.css('p.smaller_par::text').extract()
        data[val.encode('ascii','ignore') for val in data]
        yield data



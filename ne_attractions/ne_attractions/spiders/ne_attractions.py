import scrapy

class NorthEastAttractionsSpider(scrapy.Spider):
    name = 'ne_attractions'
    attractions_url = 'https://www.jurnii.com/rv_guide/us_ne_reg_attractions.php'
    start_url = [attractions_url]

    def parse(self, response):
        # Extract names/titles of attractions
        h4tags = response.css("h4::text").extract()
        h4tags = filter(None, h4tags)

        # Extracted data
        for idx, bq in enumerate(response.css("blockquote")):
            data = bq.css("p.smaller_par::text").extract()
            data = filter(None, data)
        yield { "title": h4tags[idx] }



# from scrapy.spiders import Spider
import scrapy

class ScraperMe(scrapy.Spider):
    name = 'spiderman'
    start_urls = ['https://www.bayut.com/to-rent/property/dubai/']

    def parse(self, response):
        for property in response.css('div.d6e81fd0'):
            yield {
                'property_id':  property.css('div._7afabd84::text').get(),
                'price': property.css('span.f343d9ce::text').get(),
                'property_type':  property.css('div._9a4e3964::text').get()
                
                }
        next_page = response.css('a.b7880daf').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

            
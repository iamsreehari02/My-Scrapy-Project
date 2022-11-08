import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# https://www.bayut.com/to-rent/property/dubai/
# https://www.bayut.com/property/details-6365453.html


class MySpider(CrawlSpider):
    name = 'sip'
    allowed_domains = ['bayut.com']
    start_urls = ['https://www.bayut.com/to-rent/property/dubai/']

    rules = (
        Rule(LinkExtractor(allow='to-rent/property/dubai')),
        Rule(LinkExtractor(allow='property/details',deny='ar/property'), callback='parse_item')

    )

    def parse_item(self, response):
        
        yield {
            'Property_id' :response.css('span._812aa185::text')[2].get(),
            'Price': {
                'Currency' : response.css('span.e63a6bfb::text').get(),
                'Amount' : response.css('span._105b8a67::text').get()
            },
            'Location': response.css('div._1f0f1758::text').get(),
            'Purpose': response.css('span._812aa185::text')[1].get(),
            'Property_Type' : response.css('span._812aa185::text')[0].get()
        }
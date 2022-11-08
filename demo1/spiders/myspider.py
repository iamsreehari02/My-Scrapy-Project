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
            'Property_Type' : response.css('span._812aa185::text')[0].get(),
            'Bed_Bath' : 
                { 
                    'Bedroom' : response.css('span.fc2d1086::text')[0].get(),
                    'Bathroom' : response.css('span.fc2d1086::text')[1].get()

                },
            'Added_on' : response.css('span._812aa185::text')[4].get(),
            'Furnishing' : response.css('span._812aa185::text')[3].get(),
            'Description' : response.css('span._2a806e1e::text').get(),
            'Amenities' : response.css('span._005a682a::text')[0].get()+str(' & ')+response.css('span._005a682a::text')[1].get()+str(' & ')+response.css('span._005a682a::text')[2].get()+str(' & ')+response.css('span._005a682a::text')[3].get(),
            'Breadcrumbs' : response.css('span._327a3afc::text')[1].get()+str(' > ')+response.css('span._327a3afc::text')[2].get()+str(' > ')+response.css('span._327a3afc::text')[3].get(),
            'Image_link' : response.css('img.bea951ad').attrib['src']
          
            
        }
        
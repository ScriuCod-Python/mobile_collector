import scrapy


class AltexSpider(scrapy.Spider):
    name = 'mediagalaxy'
    allowed_domains = ['https://mediagalaxy.ro/telefoane/cpl/']
    start_urls = ['https://mediagalaxy.ro/telefoane/cpl/filtru/p/1/']

    custom_settings = {'FEED_URI': "mediagalaxy_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}

    def parse(self, response):
        #print("procesing:" + response.url)
        # Extract data using css selectors
        price_range = response.css('.Price-int::text').extract()
        name = response.css('.Product-name::text').extract()

        row_data = zip(price_range, name)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                #'page': response.url,
                # item[0] means product in the list and so on, index tells what value to assign
                'name': item[0],
                'price_range': item[1],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
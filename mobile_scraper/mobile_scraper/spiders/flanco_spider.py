import scrapy


class AltexSpider(scrapy.Spider):
    name = 'flanco'
    allowed_domains = ['https://www.flanco.ro/telefoane-tablete/smartphone.html']
    start_urls = ['https://www.flanco.ro/telefoane-tablete/smartphone/p/1.html']

    custom_settings = {'FEED_URI': "flanco_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}

    def parse(self, response):
        #print("procesing:" + response.url)
        # Extract data using css selectors
        price_range = response.css('.produs-price .price::text').extract()
        name = response.css('.product-new-link::text').extract()

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
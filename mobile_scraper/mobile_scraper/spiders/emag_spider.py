import scrapy


class EmagSpider(scrapy.Spider):
    name = 'emag'
    allowed_domains = ['https://www.emag.ro/telefoane-mobile/c?ref=hp_menu_quick-nav_1_16']
    start_urls = ['https://www.emag.ro/telefoane-mobile/c']

    custom_settings = {'FEED_URI': "emag_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}

    def parse(self, response):
        #print("procesing:" + response.url)
        # Extract data using css selectors
        price_range = response.css('.product-new-price::text').extract()
        name = response.css('.product-title::text').extract()

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
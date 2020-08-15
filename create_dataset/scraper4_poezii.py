# scrapy runspider scraper4_poezii.py

import scrapy

FILENAME = "poezii1.txt"
AUTHOR_NAME = "Mihai Eminescu"

class RomanianPoemsSpider(scrapy.Spider):
    name = 'brick_spider'
    # start_urls = ['http://brickset.com/sets/year-2016']
    start_urls = ['http://www.romanianvoice.com/poezii/poezii/amintirile.php', 'http://www.romanianvoice.com/poezii/poezii/criticilor.php']
    # start_urls = ['http://www.romanianvoice.com/poezii/poeti/eminescu.php']
    def __init__(self):
        global f_poezii
        f_poezii = open(FILENAME, "w+")

    # Called when class destroyed
    def __del__(self):
        global f_poezii
        f_poezii.close()

    def parse(self, response):
        # for link in start_urls:
        #     request = scrapy.Request(link)
        #     yield request
        print("-----------------------")
        print("Mihai Eminescu")
        print("-----------------------")
        

        # table = response.xpath('//*[@class="table"]')
        table = response.xpath('//table')

        # for td in table.xpath('.//td'):
        for tr in table.xpath('.//tr'):
            tr_extract = tr.extract()
            # print("tr:", tr_extract)
            if '<br><br>' in tr_extract:
                f_poezii.write(tr_extract + "\n-----------\n" + AUTHOR_NAME + "\n-----------\n-----------\n")

                print("td text:", tr_extract)
                # for td in tr.xpath('.//td'):
                    # print("text:", td.xpath())
            # address = s.xpath(".//tr/td[1]/text()").extract()

        print("Table:",table)
        # SET_SELECTOR = '.set'



        # # for row in response.xpath('//*[@class="table table-striped"]//tbody/tr'):
        # # for row in response.xpath('//table//tbody/tr'):
        # for row in response.xpath('//table//tbody/tr'):
        #     yield {
        #         # 'first' : row.xpath('td[1]//text()').extract_first(),
        #         'first' : row.xpath('td[1]').extract_first(),
        #         'last': row.xpath('td[2]//text()').extract_first(),
        #         'handle' : row.xpath('td[3]//text()').extract_first(),
        #     }


        print("-----------------------")

        # for brickset in response.css(SET_SELECTOR):

        #     SELECTOR1 = 'td'
        #     NAME_SELECTOR = 'td ::text'
        #     # PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
        #     # MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
        #     # IMAGE_SELECTOR = 'img ::attr(src)'
        #     yield {
        #         'poem': brickset.xpath(SELECTOR1).extract_first(),
        #         'name': brickset.css(NAME_SELECTOR).extract_first(),
        #         # 'name': brickset.css(NAME_SELECTOR).extract_first(),
        #         # 'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
        #         # 'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
        #         # 'image': brickset.css(IMAGE_SELECTOR).extract_first(),
        #     }

        # # NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        # NEXT_PAGE_SELECTOR = 'a ::attr(href)'
        # # NEXT_PAGE_SELECTOR = '.next td'
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # print("Next page:")
        # print(next_page)
        # if next_page:
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse
        #     )


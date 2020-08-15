# scrapy runspider scraper4_poezii.py

import scrapy

FILENAME = "poezii1.txt"
AUTHOR_NAME = "Mihai Eminescu"

class RomanianPoemsSpider(scrapy.Spider):
    name = 'brick_spider'
    # start_urls = ['http://brickset.com/sets/year-2016']
    # start_urls = ['http://www.romanianvoice.com/poezii/poezii/amintirile.php', 'http://www.romanianvoice.com/poezii/poezii/criticilor.php']
    start_urls = ['http://poezii.romanianvoice.com', 'http://poezii.romanianvoice.com/biblio/bib_eminescu.php', 'http://poezii.romanianvoice.com/poezii/adio.php', 'http://poezii.romanianvoice.com/poezii/afarai.php', 'http://poezii.romanianvoice.com/poezii/marmure.php', 'http://poezii.romanianvoice.com/poezii/frageda.php', 'http://poezii.romanianvoice.com/poezii/calin.php', 'http://poezii.romanianvoice.com/poezii/amintirile.php', 'http://poezii.romanianvoice.com/poezii/glasul.php', 'http://poezii.romanianvoice.com/poezii/amorul.php', 'http://poezii.romanianvoice.com/poezii/legeni.php', 'http://poezii.romanianvoice.com/poezii/doresc.php', 'http://poezii.romanianvoice.com/poezii/copiieram.php', 'http://poezii.romanianvoice.com/poezii/craiasa.php', 'http://poezii.romanianvoice.com/poezii/criticilor.php', 'http://poezii.romanianvoice.com/poezii/cumaine.php', 'http://poezii.romanianvoice.com/poezii/dionis.php', 'http://poezii.romanianvoice.com/poezii/decateori.php', 'http://poezii.romanianvoice.com/poezii/suflet.php', 'http://poezii.romanianvoice.com/poezii/decenuvii.php', 'http://poezii.romanianvoice.com/poezii/deasavea.php', 'http://poezii.romanianvoice.com/poezii/treceanii.php', 'http://poezii.romanianvoice.com/poezii/departe.php', 'http://poezii.romanianvoice.com/poezii/despartire.php', 'http://poezii.romanianvoice.com/poezii/diana.php', 'http://poezii.romanianvoice.com/poezii/dinnoaptea.php', 'http://poezii.romanianvoice.com/poezii/strainatate.php', 'http://poezii.romanianvoice.com/poezii/valurile.php', 'http://poezii.romanianvoice.com/poezii/doina_me.php', 'http://poezii.romanianvoice.com/poezii/dorinta.php', 'http://poezii.romanianvoice.com/poezii/egipetul.php', 'http://poezii.romanianvoice.com/poezii/epigonii.php', 'http://poezii.romanianvoice.com/poezii/fatfrumosdintei.php', 'http://poezii.romanianvoice.com/poezii/paduri.php', 'http://poezii.romanianvoice.com/poezii/floare.php', 'http://poezii.romanianvoice.com/poezii/foaia.php', 'http://poezii.romanianvoice.com/poezii/freamat.php', 'http://poezii.romanianvoice.com/poezii/glossa.php', 'http://poezii.romanianvoice.com/poezii/iarcand.php', 'http://poezii.romanianvoice.com/poezii/intaina.php', 'http://poezii.romanianvoice.com/poezii/imparat.php', 'http://poezii.romanianvoice.com/poezii/inger.php', 'http://poezii.romanianvoice.com/poezii/ingersidemon.php', 'http://poezii.romanianvoice.com/poezii/junii.php', 'http://poezii.romanianvoice.com/poezii/kamadeva.php', 'http://poezii.romanianvoice.com/poezii/labucovina.php', 'http://poezii.romanianvoice.com/poezii/lamijloc.php', 'http://poezii.romanianvoice.com/poezii/stirbey.php', 'http://poezii.romanianvoice.com/poezii/pumnul.php', 'http://poezii.romanianvoice.com/poezii/steaua.php', 'http://poezii.romanianvoice.com/poezii/lacul.php', 'http://poezii.romanianvoice.com/poezii/lasati.php', 'http://poezii.romanianvoice.com/poezii/luceafarul.php', 'http://poezii.romanianvoice.com/poezii/singurdor.php', 'http://poezii.romanianvoice.com/poezii/manusa.php', 'http://poezii.romanianvoice.com/poezii/melancolie_me.php', 'http://poezii.romanianvoice.com/poezii/misterele.php', 'http://poezii.romanianvoice.com/poezii/mortuaest.php', 'http://poezii.romanianvoice.com/poezii/intelegi.php', 'http://poezii.romanianvoice.com/poezii/noaptea.php', 'http://poezii.romanianvoice.com/poezii/mormant.php', 'http://poezii.romanianvoice.com/poezii/numai.php', 'http://poezii.romanianvoice.com/poezii/omama.php', 'http://poezii.romanianvoice.com/poezii/oramai.php', 'http://poezii.romanianvoice.com/poezii/odama.php', 'http://poezii.romanianvoice.com/poezii/pajulcup.php', 'http://poezii.romanianvoice.com/poezii/ulicioara.php', 'http://poezii.romanianvoice.com/poezii/plopii.php', 'http://poezii.romanianvoice.com/poezii/virfuri.php', 'http://poezii.romanianvoice.com/poezii/poet_me.php', 'http://poezii.romanianvoice.com/poezii/codrului.php', 'http://poezii.romanianvoice.com/poezii/teiului.php', 'http://poezii.romanianvoice.com/poezii/prinnopti.php', 'http://poezii.romanianvoice.com/poezii/revedere.php', 'http://poezii.romanianvoice.com/poezii/unuidac.php', 'http://poezii.romanianvoice.com/poezii/dusamorul.php', 'http://poezii.romanianvoice.com/poezii/sarapedeal.php', 'http://poezii.romanianvoice.com/poezii/scrisoarea1.php', 'http://poezii.romanianvoice.com/poezii/scrisoarea2.php', 'http://poezii.romanianvoice.com/poezii/scrisoarea3.php', 'http://poezii.romanianvoice.com/poezii/scrisoarea4.php', 'http://poezii.romanianvoice.com/poezii/scrisoarea5.php', 'http://poezii.romanianvoice.com/poezii/sebate.php', 'http://poezii.romanianvoice.com/poezii/sidaca.php', 'http://poezii.romanianvoice.com/poezii/decuziua.php', 'http://poezii.romanianvoice.com/poezii/singuratate.php', 'http://poezii.romanianvoice.com/poezii/somnoroase.php', 'http://poezii.romanianvoice.com/poezii/sonet1.php', 'http://poezii.romanianvoice.com/poezii/sonet2.php', 'http://poezii.romanianvoice.com/poezii/sonet3.php', 'http://poezii.romanianvoice.com/poezii/speranta.php', 'http://poezii.romanianvoice.com/poezii/teduci.php', 'http://poezii.romanianvoice.com/poezii/trecutau.php', 'http://poezii.romanianvoice.com/poezii/unluceafar.php', 'http://poezii.romanianvoice.com/poezii/venere.php', 'http://poezii.romanianvoice.com/poezii/venetia.php']

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


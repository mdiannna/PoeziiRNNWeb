# scrapy runspider scraper4_poezii.py

import scrapy

# FILENAME = "poezii1.txt"
# AUTHOR_NAME = "Mihai Eminescu"

class RomanianPoemsListSpider(scrapy.Spider):
    name = 'brick_spider'
    # start_urls = ['http://brickset.com/sets/year-2016']
    # start_urls = ['http://www.romanianvoice.com/poezii/poezii/amintirile.php', 'http://www.romanianvoice.com/poezii/poezii/criticilor.php']
    start_urls = ['http://www.romanianvoice.com/poezii/poeti/eminescu.php']
    # def __init__(self):
    #     global f_poezii
    #     f_poezii = open(FILENAME, "w+")

    # # Called when class destroyed
    # def __del__(self):
    #     global f_poezii
    #     f_poezii.close()

    def parse(self, response):
      
        table = response.xpath('//a/@href').getall()
        # table = response.xpath('//a').get_attribute('href')
        # table = response.xpath("*//a").get_attribute('href')
        # table = response.xpath("//a").extract_first()

        # # for td in table.xpath('.//td'):
        # for tr in table.xpath('.//tr'):
        #     tr_extract = tr.extract()
        #     # print("tr:", tr_extract)
        #     if '<br><br>' in tr_extract:
        #         f_poezii.write(tr_extract + "\n-----------\n" + AUTHOR_NAME + "\n-----------\n-----------\n")

        #         print("td text:", tr_extract)
        #         # for td in tr.xpath('.//td'):
        #             # print("text:", td.xpath())
        #     # address = s.xpath(".//tr/td[1]/text()").extract()


        # Links: ['http://poezii.romanianvoice.com', '../biblio/bib_eminescu.php', '../poezii/adio.php', '../poezii/afarai.php', '../poezii/marmure.php', '../poezii/frageda.php', '../poezii/calin.php', '../poezii/amintirile.php', '../poezii/glasul.php', '../poezii/amorul.php', '../poezii/legeni.php', '../poezii/doresc.php', '../poezii/copiieram.php', '../poezii/craiasa.php', '../poezii/criticilor.php', '../poezii/cumaine.php', '../poezii/dionis.php', '../poezii/decateori.php', '../poezii/suflet.php', '../poezii/decenuvii.php', '../poezii/deasavea.php', '../poezii/treceanii.php', '../poezii/departe.php', '../poezii/despartire.php', '../poezii/diana.php', '../poezii/dinnoaptea.php', '../poezii/strainatate.php', '../poezii/valurile.php', '../poezii/doina_me.php', '../poezii/dorinta.php', '../poezii/egipetul.php', '../poezii/epigonii.php', '../poezii/fatfrumosdintei.php', '../poezii/paduri.php', '../poezii/floare.php', '../poezii/foaia.php', '../poezii/freamat.php', '../poezii/glossa.php', '../poezii/iarcand.php', '../poezii/intaina.php', '../poezii/imparat.php', '../poezii/inger.php', '../poezii/ingersidemon.php', '../poezii/junii.php', '../poezii/kamadeva.php', '../poezii/labucovina.php', '../poezii/lamijloc.php', '../poezii/stirbey.php', '../poezii/pumnul.php', '../poezii/steaua.php', '../poezii/lacul.php', '../poezii/lasati.php', '../poezii/luceafarul.php', '../poezii/singurdor.php', '../poezii/manusa.php', '../poezii/melancolie_me.php', '../poezii/misterele.php', '../poezii/mortuaest.php', '../poezii/intelegi.php', '../poezii/noaptea.php', '../poezii/mormant.php', '../poezii/numai.php', '../poezii/omama.php', '../poezii/oramai.php', '../poezii/odama.php', '../poezii/pajulcup.php', '../poezii/ulicioara.php', '../poezii/plopii.php', '../poezii/virfuri.php', '../poezii/poet_me.php', '../poezii/codrului.php', '../poezii/teiului.php', '../poezii/prinnopti.php', '../poezii/revedere.php', '../poezii/unuidac.php', '../poezii/dusamorul.php', '../poezii/sarapedeal.php', '../poezii/scrisoarea1.php', '../poezii/scrisoarea2.php', '../poezii/scrisoarea3.php', '../poezii/scrisoarea4.php', '../poezii/scrisoarea5.php', '../poezii/sebate.php', '../poezii/sidaca.php', '../poezii/decuziua.php', '../poezii/singuratate.php', '../poezii/somnoroase.php', '../poezii/sonet1.php', '../poezii/sonet2.php', '../poezii/sonet3.php', '../poezii/speranta.php', '../poezii/teduci.php', '../poezii/trecutau.php', '../poezii/unluceafar.php', '../poezii/venere.php', '../poezii/venetia.php', '..']

        print("Table:",table)


        table = [item.replace('..', 'http://poezii.romanianvoice.com') for item in table[:-1]]

        print("--------------")
        print("Url links:")
        print(table)
        print("--------------")


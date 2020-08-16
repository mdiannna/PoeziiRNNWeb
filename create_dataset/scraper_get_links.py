# scrapy runspider scraper4_poezii.py

import scrapy

# FILENAME = "poezii1.txt"
# AUTHOR_NAME = "Mihai Eminescu"

class RomanianPoemsListSpider(scrapy.Spider):
    name = 'brick_spider'
    # start_urls = ['http://www.romanianvoice.com/poezii/poeti/eminescu.php']
    # start_urls = ['http://www.romanianvoice.com/poezii/poeti/alecsandri.php']
    # start_urls = ['http://www.romanianvoice.com/poezii/poeti/blandiana.php']
    start_urls = ['http://www.romanianvoice.com/poezii/poeti/blaga.php']
    
    def parse(self, response):
      
        links = response.xpath('//a/@href').getall()
    
        print("links:",links)


        links = [item.replace('..', 'http://poezii.romanianvoice.com') for item in links[:-1]]

        print("--------------")
        print("Url links:")
        print(links)
        print("--------------")


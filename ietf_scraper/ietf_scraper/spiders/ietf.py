from ast import parse
import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['https://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        #title = response.css('span.title::text').get()  #css
        #title = response.xpath('//span[@class="title"]/text()').get() #xpath
        return {
            "number": response.xpath('//span[@class="rfc-no"]/text()').get(),
            "title" : response.xpath('//span[@class="title"]/text()').get(), 
            "date": response.xpath('//span[@class="date"]/text()').get(),
            "author": response.xpath('//span[@class="author-name"]/text()').get(),
            "text": response.xpath('//div[@class="text"]/text()').getall(),
            "headings": response.xpath('//span[@class="subheading"]/text()').getall(),
            "address": response.xpath('//span[@class="address"]/text()').get(),
            "email": response.xpath('//span[@class="email"]/text()').get(),
            }
import scrapy

from listingscrapy.items import ListingscrapyItem


class ListSpiderSpider(scrapy.Spider):
    name = 'list_spider'
    allowed_domains = ['www.armadarealestate.com']
    start_urls1 = ['https://www.armadarealestate.com/inventory.aspx']
    #iframe src
    start_urls = ['https://buildout.com/plugins/3e0f3893dc334368bb1ee6274ad5fd7b546414e9/www.armadarealestate.com/inventory/?pluginId=0&iframe=true&embedded=true&cacheSearch=true&=undefined']

    def parse(self, response):
        lists = response.xpath('//div[@id="result-container"]').extract()
        yield lists

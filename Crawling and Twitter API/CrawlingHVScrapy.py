from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

# Manejo de expresiones XPATH
# Ejemplo Zyte: Artículos Blog

class ArticuloBlog(Item):
    titulo = Field()
    autor = Field()
    fecha = Field()

class Spider(CrawlSpider):
    name = "PrimerCrawler"
    start_urls = ["https://www.zyte.com/blog/"]
    allowed_domains = ['zyte.com']

    rules = (
        # crawling horizontal, crawling vertical
        Rule(LinkExtractor(allow=r'/page')),
        Rule(LinkExtractor(allow=r'/blog'), callback = 'parse_items')
    )
    def parse_items(self, response):
        item = ItemLoader(ArticuloBlog(),response)
        item.add_xpath('titulo','//*[@id="span-68-674"]/text()')
        item.add_xpath('autor','//*[@id="span-143-674"]/a/text()')
        item.add_xpath('fecha','//*[@id="span-124-674"]/text()')
        yield item.load_item()

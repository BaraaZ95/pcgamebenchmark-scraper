import scrapy


class GamesSpider(scrapy.Spider):
    name = 'games'
    #allowed_domains = ['www.pcgamebenchmark.com']
    start_urls = [f'https://www.pcgamebenchmark.com/best-pc-games/page-{i}?tags=&sort=0' for i in range(1, 6933)]

    def parse(self, response):
        urls =  response.css('div[class="games-list"]>div>div>a::attr(href)').getall()
        urls = ['https://www.pcgamebenchmark.com' + url for url in urls]
        for url in urls:
            yield scrapy.Request(url, callback= self.parse_page)
            
    def parse_page(self, response):
        
        
        specs = response.css('div[class="six columns"]> ul[class="bb_ul"]> li>strong::text').getall()
        text =  response.css('div[class="six columns"]> ul[class="bb_ul"]> li::text').getall()
        dict_ = dict(zip(specs, text))
        dict_['name'] = response.css('h1::text').get()
        yield dict_
        
        
        

import scrapy

class Extracturls(scrapy.Spider):
    name="khaleeda"
    def start_requests(self):
        urls=['https://www.example.com']
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parse)
    def parse(self, response):
        links=response.css('a::attr(href)').extract()
        for link in links:
            yield{'links': link}
       
        

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "glassdoor"

    start_urls = [
'https://www.glassdoor.com/Reviews/KfW-Reviews-E10659.htm'
    ]

    def parse(self, response):
        name_split = response.css('title::text').extract()[0].split(" ")[:-3]
        name = " ".join(name_split)
        for comment in response.css('.hreview'):
            yield {
                'name': name,
                'pros': comment.css('.pros::text').extract_first(),
                'cons': comment.css('.cons::text').extract_first(),
                'adviceMgmt': comment.css('.adviceMgmt::text').extract_first(),
                'time': comment.('.floatLt').xpath('./time/@datetime').extract(),
            }

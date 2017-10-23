import scrapy

class QuotesSpider(scrapy.Spider):
    name = "glassdoor"

    start_urls = [
'https://www.glassdoor.com/Reviews/Bank-Simpanan-Nasional-Reviews-E1252990.htm',
'https://www.glassdoor.com/Reviews/EXIM-Bank-of-Malaysia-Reviews-E692956.htm',
'https://www.glassdoor.com/Reviews/Bank-Pembangunan-Reviews-E42238.htm',
'https://www.glassdoor.com/Reviews/Agrobank-Reviews-E965869.htm',
'https://www.glassdoor.ca/Reviews/Small-Medium-Enterprise-Development-Bank-Reviews-E798175.htm'
    ]

    def parse(self, response):
        name_split = response.css('title::text').extract()[0].split(" ")[:-3]
        name = " ".join(name_split)
        for comment in response.css('.hreview'):
            yield {
                'Inst.': name,
                'Pros': comment.css('.pros::text').extract_first(),
                'Cons': comment.css('.cons::text').extract_first(),
                'Advice to Mgmt': comment.css('.adviceMgmt::text').extract_first(),
                'Time': comment.css('.floatLt').xpath('./time/@datetime').extract_first(),
            }

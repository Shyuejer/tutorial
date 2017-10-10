import scrapy

class QuotesSpider(scrapy.Spider):
    name = "glassdoor"

    start_urls = [
'https://www.glassdoor.ca/Reviews/Business-Development-Bank-of-Canada-Reviews-E221234_P2.htm',
'https://www.glassdoor.ca/Reviews/Business-Development-Bank-of-Canada-Reviews-E221234_P3.htm',
'https://www.glassdoor.ca/Reviews/Business-Development-Bank-of-Canada-Reviews-E221234_P4.htm',
'https://www.glassdoor.ca/Reviews/Business-Development-Bank-of-Canada-Reviews-E221234_P5.htm',
'https://www.glassdoor.ca/Reviews/Business-Development-Bank-of-Canada-Reviews-E221234_P6.htm',
'https://www.glassdoor.ca/Reviews/Business-Development-Bank-of-Canada-Reviews-E221234.htm',
'https://www.glassdoor.ca/Reviews/Bank-Negara-Reviews-E42236.htm',
'https://www.glassdoor.ca/Reviews/Bank-Negara-Reviews-E42236_P2.htm',
'https://www.glassdoor.ca/Reviews/Bank-Negara-Reviews-E42236_P3.htm',
'https://www.glassdoor.ca/Reviews/Bank-Negara-Reviews-E42236_P4.htm',
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
                'time': comment.css('.floatLt').xpath('./time/@datetime').extract_first(),
            }

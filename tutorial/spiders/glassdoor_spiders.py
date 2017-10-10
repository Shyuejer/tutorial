import scrapy

class QuotesSpider(scrapy.Spider):
    name = "glassdoor"

    start_urls = [
'https://www.glassdoor.ca/Reviews/Business-Development-Bank-of-Canada-Reviews-E221234.htm'
    ]

    def parse(self, response):
        name_split = response.css('title::text').extract()[0].split(" ")[:-3]
        name = " ".join(name_split)
        for comment in response.css('.hreview'):
            yield {
                'name': name,
                'pros': comment.css('div.padTopMd::text').extract_first(),
                'date': comment.css('span.comdt::text').extract_first().split(" ")[0],
                'time': comment.css('span.comdt::text').extract_first().split(" ")[1],
                'comment': comment.css('span.autolink::text').extract_first(),
            }

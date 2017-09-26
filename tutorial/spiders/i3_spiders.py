import scrapy

class QuotesSpider(scrapy.Spider):
    name = "i3"

    start_urls = [
        'https://klse.i3investor.com/servlets/stk/0186.jsp',
        'https://klse.i3investor.com/servlets/stk/0176.jsp',
    ]

    def parse(self, response):
        name = response.css('title::text').extract()[0].split(" ")[0]
        for comment in response.css('div.comtb')[2:-1]:
            yield {
                'name': name,
                'username': comment.css('span.comuid::text').extract_first(),
                'datetime': comment.css('span.comdt::text').extract_first(),
                'comment': comment.css('span.autolink::text').extract_first(),
            }

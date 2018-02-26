import scrapy

class QuotesSpider(scrapy.Spider):
    name = "i3"

    start_urls = [
'https://klse.i3investor.com/servlets/stk/5277.jsp',
'https://klse.i3investor.com/servlets/stk/0185.jsp',
'https://klse.i3investor.com/servlets/stk/0146.jsp',
'https://klse.i3investor.com/servlets/stk/5171.jsp',
'https://klse.i3investor.com/servlets/stk/0176.jsp',
'https://klse.i3investor.com/servlets/stk/0126.jsp',
'https://klse.i3investor.com/servlets/stk/0113.jsp',
'https://klse.i3investor.com/servlets/stk/0108.jsp',
'https://klse.i3investor.com/servlets/stk/0186.jsp',
'https://klse.i3investor.com/servlets/stk/7200.jsp',
'https://klse.i3investor.com/servlets/stk/0106.jsp',
'https://klse.i3investor.com/servlets/stk/5243.jsp',
'https://klse.i3investor.com/servlets/stk/0080.jsp',
'https://klse.i3investor.com/servlets/stk/5218.jsp',
'https://klse.i3investor.com/servlets/stk/7089.jsp',
'https://klse.i3investor.com/servlets/stk/5263.jsp',
'https://klse.i3investor.com/servlets/stk/5160.jsp',
'https://klse.i3investor.com/servlets/stk/5001.jsp',
'https://klse.i3investor.com/servlets/stk/5398.jsp',
'https://klse.i3investor.com/servlets/stk/5031.jsp',
'https://klse.i3investor.com/servlets/stk/3336.jsp',
'https://klse.i3investor.com/servlets/stk/1651.jsp',
'https://klse.i3investor.com/servlets/stk/5014.jsp',
    ]

    def parse(self, response):
        name = response.css('title::text').extract()[0].split(" ")[0]
        for comment in response.css('div.comtb')[2:-1]:
            yield {
                'name': name,
                'username': comment.css('span.comuid::text').extract_first(),
                'date': comment.css('span.comdt::text').extract_first().split(" ")[0],
                'time': comment.css('span.comdt::text').extract_first().split(" ")[1],
                'comment': comment.css('span.autolink::text').extract_first(),
            }

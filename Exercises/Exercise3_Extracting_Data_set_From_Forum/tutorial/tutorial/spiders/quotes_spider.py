import scrapy

# name: identifies the Spider. It must be unique within a project, 
# that is, you can’t set the same name for different Spiders.
 
# start_requests(): must return an iterable of Requests 
# (you can return a list of requests or write a generator function) which the 
# Spider will begin to crawl from. Subsequent requests will be generated successively 
# from these initial requests.

# parse(): a method that will be called to handle the response downloaded for each 
# of the requests made. The response parameter is an instance of TextResponse that 
# holds the page content and has further helpful methods to handle it.

# The parse() method usually parses the response, extracting the scraped data as dicts 
# and also finding new URLs to follow and creating new requests (Request) from them.
# V1
#class QuotesSpider(scrapy.Spider):
#    name = "quotes"

#    def start_requests(self):
#        urls = [
#            'http://quotes.toscrape.com/page/1/',
#            'http://quotes.toscrape.com/page/2/',
#        ]
#        for url in urls:
#            yield scrapy.Request(url=url, callback=self.parse)

#    def parse(self, response):
#        page = response.url.split("/")[-2]
#        filename = 'quotes-%s.html' % page
#        with open(filename, 'wb') as f:
#            f.write(response.body)
#        self.log('Saved file %s' % filename)

# V2
#class QuotesSpider(scrapy.Spider):
#    name = "quotes"
#    start_urls = [
#        'http://quotes.toscrape.com/page/1/',
#        'http://quotes.toscrape.com/page/2/',
#    ]
#
#    def parse(self, response):
#        page = response.url.split("/")[-2]
#        filename = 'quotes-%s.html' % page
#        with open(filename, 'wb') as f:
#            f.write(response.body)

# V3
#class QuotesSpider(scrapy.Spider):
#    name = "quotes"
#    start_urls = [
#        'http://quotes.toscrape.com/page/1/',
#        'http://quotes.toscrape.com/page/2/',
#    ]
#
#    def parse(self, response):
#        for quote in response.css('div.quote'):
#            yield {
#                'text': quote.css('span.text::text').get(),
#                'author': quote.css('small.author::text').get(),
#                'tags': quote.css('div.tags a.tag::text').getall(),
#            }   

# V4
#class QuotesSpider(scrapy.Spider):
#    name = "quotes"
#    start_urls = [
#        'http://quotes.toscrape.com/page/1/',
#    ]
#
#    def parse(self, response):
#        for quote in response.css('div.quote'):
#            yield {
#                'text': quote.css('span.text::text').get(),
#                'author': quote.css('small.author::text').get(),
#                'tags': quote.css('div.tags a.tag::text').getall(),
#            }
#
#        next_page = response.css('li.next a::attr(href)').get()
#        if next_page is not None:
#            next_page = response.urljoin(next_page)
#            yield scrapy.Request(next_page, callback=self.parse)

# V5
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)



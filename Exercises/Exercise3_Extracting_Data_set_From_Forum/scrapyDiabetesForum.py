import scrapy

#class AuthorSpider(scrapy.Spider):
#    name = 'author'
#
#    start_urls = ['http://quotes.toscrape.com/']
#
#    def parse(self, response):
#        # follow links to author pages
#        for href in response.css('.author + a::attr(href)'):
#            yield response.follow(href, self.parse_author)
#
#        # follow pagination links
#        for href in response.css('li.next a::attr(href)'):
#            yield response.follow(href, self.parse)
#
#    def parse_author(self, response):
#        def extract_with_css(query):
#            return response.css(query).get(default='').strip()
#
#        yield {
#            'name': extract_with_css('h3.author-title::text'),
#            'birthdate': extract_with_css('.author-born-date::text'),
#            'bio': extract_with_css('.author-description::text'),
#        }

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
            print("aaa")





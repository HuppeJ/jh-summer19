# Scraped the subforum "Ask-a-question" for first sample for testing
import scrapy
from bs4 import BeautifulSoup
    
# scrapy crawl questions
# scrapy crawl questions -o questions.json
# scrapy crawl questions -o questions.jl

class QuestionsSpider(scrapy.Spider):
    name = "questions"
    start_urls = [
        # 1 - 10
        "https://www.diabetes.co.uk/forum/category/ask-a-question.15/?order=view_count",
        # 11 - 20
        # "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-11?order=view_count",
        # 21 - 30
        # "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-21?order=view_count",
        # 31 - 40
        # "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-31?order=view_count",
        # 41 - 50
        # "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-41?order=view_count",
    ]

    # Max nb. of page to scrape
    COUNT_MAX = 50
    count = 0

    def parse(self, response):
        for question in response.css(".discussionListItems li[id]"):
            info = {
                "thread_id": question.css('::attr(id)').extract_first(),
                "thread_title": question.css(".title .PreviewTooltip::text").get(), 
                "thread_author": question.css(".secondRow .username::text").get(),
                "thread_startDate": question.css(".secondRow .startDate .DateTime::text").get(),
                "thread_replies": question.css(".stats .major dd::text").get(),
                "thread_views": question.css(".stats .minor dd::text").get(),
            }

            # Follow link to question page
            href = question.css("h3.title a::attr(href)")[-1].get()
            question_page = response.urljoin(href)
            request = scrapy.Request(question_page, self.parse_question)
            request.meta['item'] = info

            yield request

        # Follow pagination links
        # Gets the last link (Next page link)
        if (self.count < self.COUNT_MAX):
            self.count = self.count + 1
            href = response.css(".PageNav a::attr(href)")[-1].get()
            yield response.follow(href, self.parse)

    def parse_question(self, response):
        item = response.meta['item']
        all_paragraphs = response.css(".messageList .uix_threadAuthor .messageContent .messageText *::text").getall()
        map(str.strip, all_paragraphs)
        seperator = " "
        text = seperator.join(all_paragraphs)
        clean_text = BeautifulSoup(text, "lxml").text
        new_string = (clean_text.encode('ascii', 'ignore')).decode("utf-8")
        new_string  = " ".join(new_string.split())
        item["question"] = new_string
        yield item




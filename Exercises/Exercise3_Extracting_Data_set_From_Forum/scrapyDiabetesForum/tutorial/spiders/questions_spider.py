import scrapy
# import html2text
    
# scrapy crawl questions
# scrapy crawl questions -o questions.json

class QuestionsSpider(scrapy.Spider):
    name = "questions"
    start_urls = [
    #    "https://www.diabetes.co.uk/forum/category/ask-a-question.15/?order=view_count",
        "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-2?order=view_count",
  #      "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-3?order=view_count",
  #      "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-4?order=view_count",
  #      "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-5?order=view_count",
  #      "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-6?order=view_count",
  #      "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-7?order=view_count",
 #       "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-8?order=view_count",
 #       "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-9?order=view_count",
  #      "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-10?order=view_count",
  #      "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-11?order=view_count",
 #       "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-12?order=view_count",
#        "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-13?order=view_count",
#        "https://www.diabetes.co.uk/forum/category/ask-a-question.15/page-14?order=view_count",
    ]

    def parse(self, response):
        for question in response.css(".discussionListItems li[id]"):
            href = response.css("h3.title a::attr(href)")[0].get()
            yield response.follow(href, self.parse_question)

            scraped_info = {
                "thread_id": question.css('::attr(id)').extract_first(),
                "title": question.css(".title .PreviewTooltip::text").get(), 
                "author": question.css(".secondRow .username::text").get(),
                "startDate": question.css(".secondRow .startDate .DateTime::text").get(),
                "replies": question.css(".stats .major dd::text").get(),
                "views": question.css(".stats .minor dd::text").get(),
            }

            yield scraped_info 

        # Follow links to author pages
        print("TEST")
        print(response.css("h3.title a::attr(href)").getall())
        #for href in response.css(".discussionListItem h3.title a::attr(href)"):
        #    yield response.follow(href, self.parse_question)
        href = response.css("h3.title a::attr(href)")[0].get()
        yield response.follow(href, self.parse_question)

        # follow pagination links
        # Gets the last link (Next page link)
        # href = response.css(".PageNav a::attr(href)")[-1].get()
        # yield response.follow(href, self.parse)

    def parse_question(self, response):
        yield {
            "question": response.css(".messageList .uix_threadAuthor .messageContent .messageText *::text").getall(),
        }




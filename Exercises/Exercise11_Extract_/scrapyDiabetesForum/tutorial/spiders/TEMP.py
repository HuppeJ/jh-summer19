import scrapy
from bs4 import BeautifulSoup
import csv

def get_subforumLinks():
    dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise11_Extract_\scrapyDiabetesForum\getAllSubforumLinks"
    input_file_name = r"\counts_v2_totals.csv"
    with open(dir_path + input_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        subforumlinks = []
        for row in csv_reader:
            subforumLink = row[3]
            subforumlinks.append(subforumLink)
    subforumlinks.pop(0) 
    return subforumlinks

# scrapy crawl subforum
# scrapy crawl subforum -o subforum.json
# scrapy crawl subforum -o subforum.jl

class SubForumSpider(scrapy.Spider):
    name = "subforum"
    start_urls = get_subforumLinks()

    # Nb. of page scraped
    count = 1

    def parse(self, response):
        for question in response.css(".discussionListItems li[id]"):
            info = {
                "thread_id": question.css('::attr(id)').extract_first(),
                "thread_title": question.css(".title .PreviewTooltip::text").get(), 
                "thread_link": response.urljoin(question.css("h3.title a::attr(href)")[-1].get()), 
                "thread_author": question.css(".secondRow .username::text").get(),
                "thread_startDate": question.css(".secondRow .startDate .DateTime::text").get(),
                "thread_replies": question.css(".stats .major dd::text").get(),
                "thread_views": question.css(".stats .minor dd::text").get(),
            }

            # Follow link to question page
            #href = question.css("h3.title a::attr(href)")[-1].get()
            #question_page = response.urljoin(href)
            #request = scrapy.Request(question_page, self.parse_question)
            #request.meta['item'] = info

            yield info

        # If there is a Next button go to next page of threads
        has_nextPage = False
        a_tags = response.css(".pageNavLinkGroup.afterDiscussionListHandle .PageNav a::text")
        for tag in a_tags:
            if("Next" in tag.get()):
                has_nextPage = True
            # else:
                # print("TOTAL Nb OF PAGE SCRAPED: ", self.count)

        if (has_nextPage):
            # self.count = self.count + 1
            # Gets the last link (Next page link)
            href = response.css(".PageNav a::attr(href)")[-1].get()
            yield response.follow(href, self.parse)

    #def parse_question(self, response):
        #item = response.meta['item']
        #all_paragraphs = response.css(".messageList .uix_threadAuthor .messageContent .messageText *::text").getall()
        #map(str.strip, all_paragraphs)
        #seperator = " "
        #text = seperator.join(all_paragraphs)
        #clean_text = BeautifulSoup(text, "lxml").text
        #new_string = (clean_text.encode('ascii', 'ignore')).decode("utf-8")
        #new_string  = " ".join(new_string.split())
        #item["question"] = new_string
        #yield item






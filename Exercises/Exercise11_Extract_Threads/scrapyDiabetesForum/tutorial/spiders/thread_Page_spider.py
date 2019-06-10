import scrapy
from bs4 import BeautifulSoup
import csv

def get_subforumLinks():
    dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise11_Extract_\scrapyDiabetesForum\counts\original"
    input_file_name = r"\counts_v2.csv"
    with open(dir_path + input_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        subforumlinks = []
        for row in csv_reader:
            subforumLink = row[3]
            subforumlinks.append(subforumLink)
    subforumlinks.pop(0) 
    return subforumlinks

# scrapy crawl thread
# scrapy crawl thread -o thread.json
# scrapy crawl thread -o thread.jl

class ThreadSpider(scrapy.Spider):
    name = "thread"
    start_urls = [get_subforumLinks()[41]]

    # Nb. of page scraped
    count = 1

    def parse(self, response):
        for thread in response.css(".discussionListItems li[id]"):
            info = {
                "thread_id": thread.css('::attr(id)').extract_first(),
            }

            # Follow link to thread page
            href = thread.css("h3.title a::attr(href)")[-1].get()
            print("ICICI href", href)
            thread_page = response.urljoin(href)
            request = scrapy.Request(thread_page, self.parse_thread)
            request.meta['item'] = info

            yield request

        # If there is a Next button go to next page of threads
        has_nextPage = False
        a_tags = response.css(".pageNavLinkGroup.afterDiscussionListHandle .PageNav a::text")
        for tag in a_tags:
            if("Next" in tag.get()):
                has_nextPage = True

        if (has_nextPage):
            # self.count = self.count + 1
            # Gets the last link (Next page link)
            href = response.css(".PageNav a::attr(href)")[-1].get()
            yield response.follow(href, self.parse)

    def parse_thread(self, response):
        item = response.meta['item']

        for post in response.css(".messageList li[id]"):
            item["post_id"] = post.css('::attr(id)').extract_first()
            yield item

        
        # If there is a Next button go to next page of posts
        has_nextPage = False
        a_tags = response.css(".pageNavLinkGroup .PageNav a::text")
        for tag in a_tags:
            if("Next" in tag.get()):
                has_nextPage = True
        if (has_nextPage):
            print("has_nextPage")
            # self.count = self.count + 1
            # Gets the last link (Next page link)
            href = response.css(".PageNav a::attr(href)")[-1].get()       
            next_post_page = response.urljoin(href)   
            request = scrapy.Request(href, self.parse_thread)
            request.meta['item'] = item

            yield request


        #all_paragraphs = response.css(".messageList .uix_threadAuthor .messageContent .messageText *::text").getall()
        #map(str.strip, all_paragraphs)
        #seperator = " "
        #text = seperator.join(all_paragraphs)
        #clean_text = BeautifulSoup(text, "lxml").text
        #new_string = (clean_text.encode('ascii', 'ignore')).decode("utf-8")
        #new_string  = " ".join(new_string.split())
        #item["thread"] = new_string


    def parse_post(self, response):
        return ""
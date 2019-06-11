import scrapy
from bs4 import BeautifulSoup
import csv
import os
import re

def get_subforumLinks():
    dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise11_Extract_Threads\scrapyDiabetesForum\counts\original"
    input_file_name = r"\counts_v2.csv"
    with open(dir_path + input_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        subforumlinks = []
        for row in csv_reader:
            subforumLink = row[3]
            subforumlinks.append(subforumLink)
    return subforumlinks

def clean_text(text):
        clean_text = BeautifulSoup(text, "lxml").text
        new_string = (clean_text.encode("ascii", "ignore")).decode("utf-8")
        new_string  = " ".join(new_string.split())
        return new_string

def clean_text_for_filename(text):
    text = re.sub(r'[\\/*?:"<>|]', '', text)
    text = clean_text(text)
    return text

# scrapy crawl thread
# scrapy crawl thread -o thread.json
# scrapy crawl thread -o thread.jl

index = 30
class ThreadSpider(scrapy.Spider):
    name = "thread"
    start_urls = [get_subforumLinks()[index]]
    html_path_out = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise11_Extract_Threads\scrapyDiabetesForum\thread\source\30-diabetes management_blood glucose monitoring"

    # Nb. of page scraped
    count = 1

    def parse(self, response):
        for thread in response.css(".discussionListItems li[id]"):
            info = {
                "thread_id": thread.css("::attr(id)").extract_first(),
                "thread_title": thread.css(".title .PreviewTooltip::text").get(), 
                "thread_link": response.urljoin(thread.css("h3.title a::attr(href)")[-1].get()), 
                "thread_author": thread.css(".secondRow .username::text").get(),
                "thread_startDate": thread.css(".secondRow .startDate .DateTime::text").get(),
                "thread_replies": thread.css(".stats .major dd::text").get(),
                "thread_views": thread.css(".stats .minor dd::text").get(),
            }

            # Follow link to thread page
            href = thread.css("h3.title a::attr(href)")[-1].get()
            thread_page = response.urljoin(href)
            request = scrapy.Request(thread_page, self.parse_thread)
            request.meta["item"] = info

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
        title = clean_text_for_filename(response.css(".titleBar h1::text").get())
        if response.css(".currentPage::text"):
            page_number = response.css(".currentPage::text")[0].get()
        else:
            page_number = str(1)
        file_name = title + "_Page-" + page_number + ".html"
        html_file_name = os.path.join(self.html_path_out, file_name)
        with open(html_file_name, 'w', encoding="utf-8") as html_file:
            html_file.write(response.text)
        
        item = response.meta["item"]

        for post in response.css(".messageList li[id]"):
            item["post_id"] = post.css("::attr(id)").extract_first()
            item["post_username"] = post.css(".messageUserBlock .userText .username::text").get()
            item["post_userTitle"] = clean_text(post.css(".messageUserBlock .userText .userTitle::text").get())
            
            if post.css(".messageUserBlock .extraUserInfo").get() != None:
                pairsJustified = post.css(".messageUserBlock .extraUserInfo .pairsJustified")
                item["post_userNbMessages"] = pairsJustified[0].css("dd a::text").get()
                item["post_userLikesReceived"] = pairsJustified[1].css("dd::text").get()
                item["post_userTrophyPoints"] = pairsJustified[2].css("dd a::text").get()
            else:
                item["post_userNbMessages"] = None
                item["post_userLikesReceived"] = None
                item["post_userTrophyPoints"] = None

            item["post_DateTime"] = post.css(".messageDetails .uix_DateTime::text").get()
            
            item["post_like"] = 0
            item["post_agree"] = 0
            item["post_useful"] = 0
            item["post_funny"] = 0
            item["post_informative"] = 0
            item["post_friendly"] = 0
            item["post_optimistic"] = 0
            item["post_hug"] = 0

            for li_item in post.css(".dark_postrating_outputlist li"):
                title = li_item.css("img::attr(title)").get()
                value = li_item.css("strong::text").get()
                if title == "Like":
                    item["post_like"] = value
                if title == "Agree":
                    item["post_agree"] = value
                if title == "Useful":
                    item["post_useful"] = value
                if title == "Funny":
                    item["post_funny"] = value
                if title == "Informative":
                    item["post_informative"] = value
                if title == "Friendly":
                    item["post_friendly"] = value
                if title == "Optimistic":
                    item["post_optimistic"] = value
                if title == "Hug":
                    item["post_hug"] = value
            item["post_number"] = post.css(".messageDetails .postNumber::text").get()
            messageTextDiv = post.css(".messageText")
            #  messageTextDiv.xpath(".//text()[not(ancestor::div[@class='bbCodeQuote'])]").extract()
            
            # Get all textNode in messageText div
            all_text = post.css(".messageText *::text").getall()
            all_text = " ".join(all_text)

            # Get all textNode in Quote div
            all_quote_text = post.css(".messageText .bbCodeQuote *::text").getall() 
            all_quote_text = " ".join(all_quote_text)
            # Remove textNode comming from Quote div of messageText div
            if (all_quote_text in all_text):
                all_text = all_text.replace(all_quote_text, "")
            

            map(str.strip, all_text)
            map(str.strip, all_quote_text)
            all_text = clean_text(all_text)
            all_quote_text = clean_text(all_quote_text)

            item["post_messageText"] = all_text
            item["post_quoteText"] = all_quote_text
            
            yield item

       
        # If there is a Next button go to next page of posts
        has_nextPage = False
        a_tags = response.css(".pageNavLinkGroup .PageNav a::text")
        for tag in a_tags:
            if("Next" in tag.get()):
                has_nextPage = True
        if (has_nextPage):
            # self.count = self.count + 1
            # Gets the last link (Next page link)
            href = response.css(".PageNav a::attr(href)")[-1].get()       
            next_post_page = response.urljoin(href)   
            request = scrapy.Request(next_post_page, self.parse_thread)
            request.meta["item"] = item

            yield request




    def parse_post(self, response):
        return ""
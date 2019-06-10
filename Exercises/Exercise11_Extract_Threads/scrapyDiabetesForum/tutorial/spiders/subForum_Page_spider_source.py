import scrapy
from bs4 import BeautifulSoup
import csv
import os

def get_subforumLinks():
    dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise11_Extract_Threads\scrapyDiabetesForum\counts\original"
    input_file_name = r"\counts_v2.csv"
    with open(dir_path + input_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        subforumlinks = []
        for row in csv_reader:
            subforumLink = row[3]
            subforumlinks.append(subforumLink)
    subforumlinks.pop(0) 
    return subforumlinks

# scrapy crawl subforumsource
# scrapy crawl subforumsource -o subforumsource.json
# scrapy crawl subforumsource -o subforumsource.jl

class SubForumSourceSpider(scrapy.Spider):
    name = "subforumsource"
    start_urls = get_subforumLinks()
    html_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise11_Extract_Threads\scrapyDiabetesForum\subforum\subforum_source"

    def parse(self, response):
        title = response.css(".titleBar h1::text").get()
        page_number = response.css(".currentPage::text")[0].get()
        file_name = title + "_Page-" + page_number + ".html"
        html_file_name = os.path.join(self.html_path, file_name)
        with open(html_file_name, 'w', encoding="utf-8") as html_file:
            html_file.write(response.text)
            yield { }

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
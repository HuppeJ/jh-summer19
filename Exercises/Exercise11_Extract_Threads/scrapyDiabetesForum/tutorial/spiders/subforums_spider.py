import scrapy
from bs4 import BeautifulSoup
    
# scrapy crawl subforum
# scrapy crawl subforum -o subforum.json
# scrapy crawl subforum -o subforum.jl

class SubforumSpider(scrapy.Spider):
    name = "subforum"
    start_urls = ["https://www.diabetes.co.uk/forum/"]
    html_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise10_Extract_Number_of_Posts_and_Comments\scrapyDiabetesForum\source"

    def __init__(self):
        self.path_to_html = self.html_path + r"\forums.html"


    def parse(self, response):
        with open(self.path_to_html, 'w') as html_file:
            html_file.write(response.text)
        print("ICI")
        for category in response.css(".node.category.level_1"):
            for subforum in category.css(".node.forum.level_2"):
                
                info = {
                    "category_title": category.css(".categoryText .nodeTitle a::text").get().lower(),
                    "category_link": response.urljoin(category.css(".categoryText .nodeTitle a::attr(href)")[0].get()),
                    "subforum_title": subforum.css(".nodeText .nodeTitle a::text").get().lower(),
                    "subforum_link": response.urljoin(subforum.css(".nodeText .nodeTitle a::attr(href)")[0].get()),
                    "subforum_description": subforum.css(".nodeText .nodeDescription::text").get(),
                    "subforum_nb_posts": subforum.css(".nodeStats dl dd::text")[0].get(),
                    "subforum_nb_comments": subforum.css(".nodeStats dl dd::text")[1].get(),
                }
                yield info






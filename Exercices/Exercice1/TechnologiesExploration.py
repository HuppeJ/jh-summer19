
#%% [markdown]
## Sample discussion on diabetes forum analysis
### [diabetes.co.uk: Essential info for choosing a pump](https://www.diabetes.co.uk/forum/threads/essential-info-for-choosing-a-pump.6699/)


#%% 
# Getting the html page
import requests
pageUrl = "https://www.diabetes.co.uk/forum/threads/essential-info-for-choosing-a-pump.6699/"
r = requests.get(pageUrl)
c = r.content

# Soup the html page
from bs4 import BeautifulSoup
soup = BeautifulSoup(c)

# Outputing the soup version of the html page to find tags for parsing the comments
#with open("diabetesForumTestQuestion.html", "w") as file:
#    file.write(str(soup.encode("utf-8")))


# Extracting relevant data
parsedPage = ""

# Adding title
title = soup.find("h1").text
parsedPage = parsedPage + title + "\n"

questionElem = soup.select('.uix_threadAuthor .messageText')[0]
content = questionElem.text.strip()
question = "Question: " + content
parsedPage = parsedPage + question + "\n"


# Adding the comments
commentsElem = soup.select('.uix_message .messageText')
for i, commentElem in enumerate(commentsElem):
    content = commentElem.text.strip()
    comment = "Comment: " + str(i + 1) + " " + content + "\n"
    parsedPage = parsedPage + comment


print(parsedPage)

# Write parsedPage in file 
#with open("diabetesForumTestQuestionData.txt", "w") as file:
#    file.write(str(parsedPage.encode("utf-8")))








#%%

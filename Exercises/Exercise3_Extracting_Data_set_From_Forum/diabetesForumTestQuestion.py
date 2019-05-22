
#%% [markdown]
## Sample discussion on diabetes forum analysis
### [diabetes.co.uk: Essential info for choosing a pump](https://www.diabetes.co.uk/forum/threads/essential-info-for-choosing-a-pump.6699/)


#%% 
# Getting the html page
import requests
pageUrl = "https://www.diabetes.co.uk/forum/threads/essential-info-for-choosing-a-pump.6699/"
r = requests.get(pageUrl)
c = r.content

#%% 
# Soup the html page
from bs4 import BeautifulSoup
soup = BeautifulSoup(c)

#%% 
# Outputing the soup version of the html page to find tags for parsing the comments
#with open("diabetesForumTestQuestion.html", "w") as file:
#    file.write(str(soup.encode("utf-8")))

#%% 
# Extracting relevant data

# Adding title
title = {"id": "title", "content": soup.find("h1").text}

questionElem = soup.select('.uix_threadAuthor .messageText')[0]
question = {"id": "question", "content": questionElem.text.strip()}

# Adding the comments
commentsElem = soup.select('.uix_message .messageText')
parsedComments = []
for i, commentElem in enumerate(commentsElem):
    commentId = "comment " + str(i + 1) + ": "
    content = commentElem.text.strip() + "\n"
    comment = {"id": commentId, "content": content}
    parsedComments.append(comment)

# Remove Question
parsedComments.pop(0)
#%% 
# Write parsedPage in .csv file
import csv
fieldnames = ["id", "content"]

with open("diabetesForumTestQuestionData.csv", mode="w", encoding="utf-8", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    try:      
        writer.writerow(title)
        writer.writerow(question)
        for parsedComment in parsedComments:
            writer.writerow(parsedComment)
    except Exception as e:
        print("Have not been able to write in csv file", e)   
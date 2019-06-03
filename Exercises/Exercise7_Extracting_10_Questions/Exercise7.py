
#%% [markdown]
## Sample discussions on diabetes forum analysis
### Sample manually extracted from all different sub forums of https://www.diabetes.co.uk/forum/


#%% 
# Getting the html page
import requests
from bs4 import BeautifulSoup

URLs = [
    #"https://www.diabetes.co.uk/forum/threads/discovery-sheets.5797/",
    #"https://www.diabetes.co.uk/forum/threads/new-type-1-drug-trialled-in-cardiff.156338/",
    #"https://www.diabetes.co.uk/forum/threads/how-can-they-put-me-into-esa-wrag-group-when-my-wife-is-care.22461/",
    #"https://www.diabetes.co.uk/forum/threads/chicken-pox.17891/",
    #"https://www.diabetes.co.uk/forum/threads/newcastle-diet-journey.47081/",
    #"https://www.diabetes.co.uk/forum/threads/diabetic-craft-club.61611/",
    #"https://www.diabetes.co.uk/forum/threads/can-pregnancy-hormones-cause-high-blood-sugar-levels.117443/",
    #"https://www.diabetes.co.uk/forum/threads/ladas-preserving-their-beta-cells.62177/",
    #"https://www.diabetes.co.uk/forum/threads/statins.156511/",
    #"https://www.diabetes.co.uk/forum/threads/gluten-free-baking.153152/",
]

for url in URLs:
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c)
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

    # Write parsedPage in .csv file
    import csv
    fieldnames = ["id", "content"]

    dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise7_Extracting_10_Questions"
    output_file_name = "\question" + str(8) + ".csv"

    with open(dir_path + output_file_name, mode="w", encoding="utf-8", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        try:      
            writer.writerow(title)
            writer.writerow(question)
            for parsedComment in parsedComments:
                writer.writerow(parsedComment)
        except Exception as e:
            print("Have not been able to write in csv file", e)   




#%%

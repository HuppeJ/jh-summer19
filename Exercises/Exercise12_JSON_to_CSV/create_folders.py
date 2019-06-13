#%%

import os
import csv

dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise11_Extract_Threads\scrapyDiabetesForum\thread"

dir_counts = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise11_Extract_Threads\scrapyDiabetesForum\counts"
input_file_name = r"\counts_v2_no_titles.csv"
index = 1
with open(dir_counts + input_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    subforumTitles = []
    for row in csv_reader:
        category_title = row[0]
        subforum_title= row[2]
        directory_name = str(index) + "-" + category_title + "_" + subforum_title
        index = index + 1
        temp = os.path.join(dir_path, directory_name)
        try:  
            os.mkdir(temp)
        except OSError:  
            print ("Creation of the directory %s failed" % temp)
        else:  
            print ("Successfully created the directory %s " % temp)




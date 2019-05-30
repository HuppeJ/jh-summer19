
#%% [markdown]
## Labeling sentences to create datasets
### - Extracting all sentences to create a datasets

#%% 
import csv
import os
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import ast

#%% 
# Init tools
stop_words = stopwords.words('english')
porter = PorterStemmer()
lemmatizer = WordNetLemmatizer()

#%%
# Open question database csv file
dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise5_Creating_Labelled_Datasets"
input_file_name = "\questions_db_parsed.csv"
# input_file_name = "\questions_db_sample_parsed.csv"

with open(dir_path + input_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Creating a dictionary with all the sentences of every question
    # data_dict = {"thread_id": sentences of question } 
    for row in csv_reader:
        data_dict = {rows[0]:rows[2] for rows in csv_reader}


#print(lemmatized_words)
#%%
# Write in csv file all sentences
output_file_name = "\sentences_db.csv"
# output_file_name = "\sentences_db_sample.csv"

with open(dir_path + output_file_name, mode='w', encoding="utf-8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    csv_writer.writerow(["sentences", "Expresses a need?"])

    for k in data_dict:
        sentences_list = ast.literal_eval(data_dict[k])
        for s in sentences_list:
            csv_writer.writerow([s])



#%%

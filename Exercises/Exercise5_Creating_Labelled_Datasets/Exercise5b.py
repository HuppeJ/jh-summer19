
#%% [markdown]
## Labeling sentences to create datasets
### - Selecting a portion of the 20 000 sentences generated

#%% 
import csv
import os
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import ast
import random


#%% 
# Init tools
stop_words = stopwords.words('english')
porter = PorterStemmer()
lemmatizer = WordNetLemmatizer()

#%%
# Open sentences database csv file
dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise5_Creating_Labelled_Datasets"
input_file_name = "\sentences_db.csv"
# input_file_name = "\sentences_db_sample.csv"
counter = 0
total = 0

with open(dir_path + input_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    selected_sentences = []
    for row in csv_reader:
        sentence = row[0]
        tokenned_words = word_tokenize(sentence)
        total = total + 1
        if 4 < len(tokenned_words) < 12:
            selected_sentences.append(sentence)
            counter = counter + 1
        #data_dict = {rows[0]:rows[2] for rows in csv_reader}


    sample = random.sample(selected_sentences, 200)

print(total)
print(counter)

#print(lemmatized_words)
#%%
# Write in csv file all sentences
output_file_name = "\sentences_db_parsed.csv"
# output_file_name = "\sentences_db_sample_parsed.csv"

with open(dir_path + output_file_name, mode='w', encoding="utf-8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    csv_writer.writerow(["sentences_parsed", "Expresses a need?"])

    for s in sample:
        csv_writer.writerow([s])



#%%

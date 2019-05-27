
#%% [markdown]
## Extracting Sentences Containing Requirements Keywords

#%% 
import csv
import os
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#%% 
# Init tools
stop_words = stopwords.words('english')
porter = PorterStemmer()
lemmatizer = WordNetLemmatizer()

#%%
# Open question database csv file
dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise4_Extracting_Requirements_Sentences_Questions"
input_file_name = "\questions_db.csv"
# input_file_name = "\questions_db_sample.csv"

with open(dir_path + input_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Creating a dictionary with all the questions
    # data_dict = {"thread_id": question } 
    for row in csv_reader:
        data_dict = {rows[0]:rows[6] for rows in csv_reader}

#%% 
# Adding attribute sentences to data_dict
# data_dict = {"thread_id": {"question": question, "sentences": sentences}} 
for k in data_dict:
    # split into sentences
    sentences = sent_tokenize(data_dict[k])
    for i, sentence in enumerate(sentences):
        sentences[i] = sentence.lower()
    question = data_dict[k]
    data_dict[k] = {
        "question": question, 
        "sentences": sentences
    }

#%%
# Finding requirements sentences
requirements_word_dict = {"need", "how", "i will be interested", "can't find", "i am trying", "help"}
requirements_sentences = []
for k in data_dict:
    for sentence in data_dict[k]["sentences"]:
        if any(word in sentence for word in requirements_word_dict):
            requirements_sentences.append(sentence)
    question = data_dict[k]["question"]
    sentences = data_dict[k]["sentences"]
    data_dict[k] = {
        "question": question, 
        "sentences": sentences, 
        "requirements_sentences": requirements_sentences
    }
    requirements_sentences = []

#%%

# Clean requirements_sentences's words
for k in data_dict:
    lemmatized_words = []    
    words = []

    for requirements_sentence in data_dict[k]["requirements_sentences"]:
        tokenned_words = word_tokenize(requirements_sentence)
        cleanned_words = [word for word in tokenned_words if word not in stop_words and word.isalpha()]
        words.extend(cleanned_words)
        for word in words:
            # print(porter.stem(word))
            # print(lemmatizer.lemmatize(word))
            lemmatized_words.append(lemmatizer.lemmatize(word))
    
    question = data_dict[k]["question"]
    sentences = data_dict[k]["sentences"]
    requirements_sentences = data_dict[k]["requirements_sentences"]

    data_dict[k] = {
        "question": question, 
        "sentences": sentences, 
        "requirements_sentences": requirements_sentences, 
        "words": words,
        "lemmatized_words": lemmatized_words 
    }



#print(lemmatized_words)
#%%
# Write in csv file new values
output_file_name = "\questions_db_parsed.csv"
# output_file_name = "\questions_db_sample_parsed.csv"

with open(dir_path + output_file_name, mode='w', encoding="utf-8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    csv_writer.writerow(["thread-id", "question", "sentences", "requirements_sentences", "words", "lemmatized_words"])

    for k in data_dict:
        csv_writer.writerow([k, data_dict[k]["question"], data_dict[k]["sentences"], data_dict[k]["requirements_sentences"], data_dict[k]["words"], data_dict[k]["lemmatized_words"]])

#%%

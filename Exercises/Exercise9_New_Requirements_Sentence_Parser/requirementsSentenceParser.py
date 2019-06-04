
#%% [markdown]
## Extracting Sentences Containing Requirements Keywords V2

### Algorithm: 

# - 1. Open question database csv file
# - 2. Split question into sentences
# - 3. Clean sentences text
#   - 3.1 Remove links
#   - 3.2 Remove @ references
#   - 3.3 Only keep characters matching 
#   - 3.4 Lower all characters
# - 4. Get the requirement words from csv file
# - 5. Find the requirements sentences based on the requirement words
#   - 5.1 Possible TODO: We could check if lemmatizing or stemming the words in the sentences 
#       before checking if they are part of the requirement words would help  
# - 6. Remove stop words from  requirements sentences
# - 7.  Get the lemmatized words from the remaining words
# - 8.  Write in csv file new values

#%% 
import csv
import os
import re
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
dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise9_New_Requirements_Sentence_Parser"
input_file_name = "\questions_db.csv"
#input_file_name = "\questions_db_sample.csv"

with open(dir_path + input_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Creating a dictionary with all the questions
    # data_dict = {"thread_id": question } 
    for row in csv_reader:
        data_dict = {rows[0]:rows[6] for rows in csv_reader}

#%% 
# Split question into sentences
# data_dict = {"thread_id": {"question": question, "sentences": sentences}} 
for k in data_dict:
    sentences = sent_tokenize(data_dict[k])
    for i, sentence in enumerate(sentences):
        # Clean sentences text
        sentences[i] = re.sub(r"https?://\S+", "" , sentences[i])
        sentences[i] = re.sub(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " " , sentences[i])
        sentences[i] = re.sub(r"@", "at" , sentences[i])
        sentences[i] = sentences[i].lower()
    question = data_dict[k]
    data_dict[k] = {
        "question": question, 
        "sentences": sentences
    }

#%% 
# Get the requirement words from csv file
requirement_words = []
annotation_file_name = r"\improved_annotations.csv"

requirements_word_dict = {}
with open(dir_path + annotation_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    requirements_word_dict = {rows[0] for rows in csv_reader}

#%%
# Find the requirements sentences based on the requirement words
requirements_sentences = []
for k in data_dict:
    for sentence in data_dict[k]["sentences"]:
        # TODO: We could check if lemmatizing or stemming the word would help  
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
# Remove stop words from requirements sentences
for k in data_dict:
    lemmatized_words = []    
    words = []

    for requirements_sentence in data_dict[k]["requirements_sentences"]:
        tokenned_words = word_tokenize(requirements_sentence)
        cleanned_words = [word for word in tokenned_words if word not in stop_words and word.isalpha()]
        words.extend(cleanned_words)
        # Get the lemmatized words from the remaining words
        for word in words:
            lemmatized_words.append(lemmatizer.lemmatize(word))
    
    question = data_dict[k]["question"]
    sentences = data_dict[k]["sentences"]
    requirements_sentences = data_dict[k]["requirements_sentences"]

    data_dict[k] = {
        "question": question, 
        "sentences": sentences, 
        "requirements_sentences": requirements_sentences, 
        "words": words,
        "lemmatized_words": list(dict.fromkeys(lemmatized_words)) 
    }

#%%
# Write in csv file new values
output_file_name = "\questions_db_parsed.csv"
#output_file_name = "\questions_db_sample_parsed.csv"

with open(dir_path + output_file_name, mode='w', encoding="utf-8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    csv_writer.writerow(["thread-id", "question", "sentences", "requirements_sentences", "words", "lemmatized_words"])

    for k in data_dict:
        csv_writer.writerow([k, data_dict[k]["question"], data_dict[k]["sentences"], data_dict[k]["requirements_sentences"], data_dict[k]["words"], data_dict[k]["lemmatized_words"]])


#%%


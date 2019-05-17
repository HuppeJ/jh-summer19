
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
dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise2_Extracting_Sentences_Containing_Requirements_Keywords"

with open(dir_path + "\diabetesForumTestQuestionData.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data_dict = {rows[0]:rows[1] for rows in csv_reader}


# Creating a dictionary with all the comments
# comments_dict = {"comment i :": comment_text } 
comments_dict = {k: v for k, v in data_dict.items() if k.startswith('comment')}

# Adding attribute sentences to comments_dict
# comments_dict = {"comment i :": {"comment": comment, "sentences": sentences}} 
for k in comments_dict:
    # split into sentences
    sentences = sent_tokenize(comments_dict[k])
    for i, sentence in enumerate(sentences):
        sentences[i] = sentence.lower()
    comment = comments_dict[k]
    comments_dict[k] = {"comment": comment, "sentences": sentences}

# Finding requirements sentences
requirements_word_dict = {"need", "how", "i will be interested", "can't find", "i am trying"}
requirements_sentences = []
for k in comments_dict:
    for sentence in comments_dict[k]["sentences"]:
        if any(word in sentence for word in requirements_word_dict):
            requirements_sentences.append(sentence)
print(requirements_sentences)

stop_words = stopwords.words('english')
porter = PorterStemmer()
lemmatizer = WordNetLemmatizer()

requirements_words= []
for sentence in requirements_sentences:
    words = word_tokenize(sentence)
    words = [word for word in words if word not in stop_words and word.isalpha()]
    lemmatized_words = []
    for word in words:
        # print(porter.stem(word))
        # print(lemmatizer.lemmatize(word))
        lemmatized_words.append(lemmatizer.lemmatize(word))

print(lemmatized_words)
#%%

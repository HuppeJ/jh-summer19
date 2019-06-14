
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
import pandas as pd
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

#%% 
# Init tools
stop_words = stopwords.words('english')
porter = PorterStemmer()
lemmatizer = WordNetLemmatizer()


#%% 
# SENTENCES

def get_sentences(text):
    return sent_tokenize(text)

def remove_links(text):
    return re.sub(r"https?://\S+", "" , text)

def remove_special_characters(text):
    return re.sub(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " " , text)

def replace_at_symbols(text):
    return re.sub(r"@", "at" , text)

def clean_text(text):
    cleanned_text = remove_links(text)
    cleanned_text = remove_special_characters(cleanned_text)
    cleanned_text = replace_at_symbols(cleanned_text)
    cleanned_text = cleanned_text.lower()
    return cleanned_text

def parse_text_to_sentences(text):
    sentences = get_sentences(text)
    for i, sentence in enumerate(sentences):
        # Clean sentences text
        sentences[i] = clean_text(sentences[i])

    return sentences

def get_percentage_stats(column):
    return column.value_counts(normalize=True) * 100

#%%
# GET SENTENCES

# Open question database csv file
dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise13_Creating_Sample_Datasets"
input_file_name = r"\4_sample_10.csv"
df = pd.read_csv(dir_path + input_file_name)

# Applies function to each row
# df["post_messageText_sentences"] = df.apply(parse_text_to_sentences, axis=1)
sentence_column = "sentence"
df_sentences = pd.DataFrame(columns=[sentence_column])

for name, row in df.iterrows():
    sentences = parse_text_to_sentences(str(row["post_messageText"]))
    # df_sentences = pd.concat([df_sentences([s], columns=[sentence_column]) for s in sentences], ignore_index=True)

    for sentence in sentences:
        #dict((sentence) for a in [sentence_column])
        df_sentences = df_sentences.append({sentence_column: sentence}, ignore_index=True)

print(df_sentences)

#%% 
# REQUIREMENT WORDS

# Get the requirement words from csv file
requirement_words = []
annotation_file_name = r"\improved_annotations_v2.csv"

requirements_word_dict = {}
with open(dir_path + annotation_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    requirements_word_dict = {rows[0] for rows in csv_reader}

has_requirement_words_column = "has_requirement_words"
df_sentences[has_requirement_words_column] = 0

# Find the requirements sentences based on the requirement words
for row in df_sentences.itertuples():
    sentence = df_sentences.at[row.Index, sentence_column]
    if any(word in sentence for word in requirements_word_dict):
        df_sentences.at[row.Index, has_requirement_words_column] = 1

print(get_percentage_stats(df_sentences[has_requirement_words_column]))
print(df_sentences)

#%%
# REMOVE STOP WORDS FROM SENTENCES
words = []
without_stop_words_column = "without_stop_words"
df_sentences[without_stop_words_column] = ""

for row in df_sentences.itertuples():
    sentence = df_sentences.at[row.Index, sentence_column]
    tokenned_words = word_tokenize(sentence)
    cleanned_words = [word for word in tokenned_words if word not in stop_words and word.isalpha()]
    words.extend(cleanned_words)
    df_sentences.at[row.Index, without_stop_words_column] = words
    words = []

print(df_sentences)
#%%
# LEMMATIZE WORDS
lemmatized_words = []
lemmatized_words_column = "lemmatized_words"
df_sentences[lemmatized_words_column] = ""

for row in df_sentences.itertuples():
    words = df_sentences.at[row.Index, without_stop_words_column]
    for word in words:
        lemmatized_words.append(lemmatizer.lemmatize(word))
    df_sentences.at[row.Index, lemmatized_words_column] = lemmatized_words
    lemmatized_words = []

print(df_sentences)

#%%
# POST TAGGING
words = []
pos_tags_column = "pos_tags"
df_sentences[pos_tags_column] = ""

for row in df_sentences.itertuples():
    sentence = df_sentences.at[row.Index, sentence_column]
    tokenned_words = word_tokenize(sentence)
    tags = pos_tag(tokenned_words)
    df_sentences.at[row.Index, pos_tags_column] = tags

print(df_sentences)


#%%
# TD-IDF

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

corpus = [
    df_sentences.at[0, sentence_column], 
    df_sentences.at[1, sentence_column]
]

print(corpus)

vectorizer = TfidfVectorizer()
# X = tfidf_matrix 
X = vectorizer.fit_transform(corpus)

df = pd.DataFrame(X.toarray(), columns = vectorizer.get_feature_names())
print(df)


#%%
# WRITE IN CSV FILE NEW VALUES
output_file_name = "\sentences_analysis_10_v1.csv"

df_sentences.to_csv(dir_path + output_file_name, sep=',', encoding='utf-8')


#%%


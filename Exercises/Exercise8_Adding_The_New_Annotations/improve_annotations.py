
#%% [markdown]
## Extracting Sentences Containing Requirements Keywords

### Algorithm: 

# - 1. Get the original annotations
# - 2. Lemmatize the original annotations
# - 3. Find all synonyms of annotations
# - 4. Merge the two annotations lists
# - 5. Remove duplicates
# - 6. Write in csv file new values

#%% 
import csv
import os
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

#%% 
# Init tools
lemmatizer = WordNetLemmatizer()
#%%
dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise8_Adding_The_New_Annotations"
input_file_name = r"\annotations.csv"

annotations = []

# Get the original annotations
with open(dir_path + input_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        annotations.append(row[0])

# Lemmatize the original annotations
for i, annotation in enumerate(annotations): 
    annotations[i] = lemmatizer.lemmatize(annotation)

# Find all synonyms of annotations
synonym_annotations = []
for annotation in annotations:
    for syn in wordnet.synsets(annotation):
        for l in syn.lemmas():
            synonym_annotations.append(l.name())

# Merge the two annotations lists
improved_annotations = annotations + synonym_annotations

# Remove duplicates
improved_annotations = list(dict.fromkeys(improved_annotations))

#%%
# Write in csv file new values
output_file_name = "\improved_annotations.csv"

with open(dir_path + output_file_name, mode='w', encoding="utf-8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for annotation in improved_annotations:
        csv_writer.writerow([annotation])
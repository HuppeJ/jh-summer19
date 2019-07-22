### Algorithm: 

# - 1. Get the list of initial keywords retrieved manually through conversation analysis from annotation.csv
# - 2. Split post_messageText into sentences
# - 3. Clean sentences text

# Imports
import csv
import os
import re
import pandas as pd
from nltk.corpus import wordnet
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH


def run():
    print("Running get_synonyms")
    
    # Load initial keywords list
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "annotations", "annotations.csv"]
    input_file = os.path.join('', *file_path)
    df_annotations = pd.read_csv(input_file)
    df_annotations_with_synonyms = df_annotations.copy()

    keywords = df_annotations["keywords"].tolist()
    synonym_annotations = []

    for keyword in keywords:
        for syn in wordnet.synsets(keyword):
            for lemma in syn.lemmas():
                synonym_annotations.append(lemma.name())

    # Merge the two annotations lists
    improved_annotations = keywords + synonym_annotations
    
    # Remove duplicates
    improved_annotations = list(dict.fromkeys(improved_annotations))
    
    temp = "business_organization"
    print("_" in temp)
    # Remove keywords with "_"
    
    for annotation in improved_annotations:
        if "_" in annotation or "-" in annotation:
            print(annotation)
            improved_annotations.remove(annotation)

    # Add keywords to DataFrame
    df_annotations_with_synonyms = pd.DataFrame()
    df_annotations_with_synonyms["keywords"] = improved_annotations

    # Write output file
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "annotations", "annotations_with_synonyms.csv"]
    output_file = os.path.join('', *output_path)
    df_annotations_with_synonyms.to_csv(output_file, sep=',', encoding='utf-8', index=False)    

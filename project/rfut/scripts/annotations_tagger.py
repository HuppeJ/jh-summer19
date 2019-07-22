### Algorithm: 

# Imports
import csv
import os
import re
import pandas as pd
from nltk import sent_tokenize
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from rfut.objects.sentence_parser import SentenceParser 

# Time: --- 95.95727944374084 seconds ---

def run():
    print("Running : annotations_tagger")

    # Init tools 
    sp = SentenceParser()

    # Load sample of threads data in dataframe
    #  TODO : parsed_0.02_kept_threads_with_is_question.csv
    threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "parsed_0.02_kept_threads_with_is_question.csv"]
    input_file = os.path.join('', *threads_sample_path)
    df_input = pd.read_csv(input_file)

    # Load the annotations 
    threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "annotations", "annotations_with_synonyms.csv"]
    input_file = os.path.join('', *threads_sample_path)
    df_annotations = pd.read_csv(input_file)
    annotations = df_annotations["keywords"].tolist()

    df_input["has_annotations"] = False

    # df_input = df_input.sample(100)

    for row in df_input.itertuples():
        sentence = str(df_input.at[row.Index, "sentence"])
        if any(sp.is_word_in_text(word, sentence) for word in annotations):
            df_input.at[row.Index, "has_annotations"] = True


     

    # Write output file
    filename = "parsed_0.02_kept_threads_with_is_question_and_annotations.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_input.to_csv(output_file, sep=',', encoding='utf-8', index=False)
    




### Algorithm: 

# Imports
import csv
import os
import re
import math
import pandas as pd
from nltk import sent_tokenize
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from rfut.objects.sentence_parser import SentenceParser 

def run():
    print("Running : core_nlp_clause_tags_to_is_question")
    # GET SENTENCES

    # Init tools 
    sp = SentenceParser()

    # Load sample of threads data in dataframe
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "parsed_0.02_kept_threads_with_core_nlp_clause_tags.csv"]
    input_file = os.path.join('', *file_path)
    df_input = pd.read_csv(input_file)

    df_input["is_question"] = False

    for row in df_input.itertuples():
        core_nlp_clause_tag = df_input.at[row.Index, "core_nlp_clause_tag"]
        if core_nlp_clause_tag == 3 or core_nlp_clause_tag == 5:
            df_input.at[row.Index, "is_question"] = True

    # Write output file
    filename = "parsed_0.02_kept_threads_with_is_question.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_input.to_csv(output_file, sep=',', encoding='utf-8', index=False) 
    




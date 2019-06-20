### Algorithm: 

# Imports
import csv
import os
import re
import pandas as pd
from nltk import sent_tokenize
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from rfut.objects.sentence_parser import SentenceParser 

from nltk.parse import CoreNLPParser
parser = CoreNLPParser(url='http://localhost:9000')

def run():
    print("Running : core_nlp_interrogative_sentence_tagger")

    # Init tools 
    sp = SentenceParser()

    # Load sample of threads data in dataframe
    threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "parsed_0.02_of_threads_kept_threads.csv"]
    input_file = os.path.join('', *threads_sample_path)
    df_input = pd.read_csv(input_file)

    df_input["is_question"] = False

    for row in df_input.itertuples():
        sentence = str(df_input.at[row.Index, "sentence"])
        try:
            t_iterator = parser.raw_parse(sentence)
            t_root = next(t_iterator)
            t = t_root[0]
            label = t.label()

            if label == "SBARQ" or label == "SQ":
                df_input.at[row.Index, "is_question"] = True
        except:
            print("An exception occurred with", sentence)
     

    # Write output file
    filename = "parsed_0.02_kept_threads_with_is_question.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *posts_path)
    df_input.to_csv(output_file, sep=',', encoding='utf-8') 
    




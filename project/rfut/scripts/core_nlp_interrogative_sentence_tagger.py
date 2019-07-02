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

    # First run of the program
    # Load sample of threads data in dataframe
    #threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "parsed_0.02_of_threads_kept_threads.csv"]
    #input_file = os.path.join('', *threads_sample_path)
    #df_input = pd.read_csv(input_file)
    # df_input["is_question"] = False

    # Second run and more of the program
    threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "parsed_0.02_kept_threads_with_is_question.csv"]
    input_file = os.path.join('', *threads_sample_path)
    df_input = pd.read_csv(input_file)

    df_input_1 = df_input.iloc[0:10000]
    df_input_2 = df_input.iloc[10000:20000]
    df_input_3 = df_input.iloc[20000:30000]
    df_input_4 = df_input.iloc[30000:40000]
    df_input_5 = df_input.iloc[40000:50000]
    df_input_6 = df_input.iloc[50000:60000]
    df_input_7 = df_input.iloc[60000:70000]
    df_input_8 = df_input.iloc[70000:80000]
    df_input_9 = df_input.iloc[90000:100000]
    df_input_10 = df_input.iloc[100000:110000]
    df_input_all_end = df_input.iloc[50000:110000]
    df_input_sample = df_input_all_end
    
    # Second and more run of the program
    for row in df_input_sample.itertuples():
        sentence = str(df_input_sample.at[row.Index, "sentence"])
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
    df_input.to_csv(output_file, sep=',', encoding='utf-8', index=False)
    




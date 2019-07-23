# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from rfut.objects.sentence_parser import SentenceParser

def run():
    # Init tools 
    sp = SentenceParser()

    # Load data
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "sample_dataset_mturk_no2.csv"]
    input_file = os.path.join('', *file_path)
    df_input = pd.read_csv(input_file)
    df_input_sentence_id = df_input.copy()

    df_input_sentence_id["sentence_id"] = ""

    for row in df_input_sentence_id.itertuples():
        thread_id = df_input_sentence_id.at[row.Index, "thread_id"]
        post_number = df_input_sentence_id.at[row.Index, "post_number"]
        sentence_number = df_input_sentence_id.at[row.Index, "sentence_number"]
        sentence_id = sp.get_sentence_id(thread_id, post_number, sentence_number)
        df_input_sentence_id.at[row.Index, "sentence_id"] = sentence_id

    # Write df_sample_dataset
    filename = "sample_dataset_mturk_no2_with_sentence_ids.csv"
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *file_path)
    df_input_sentence_id.to_csv(output_file, sep=',', encoding='utf-8', index=False)
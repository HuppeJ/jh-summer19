# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

# TODO REMOVE THIS FILE SHOULD NOT NEED IT

def run():
    print("Running: update_mturk_sample")

    # Load data
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "threads_text_for_summarization_no1.csv"]
    input_file = os.path.join('', *file_path)
    df_sum = pd.read_csv(input_file)

    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "sample_dataset_mturk_no1.csv"]
    input_file = os.path.join('', *file_path)
    df_mturk = pd.read_csv(input_file)
    

    thread_ids = df_sum["thread_id"].tolist()
    # Remove duplicates
    thread_ids_sum = list(dict.fromkeys(thread_ids))

    thread_ids = df_mturk["thread_id"].tolist()
    # Remove duplicates
    thread_ids_mturk = list(dict.fromkeys(thread_ids))

    print(set(thread_ids_mturk) == set(thread_ids_sum))
    
    print("len(thread_ids_mturk)", len(thread_ids_mturk))
    print("len(thread_ids_sum)", len(thread_ids_sum))

    df_mturk_updated = pd.DataFrame()

    for row in df_mturk.itertuples():
        thread_id = df_mturk.at[row.Index, "thread_id"]
        post_number = df_mturk.at[row.Index, "post_number"]
        sentence_number = df_mturk.at[row.Index, "sentence_number"]
        new_row = df_input.loc[(df_input["thread_id"] == thread_id) & (df_input["post_number"] == post_number) & (df_input["sentence_number"] == sentence_number)]
        df_mturk_updated = df_mturk_updated.append(new_row)

    # Split df_mturk_updated into the 3 datasets of 3500
    # for each dataset make sure every row is part of it ex.: FT, FF & TX
    # if one row doesn't match FT, FF & TX
    #   Go into parsed_0.02_kept_threads_with_is_question_and_annotations 
    #       Select the sub datasets 
    #           Select all sentences matching the thread_id
    #               Select a sentences that is not already part of the dataset

    # Or do it by hand


    # Write df_sample_dataset
    filename = "sample_dataset_mturk_no1.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_mturk_updated.to_csv(output_file, sep=',', encoding='utf-8', index=False) 
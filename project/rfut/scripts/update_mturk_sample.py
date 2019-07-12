# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

def run():
    print("Running: update_mturk_sample")

    # Load sample of threads data in dataframe
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "parsed_0.02_kept_threads_with_is_question_and_annotations.csv"]
    input_file = os.path.join('', *file_path)
    df_input = pd.read_csv(input_file)

    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "sample_dataset_mturk_no11.csv"]
    input_file = os.path.join('', *file_path)
    df_mturk = pd.read_csv(input_file)

    df_mturk_updated = pd.DataFrame()

    for row in df_mturk.itertuples():
        thread_id = df_mturk.at[row.Index, "thread_id"]
        post_number = df_mturk.at[row.Index, "post_number"]
        sentence_number = df_mturk.at[row.Index, "sentence_number"]
        new_row = df_input.loc[(df_input["thread_id"] == thread_id) & (df_input["post_number"] == post_number) & (df_input["sentence_number"] == sentence_number)]
        df_mturk_updated = df_mturk_updated.append(new_row)




    # Write df_sample_dataset
    filename = "sample_dataset_mturk_no1.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_mturk_updated.to_csv(output_file, sep=',', encoding='utf-8', index=False) 
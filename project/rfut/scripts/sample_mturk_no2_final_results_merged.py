# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

def run():

    # Load data
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH,  "sample_dataset_mturk_no2_with_sentence_ids.csv"]
    input_file = os.path.join('', *file_path)
    df_mturk = pd.read_csv(input_file)

    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "mturk", "submission_mturk_no2", "results", "sample_mturk_no2_results_grouped.csv"]
    input_file = os.path.join('', *file_path)
    df_results = pd.read_csv(input_file)

    df_mturk = df_mturk.drop(["sentence"], axis=1)


    df_mturk = df_mturk.merge(df_results, on='sentence_id')


    # Write output file
    filename = "sample_dataset_mturk_no2_merged_results.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH,  "mturk", "submission_mturk_no2", "results", filename]
    output_file = os.path.join('', *output_path)
    df_mturk.to_csv(output_file, sep=',', encoding='utf-8', index=False)
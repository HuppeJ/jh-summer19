# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

def run():
    # Load data
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "mturk", "submission_mturk_no2", "results", "sample_dataset_mturk_no2_results_to_rows.csv"]
    input_file = os.path.join('', *file_path)
    df_results_to_rows = pd.read_csv(input_file)

    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH,  "sample_dataset_mturk_no2_with_sentence_ids.csv"]
    input_file = os.path.join('', *file_path)
    df_mturk = pd.read_csv(input_file)

    df_results_to_rows["sentence"] = ""

    for row in df_results_to_rows.itertuples():
        sentence_id = df_results_to_rows.at[row.Index, "sentence_id"]
        sentence = str(df_mturk.loc[df_mturk["sentence_id"] == sentence_id]["sentence"].values[0])
        df_results_to_rows.at[row.Index, "sentence"] = sentence


    # Write output file
    filename = "sample_dataset_mturk_no2_results_to_rows_with_sentence.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH,  "mturk", "submission_mturk_no2", "results", filename]
    output_file = os.path.join('', *output_path)
    df_results_to_rows.to_csv(output_file, sep=',', encoding='utf-8', index=False)
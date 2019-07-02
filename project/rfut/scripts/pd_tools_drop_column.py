# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

def run():

    # Load sample of threads data in dataframe
    threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "threads_summarized_rouge_1_scores.csv"]
    input_file = os.path.join('', *threads_sample_path)
    df_input = pd.read_csv(input_file)

    df_input = df_input.drop(["thread_text"], axis=1)

    # Write df_sample_dataset
    filename = "threads_summarized_rouge_1_scores_no_text.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *posts_path)
    df_input.to_csv(output_file, sep=',', encoding='utf-8', index=False) 

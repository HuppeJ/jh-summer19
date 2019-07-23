# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH



def run():

    # Load data
    input_file_name = "threads_summarized_lexrank_20_to_20_no_text.csv"
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH,"summarization", "summarization_with_sample_dataset_mturk_no2", "sentences", input_file_name]
    input_file = os.path.join("", *file_path)
    df_threads_summarized_lexrank = pd.read_csv(input_file)

    for row in df_threads_summarized_lexrank.itertuples():
        all_sentences = str(df_threads_summarized_lexrank.at[row.Index, "lexrank_20_sent"])
        list_of_sentences = all_sentences.split("\n")
        d = {}
        for i in list_of_sentences:
            if i in d.keys():
                d[i] = 1
            else:
                d[i] = 0
        total_number_of_duplicate = sum(d.values())
        df_threads_summarized_lexrank.at[row.Index, "number_of_duplicate"] = total_number_of_duplicate



    # Write 
    filename = "threads_summarized_lexrank_20_to_20_no_text_with_duplicate_count.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "summarization_with_sample_dataset_mturk_no2", "sentences", filename]
    output_file = os.path.join('', *output_path)
    df_threads_summarized_lexrank.to_csv(output_file, sep=',', encoding='utf-8', index=False) 
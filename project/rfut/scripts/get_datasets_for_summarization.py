# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from rfut.objects.sentence_parser import SentenceParser 

def run():
    print("Running : get_datasets_for_summarization")

    # Init tools 
    sp = SentenceParser()

    # Load sample of sentences data in dataframe
    mturk_sentences_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "sample_dataset_mturk_no2.csv"]
    input_file = os.path.join("", *mturk_sentences_sample_path)
    df_mturk_sentences = pd.read_csv(input_file)

    thread_ids = df_mturk_sentences["thread_id"].tolist()
    # Remove duplicates
    thread_ids = list(dict.fromkeys(thread_ids))

    # Create final df
    df_thread_text = pd.DataFrame(columns=["thread_id", "thread_text"])
    df_thread_text["thread_id"] = thread_ids

    # Load sample of threads data in dataframe
    threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "0.02-of_threads_random_sample.csv"]
    input_file = os.path.join("", *threads_sample_path)
    df_threads = pd.read_csv(input_file)

    for thread_id in thread_ids:
        thread_text = ""
        df_temp = df_threads.loc[df_threads["thread_id"] == thread_id]
        for row in df_temp.itertuples():
            post_message = str(df_temp.at[row.Index, "post_messageText"])
            post_message = sp.clean_text(post_message)
            #post_message = sp.remove_quotes_symbols(post_message)
            parsed_post_message = "\n " + post_message
            thread_text += parsed_post_message
        parsed_thread_text = thread_text[2:]
        for row in df_thread_text.itertuples():
            t_id = df_thread_text.at[row.Index, "thread_id"]
            if(t_id == thread_id):
                df_thread_text.at[row.Index, "thread_text"] = parsed_thread_text


    # Write df_sample_dataset
    filename = "threads_text_for_summarization_no2.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join("", *posts_path)
    df_thread_text.to_csv(output_file, sep=",", encoding="utf-8", index=False) 

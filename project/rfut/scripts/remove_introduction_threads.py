### Algorithm: 

# - 1. Open parsed_0.02_of_threads_to_sentences data csv file
# - 2. 
# - 3. Export the new dataframe

# Imports
import csv
import os
import re
import pandas as pd
from nltk import sent_tokenize
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from rfut.objects.sentence_parser import SentenceParser 

# Init tools 
sp = SentenceParser()

def keep_thread(thread_title, words_to_remove):
    if any(sp.is_word_in_text(word, thread_title) for word in words_to_remove):
        return False
    return True

def run(): 
    print("Running : remove_introduction_threads")
    


    # Load sample of threads data in dataframe
    parsed_threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "parsed_0.02_of_threads_to_sentences_kept_sentences.csv"]
    input_file = os.path.join('', *parsed_threads_sample_path)
    df_input = pd.read_csv(input_file)
    
    # Remove all non desired thread:
    # See function keep_thread above

    # Get the list of words that indicate that we need to remove the thread
    words_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "words_in_threads_to_remove", "words_in_threads_to_remove.csv"]
    input_file = os.path.join('', *words_path)
    df_words = pd.read_csv(input_file)
    
    words_to_remove = df_words["words"].tolist()
    print(words_to_remove)

    df_input["keep_row"] = True

    for row in df_input.itertuples():
        thread_title = str(df_input.at[row.Index, "thread_title"])
        df_input.at[row.Index, "keep_row"] = keep_thread(thread_title, words_to_remove)

    mask_kept_threads = df_input["keep_row"]
    mask_removed_threads = ~df_input["keep_row"]
    
    df_kept_threads = df_input[mask_kept_threads]
    df_removed_threads = df_input[mask_removed_threads]

    df_kept_threads = df_kept_threads.drop(["keep_row"], axis=1)
    df_removed_threads = df_removed_threads.drop(["keep_row"], axis=1)

    # Write df_kept_threads file
    filename = "parsed_0.02_of_threads_kept_threads.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *posts_path)
    df_kept_threads.to_csv(output_file, sep=',', encoding='utf-8')

    # Write df_removed_threads file
    filename = "parsed_0.02_of_threads_removed_threads.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *posts_path)
    df_removed_threads.to_csv(output_file, sep=',', encoding='utf-8')
    print("Finished")




### Algorithm: 

# - 1. Open threads_sample data csv file
# - 2. Split post_messageText into sentences
# - 3. Clean sentences text
#   - 3.1 Remove links "https?://\S+"
#   - 3.2 Replace @ references to "at"
#   - 3.3 Only keep characters matching "[^A-Za-z0-9(),!?@\'\`\"\_\n]"
# - 4. Export the dataframe with all the sentence
#       - The dataframe contains the extra info listed below:
#           ["thread_id", "thread_title", "thread_author", "post_number", "subforum_number", "sentence_number", "sentence"]

# Imports
import csv
import os
import re
import pandas as pd
from nltk import sent_tokenize
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from rfut.objects.sentence_parser import SentenceParser 

def run():
    print("Running : parse_posts_to_sentences")
    # GET SENTENCES

    # Init tools 
    sp = SentenceParser()

    # Load sample of threads data in dataframe
    threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "0.02-of_threads_random_sample.csv"]
    input_file = os.path.join('', *threads_sample_path)
    df_input = pd.read_csv(input_file)

    df_sentences = pd.DataFrame(columns=["thread_id", "thread_title", "thread_author", "post_number", "subforum_number", "sentence_number", "sentence"])

    for row in df_input.itertuples():
        thread_id = df_input.at[row.Index, "thread_id"]
        thread_title = df_input.at[row.Index, "thread_title"]
        thread_author = df_input.at[row.Index, "thread_author"]
        post_number = df_input.at[row.Index, "post_number"]
        subforum_number = df_input.at[row.Index, "subforum_number"]

        post_messageText = df_input.at[row.Index, "post_messageText"]
        sentences = sp.parse_text_to_sentences(str(post_messageText))
        sentence_number = 1
        for sentence in sentences:
            new_sentence_row = {
                "thread_id": thread_id,
                "thread_title": thread_title,
                "thread_author": thread_author,
                "post_number": post_number,
                "subforum_number": subforum_number,
                "sentence_number": sentence_number,
                "sentence": sentence,
            }
            df_sentences = df_sentences.append(new_sentence_row, ignore_index=True)
            sentence_number = sentence_number + 1


    # Write output file
    filename = "parsed_0.02_of_threads_to_sentences.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *posts_path)
    df_sentences.to_csv(output_file, sep=',', encoding='utf-8', index=False) 
    




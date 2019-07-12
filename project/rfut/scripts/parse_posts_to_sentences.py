### Algorithm: 

# - 1. Open threads_sample data csv file
# - 2. Split post_messageText into sentences
# - 3. Clean sentences text
#   - 3.1 Remove links "https?://\S+"
#   - 3.2 Only keep characters matching "[^A-Za-z0-9(),!?@\'\`\"\_\n]"
# - 4. Export the dataframe with all the sentence
#       - The dataframe contains the extra info listed below:
#           ["thread_id", "thread_title", "thread_author", "post_number", "subforum_number", "sentence_number", "sentence"]

# Imports
import csv
import os
import re
import math
import pandas as pd
from nltk import sent_tokenize
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from rfut.objects.sentence_parser import SentenceParser 

def posts_to_sentences(sp, df_input):
    df_sentences = pd.DataFrame(columns=["thread_id", "thread_title", "thread_author", "post_number", "subforum_number", "sentence_number", "sentence"])

    for row in df_input.itertuples():
        subforum_number = df_input.at[row.Index, "subforum_number"]

        # Log progress
        nb_rows = len(df_input)
        step = math.floor(nb_rows / 20)
        if (row.Index % 1000 == 0):
            step = step + step 
            progess = (row.Index / nb_rows) * 100
            print("Subforum ", subforum_number, ": ", round(progess) , r"% done.")

        thread_id = df_input.at[row.Index, "thread_id"]
        thread_title = df_input.at[row.Index, "thread_title"]
        thread_link = df_input.at[row.Index, "thread_link"]
        thread_author = df_input.at[row.Index, "thread_author"]
        thread_replies = df_input.at[row.Index, "thread_replies"]
        thread_views = df_input.at[row.Index, "thread_views"]
        post_number = df_input.at[row.Index, "post_number"]
        post_like = df_input.at[row.Index, "post_like"]

        post_messageText = str(df_input.at[row.Index, "post_messageText"])
        sentences = sp.parse_text_to_sentences(post_messageText)
        sentence_number = 1
        for sentence in sentences:
            new_sentence_row = {
                "thread_id": thread_id,
                "thread_title": thread_title,
                "thread_link": thread_link,
                "thread_author": thread_author,
                "thread_replies": thread_replies,
                "thread_views": thread_views,
                "post_number": post_number,
                "post_like": post_like,
                "subforum_number": subforum_number,
                "sentence_number": sentence_number,
                "sentence": sentence,
            }
            df_sentences = df_sentences.append(new_sentence_row, ignore_index=True)
            sentence_number = sentence_number + 1
    return df_sentences
 

def run():
    print("Running : parse_posts_to_sentences")
    # GET SENTENCES

    # Init tools 
    sp = SentenceParser()

    # Load sample of threads data in dataframe
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "0.02-of_threads_random_sample.csv"]
    input_file = os.path.join('', *file_path)
    df_input = pd.read_csv(input_file)

    df_sentences = posts_to_sentences(sp, df_input)

    # Write output file
    filename = "parsed_0.02_of_threads_to_sentences.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_sentences.to_csv(output_file, sep=',', encoding='utf-8', index=False) 
    




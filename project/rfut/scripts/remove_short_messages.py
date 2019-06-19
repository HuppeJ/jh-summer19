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


# Remove sentence:
# - with 0, 1 or 2 alnum characters
# - that have 1 words and no question mark (?)
# - that are matching one of the short_sentences_to_remove (see below)
def remove_sentence(sentence, nb_alnum_characters, nb_words, short_sentences_to_remove):
    if nb_alnum_characters <= 2:
        return True
    if nb_words == 1 and "?" in sentence:
        return True
    if any(substring in sentence for substring in short_sentences_to_remove):
        return True
    
    return False

def run(): 
    print("Running : remove_short_messages")
    
    # Init tools 
    sp = SentenceParser()

    # Load sample of threads data in dataframe
    parsed_threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "parsed_0.02_of_threads_to_sentences.csv"]
    input_file = os.path.join('', *parsed_threads_sample_path)
    df_input = pd.read_csv(input_file)
    
    # Only keep rows with messages that have more than 2 word
    df_with_stats = df_input.copy()

    # Adding nb of characters for each sentences
    df_with_stats["nb_alnum_characters"] = 0
    for row in df_with_stats.itertuples():
        sentence = str(df_with_stats.at[row.Index, "sentence"])
        nb_char = sp.alnum_count(sentence)
        df_with_stats.at[row.Index, "nb_alnum_characters"] = nb_char

    # Adding nb of words for each sentences
    df_with_stats["nb_words"] = 0
    for row in df_with_stats.itertuples():
        sentence = str(df_with_stats.at[row.Index, "sentence"])
        nb_words = sp.word_count(sentence)
        df_with_stats.at[row.Index, "nb_words"] = nb_words

    # Write df_with_stats file
    filename = "parsed_0.02_of_threads_to_sentences_with_stats.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *posts_path)
    df_with_stats.to_csv(output_file, sep=',', encoding='utf-8')     

    # Write df_with_stats file sorted by nb_char
    df_with_stats_sorted_by_nb_char = df_with_stats.copy()
    df_with_stats_sorted_by_nb_char = df_with_stats_sorted_by_nb_char.sort_values(by = ["nb_alnum_characters"])
    filename = "parsed_0.02_of_threads_to_sentences_with_stats_sorted_by_nb_char.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *posts_path)
    df_with_stats_sorted_by_nb_char.to_csv(output_file, sep=',', encoding='utf-8')

    # Write df_with_stats file sorted by nb_words
    df_with_stats_sorted_by_nb_words= df_with_stats.copy()
    df_with_stats_sorted_by_nb_words= df_with_stats_sorted_by_nb_words.sort_values(by = ["nb_words"])
    filename = "parsed_0.02_of_threads_to_sentences_with_stats_sorted_by_nb_words.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *posts_path)
    df_with_stats_sorted_by_nb_words.to_csv(output_file, sep=',', encoding='utf-8')

    # Remove all non desired sentences:
    # See function remove_sentence above
    short_sentences_to_remove = ["Click to expand"]

    df_with_stats_parsed = df_with_stats.copy()
    df_with_stats_parsed["remove_row"] = False
    for row in df_with_stats_parsed.itertuples():
        sentence = str(df_with_stats_parsed.at[row.Index, "sentence"])
        nb_alnum_characters = int(df_with_stats_parsed.at[row.Index, "nb_alnum_characters"])
        nb_words = int(df_with_stats_parsed.at[row.Index, "nb_words"])
        df_with_stats_parsed.at[row.Index, "remove_row"] = remove_sentence(sentence, nb_alnum_characters, nb_words, short_sentences_to_remove)

    mask_removed_sentences = df_with_stats_parsed["remove_row"]
    mask_kept_sentences = ~df_with_stats_parsed["remove_row"]
    
    df_with_stats_removed_sentences = df_with_stats_parsed[mask_removed_sentences]
    df_with_stats_kept_sentences = df_with_stats_parsed[mask_kept_sentences]

    df_with_stats_removed_sentences = df_with_stats_removed_sentences.drop(["remove_row"], axis=1)
    df_with_stats_kept_sentences = df_with_stats_kept_sentences.drop(["remove_row"], axis=1)

    # Write df_with_stats_removed_sentences file
    filename = "parsed_0.02_of_threads_to_sentences_removed_sentences.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *posts_path)
    df_with_stats_removed_sentences.to_csv(output_file, sep=',', encoding='utf-8')

    # Write df_with_stats_kept_sentences file
    filename = "parsed_0.02_of_threads_to_sentences_kept_sentences.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *posts_path)
    df_with_stats_kept_sentences.to_csv(output_file, sep=',', encoding='utf-8')
    print("Finished")




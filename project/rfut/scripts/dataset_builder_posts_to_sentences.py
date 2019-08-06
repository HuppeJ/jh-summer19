### Algorithm: 

# - 1. For all the selected subforum (all i.csv selected (see subforum_updated_classified.csv)):
# - 1.1 Parse all the posts in the file i.csv to sentences
# - 1.2 Write the new dataset which contains all the data of the i.csv file, but in sentence format instead of post format

import os
import pandas as pd
import math
from rfut.objects.sentence_parser import SentenceParser 
from rfut.common.constants import DIABETES_DATA_PATH, SUBORUMS_DATA_PATH, POSTS_DATA_PATH, PROJECT_PATH, DATA_OUTPUT_PATH
from rfut.scripts.parse_posts_to_sentences import posts_to_sentences

def run():
    print("Running : dataset_builder_posts_to_sentences")
    # Init tools 
    sp = SentenceParser()

    # Load subforum data in dataframe
    subforum_path = [DIABETES_DATA_PATH, SUBORUMS_DATA_PATH, "subforum_updated_classified.csv"]
    subforum_file = os.path.join('', *subforum_path)
    df_subforum = pd.read_csv(subforum_file)

    # Declare column constants
    POST_THREAD_ID_COLUMN = "thread_id"
    POST_SUBFORUM_NUMBER = "subforum_number"
    SUBFORUM_IS_SELECTED_COLUMN = "subforum_is_selected"
    SUBFORUM_NUMBER_COLUMN = "subforum_number"

    # Get the selected subforums
    selected_subforums = set()
    for row in df_subforum.itertuples():
        is_selected = bool(df_subforum.at[row.Index, SUBFORUM_IS_SELECTED_COLUMN])
        if is_selected:
            subforum_number = int(df_subforum.at[row.Index, SUBFORUM_NUMBER_COLUMN])
            selected_subforums.add(subforum_number)

    print("selected_subforums", selected_subforums)

    posts_path = [DIABETES_DATA_PATH, POSTS_DATA_PATH]
    posts_directory = os.path.join('', *posts_path)
    i = 0 
    for subdir, dirs, files in os.walk(posts_directory):
        for file in files:
            fileInput = subdir + os.sep + file
            if fileInput.endswith(".csv"):
                subforum_num = int(file[:-4])
                if subforum_num in selected_subforums:
                    df_input = pd.read_csv(fileInput, dtype=str)
                    df_input_copy = df_input.copy()
                    df_input_copy[POST_SUBFORUM_NUMBER] = subforum_num
                    df_sentences = posts_to_sentences(sp, df_input_copy)
                        
                    filename = str(subforum_num) + "_posts_to_sentences.csv"
                    output_file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "posts_to_sentences", filename]
                    output_file = os.path.join('', *output_file_path)
                    df_sentences.to_csv(output_file, sep=',', encoding='utf-8', index=False)   



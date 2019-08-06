### Algorithm: 

# - 1. For all the selected subforum (all i.csv selected (see subforum_updated_classified.csv)):
# - 1.1 Extract all the first posts (post_number == #1)
# - 2. Write the new dataset in csv file

import os
import pandas as pd
import math
from rfut.objects.sentence_parser import SentenceParser 
from rfut.common.constants import DIABETES_DATA_PATH, SUBORUMS_DATA_PATH, POSTS_DATA_PATH, PROJECT_PATH, DATA_OUTPUT_PATH
from rfut.scripts.parse_posts_to_sentences import posts_to_sentences

def run():
    print("Running : dataset_builder_first_posts")

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
   
    df_output = pd.DataFrame()
    post_number_to_select = "#1"

    posts_path = [DIABETES_DATA_PATH, POSTS_DATA_PATH]
    posts_directory = os.path.join('', *posts_path)

    for subdir, dirs, files in os.walk(posts_directory):
        for file in files:
            fileInput = subdir + os.sep + file
            if fileInput.endswith(".csv"):
                subforum_num = int(file[:-4])
                if subforum_num in selected_subforums:
                    print("Subforum ", subforum_num)
                    df_input = pd.read_csv(fileInput, dtype=str)
                    df_input_copy = df_input.copy()
                    df_input_copy[POST_SUBFORUM_NUMBER] = subforum_num
                    df_selection = df_input_copy.loc[df_input_copy["post_number"] == post_number_to_select]
                    df_output = df_output.append(df_selection)

    filename = "dataset_first_posts.csv"
    output_file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_file_path)
    df_output.to_csv(output_file, sep=',', encoding='utf-8', index=False)   



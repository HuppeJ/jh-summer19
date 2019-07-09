### Algorithm: 

# - 1. Load subforums data
# - 2. Get the selected subforums
# - 3. For each posts data of the selected subforums:
#   - 3.1 Remove duplicated thread_id
#   - 3.2 Select x% of the new column with no duplicated thread_id
#   - 3.3 Select all the post matching the selected thread_ids
#   - 3.4 Add the colum subforum_number to each post 
#   - 3.5 Append the new rows to the output dataframe
# - 4. Write the output dataframe in .csv file

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

    # TODO: to comment
    selected_subforums = [1]

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
                    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "posts_to_sentences", filename]
                    output_file = os.path.join('', *posts_path)
                    df_sentences.to_csv(output_file, sep=',', encoding='utf-8', index=False)   



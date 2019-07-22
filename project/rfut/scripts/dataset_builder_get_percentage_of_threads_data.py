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
from rfut.common.constants import DIABETES_DATA_PATH, SUBORUMS_DATA_PATH, POSTS_DATA_PATH, PROJECT_PATH, DATA_OUTPUT_PATH

def run():
    print("Running : dataset_builder_get_percentage_of_threads_data")

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

    # Sample x% of threads in each selected subforum
    percentage_of_threads_to_select = 0.02
    df_output = pd.DataFrame()

    posts_path = [DIABETES_DATA_PATH, POSTS_DATA_PATH]
    posts_directory = os.path.join('', *posts_path)
    i = 0 
    nb_subforum_added = 0
    for subdir, dirs, files in os.walk(posts_directory):
        for file in files:
            fileInput = subdir + os.sep + file
            if fileInput.endswith(".csv"):
                subforum_num = int(file[:-4])
                if subforum_num in selected_subforums:
                    df_input = pd.read_csv(fileInput)
                    df_input_copy = df_input.copy()
                    df_input_copy = df_input_copy.drop_duplicates('thread_id')
                    nb_threads = len(df_input_copy)
                    nb_threads_to_select = math.floor(percentage_of_threads_to_select * nb_threads)
                    print("subforum_num:", subforum_num, "nb_threads:", nb_threads)
                    sample = df_input_copy.sample(nb_threads_to_select)
                    thread_id_sample_list = sample[POST_THREAD_ID_COLUMN].tolist()
                    # add tag to posts to which subforum
                    df_sample = df_input.loc[df_input[POST_THREAD_ID_COLUMN].isin(thread_id_sample_list)]
                    df_sample[POST_SUBFORUM_NUMBER] = subforum_num
                    df_output = df_output.append(df_sample)
                    nb_subforum_added = nb_subforum_added + 1


    print("len(selected_subforums)", len(selected_subforums))
    print("nb_subforum_added", nb_subforum_added)
    # Write output file
    filename = str(percentage_of_threads_to_select) + "-of_threads_random_sample_2.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_output.to_csv(output_file, sep=',', encoding='utf-8', index=False)     




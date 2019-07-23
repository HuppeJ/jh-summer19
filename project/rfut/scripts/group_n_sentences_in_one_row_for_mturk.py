# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH


def update_row_data_dict(df_input, row, row_data_dict, sentence_count):
    # Get the sentence_id and sentence from df_input
    sentence_id = str(df_input.at[row.Index, "sentence_id"])
    sentence = str(df_input.at[row.Index, "sentence"])

    # Get the sentence_id_colum and sentence_colum
    sentence_id_colum = "sentence" + str(sentence_count) +"_id"
    sentence_colum = "sentence" + str(sentence_count)

    # Add retrivied info in row_data_dict
    row_data_dict[sentence_id_colum] = sentence_id
    row_data_dict[sentence_colum] = sentence

    return row_data_dict

def run():
    # Load data
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "sample_dataset_mturk_no2_with_sentence_ids.csv"]
    input_file = os.path.join('', *file_path)
    df_input = pd.read_csv(input_file)

    df_output = pd.DataFrame()
    number_of_sentences_in_each_group = 5

    # group_number : groupe represent a group of sentences
    # group_number goes from 1 to 2100 (2100 comes from 10500/5 = 2100)

    
    group_count = 1
    sentence_count = 1
    row_data_dict = {}

    for row in df_input.itertuples():
        # Check if there is still place to add sentence in a row
        if sentence_count < number_of_sentences_in_each_group:
            # Update row data dict with the new added sentence
            row_data_dict = update_row_data_dict(df_input, row, row_data_dict, sentence_count)
            
            # Increment nb of sentences
            sentence_count = sentence_count + 1
        else: 
            # Add group_number
            row_data_dict["group_number"] = group_count
            
            # Update row data dict with the new added sentence
            row_data_dict = update_row_data_dict(df_input, row, row_data_dict, sentence_count)

            # Created dataframe from row_data_dict
            df_temp = pd.DataFrame(row_data_dict, index=[group_count])
            
            # Add df_temp to df_output
            df_output = df_output.append(df_temp)
            
            # Reset row_data_dict
            row_data_dict = {}
                
            # Increment group_count
            group_count = group_count + 1
            # Reset the number of sentences for the next group
            sentence_count = 1


    df_output = df_output.reindex(sorted(df_output.columns), axis=1)
        
    # Write df_sample_dataset
    filename = "sample_dataset_mturk_no2_group_of_" + str(number_of_sentences_in_each_group) + "_sent.csv"
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *file_path)
    df_output.to_csv(output_file, sep=',', encoding='utf-8', index=False)
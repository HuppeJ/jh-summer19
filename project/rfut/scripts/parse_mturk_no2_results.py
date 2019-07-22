# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

def get_answer(df_results, row_index, sentence_number):
    yes = df_results.at[row_index, "Answer.answer_sentence"+ str(sentence_number) + "_yes.Yes"]
    no = df_results.at[row_index, "Answer.answer_sentence"+ str(sentence_number) + "_no.No"]
    cd = df_results.at[row_index, "Answer.answer_sentence"+ str(sentence_number) + "_cd.Cannot Determine"]
    
    if yes and not no and not cd:
        return "yes"
    elif no and not yes and not cd:
        return "no"
    elif cd and not yes and not no:
        return "cd"
    else:
        print("Invalid value with: ", df_results.at[row_index, "Input.sentence"+ str(sentence_number) + "_id"])
        return "invalid_value"

def run():

    # Load data
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "sample_dataset_mturk_no2_with_sentence_ids.csv"]
    input_file = os.path.join('', *file_path)
    df_mturk = pd.read_csv(input_file)
    df_output = df_mturk.copy()

    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "sample_dataset_mturk_no2_results.csv"]
    input_file = os.path.join('', *file_path)
    df_results = pd.read_csv(input_file)

    number_of_sentences_in_each_group = 5
    sentence_numbers = range(1, number_of_sentences_in_each_group + 1)

    sentences_results = {}

    for row in df_results.itertuples():
        for sentence_number in sentence_numbers:

            sentence_id  = df_results.at[row.Index, "Input.sentence"+ str(sentence_number) + "_id"]
            assignment_id = df_results.at[row.Index, "AssignmentId"]
            worker_id = df_results.at[row.Index, "WorkerId"]
            worker_life_time_approval_rate = df_results.at[row.Index, "LifetimeApprovalRate"]
            worker_last_30_days_approval_rate = df_results.at[row.Index, "Last30DaysApprovalRate"]
            worker_last_7_days_approval_rate = df_results.at[row.Index, "Last7DaysApprovalRate"]
            sentence_group_number = df_results.at[row.Index, "Input.group_number"]
            expresses_a_need = get_answer(df_results, row.Index, sentence_number)

            result = {
                "assignment_id": assignment_id, 
                "worker_id": worker_id, 
                "worker_life_time_approval_rate": worker_life_time_approval_rate, 
                "worker_last_30_days_approval_rate": worker_last_30_days_approval_rate, 
                "worker_last_7_days_approval_rate": worker_last_7_days_approval_rate, 
                "sentence_group_number": sentence_group_number, 
                "expresses_a_need": expresses_a_need, 
            }

            sentences_results[sentence_id] = result

    df_output["assignment_id"] = "no_value"
    df_output["worker_id"] = "no_value"
    df_output["worker_life_time_approval_rate"] = "no_value"
    df_output["worker_last_30_days_approval_rate"] = "no_value"
    df_output["worker_last_7_days_approval_rate"] = "no_value"
    df_output["sentence_group_number"] = "no_value"
    df_output["expresses_a_need"] = "no_value"
    for row in df_mturk.itertuples():
        sentence_id = df_mturk.at[row.Index, "sentence_id"]
        if sentence_id in sentences_results:
            df_output.at[row.Index, "assignment_id"] = sentences_results[sentence_id]["assignment_id"]
            df_output.at[row.Index, "worker_id"] = sentences_results[sentence_id]["worker_id"]
            df_output.at[row.Index, "worker_life_time_approval_rate"] = sentences_results[sentence_id]["worker_life_time_approval_rate"]
            df_output.at[row.Index, "worker_last_30_days_approval_rate"] = sentences_results[sentence_id]["worker_last_30_days_approval_rate"]
            df_output.at[row.Index, "worker_last_7_days_approval_rate"] = sentences_results[sentence_id]["worker_last_7_days_approval_rate"]
            df_output.at[row.Index, "sentence_group_number"] = sentences_results[sentence_id]["sentence_group_number"]
            df_output.at[row.Index, "expresses_a_need"] = sentences_results[sentence_id]["expresses_a_need"]


    # Write output file
    filename = "sample_dataset_mturk_no2_with_results.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_output.to_csv(output_file, sep=',', encoding='utf-8', index=False)
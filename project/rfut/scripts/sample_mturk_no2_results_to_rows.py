# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

def get_answer(sentence_id, sentence_number, yes, no, cd):
    if yes and not no and not cd:
        return "yes"
    elif no and not yes and not cd:
        return "no"
    elif cd and not yes and not no:
        return "cd"
    else:
        print("Invalid value with: ", sentence_id, " yes: ", yes, " no: ", no, " cd: ", cd)
        return "invalid_value"

def run():

    # Load data
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "mturk", "submission_mturk_no2", "results", "Batch_3719368_batch_results.csv"]
    input_file = os.path.join('', *file_path)
    df_results = pd.read_csv(input_file)
    df_output = pd.DataFrame()

    number_of_sentences_in_each_group = 5
    sentence_numbers = range(1, number_of_sentences_in_each_group + 1)

    sentences_results = {}

    df_output["sentence_id"] = "no_value"
    df_output["assignment_id"] = "no_value"
    df_output["worker_id"] = "no_value"
    df_output["worker_life_time_approval_rate"] = "no_value"
    df_output["worker_last_30_days_approval_rate"] = "no_value"
    df_output["worker_last_7_days_approval_rate"] = "no_value"
    df_output["sentence_group_number"] = "no_value"
    df_output["yes"] = "no_value"
    df_output["no"] = "no_value"
    df_output["cd"] = "no_value"
    df_output["expresses_a_need"] = "expresses_a_need"

    for row in df_results.itertuples():
        for sentence_number in sentence_numbers:
            sentence_id  = df_results.at[row.Index, "Input.sentence"+ str(sentence_number) + "_id"]
            assignment_id = df_results.at[row.Index, "AssignmentId"]
            worker_id = df_results.at[row.Index, "WorkerId"]
            worker_life_time_approval_rate = df_results.at[row.Index, "LifetimeApprovalRate"]
            worker_last_30_days_approval_rate = df_results.at[row.Index, "Last30DaysApprovalRate"]
            worker_last_7_days_approval_rate = df_results.at[row.Index, "Last7DaysApprovalRate"]
            sentence_group_number = df_results.at[row.Index, "Input.group_number"]
            yes = df_results.at[row.Index, "Answer.answer_sentence"+ str(sentence_number) + "_yes.Yes"]
            no = df_results.at[row.Index, "Answer.answer_sentence"+ str(sentence_number) + "_no.No"]
            cd = df_results.at[row.Index, "Answer.answer_sentence"+ str(sentence_number) + "_cd.Cannot Determine"]
            expresses_a_need = get_answer(sentence_id, sentence_number, yes, no, cd)

            result = {
                "sentence_id": sentence_id, 
                "assignment_id": assignment_id, 
                "worker_id": worker_id, 
                "worker_life_time_approval_rate": worker_life_time_approval_rate, 
                "worker_last_30_days_approval_rate": worker_last_30_days_approval_rate, 
                "worker_last_7_days_approval_rate": worker_last_7_days_approval_rate, 
                "sentence_group_number": sentence_group_number, 
                "yes": yes,
                "no": no,
                "cd": cd,
                "expresses_a_need": expresses_a_need,
            }

            df_output = df_output.append(result, ignore_index=True)



    # Write output file
    filename = "sample_dataset_mturk_no2_results_to_rows.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH,  "mturk", "submission_mturk_no2", "results", filename]
    output_file = os.path.join('', *output_path)
    df_output.to_csv(output_file, sep=',', encoding='utf-8', index=False)
# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

# Answers to Group Label:
# 1 : yes yes yes 
# 2 : yes yes x 
# 3 : no no no 
# 4 : no no x 
# 5 : cd cd cd
# 6 : cd cd x 
# 7 : yes no cd 

# Where: 
# x: is any value

# So 
# Group Label 1, 3, 5 are answers where all workers agreed on the label
# Group Label 2, 4, 6, 7 are answers where workers disagreed on the label


def get_grouped_result(df_sentence_results): 
    yes_count = df_sentence_results.count("yes")
    no_count = df_sentence_results.count("no")
    cd_count = df_sentence_results.count("cd")

    if yes_count == 3:
        return 1
    if yes_count == 2:
        return 2
    if no_count == 3:
        return 3
    if no_count == 2:
        return 4
    if cd_count == 3:
        return 5
    if cd_count == 2:
        return 6
    else: 
        return 7

def run():
    # Load data
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "mturk", "submission_mturk_no2", "results", "sample_dataset_mturk_no2_results_to_rows_with_sentence_and_invalid_values_labelled.csv"]
    input_file = os.path.join("", *file_path)
    df_results_to_rows = pd.read_csv(input_file)


    df_output = df_results_to_rows[["sentence_id"]].copy()
    df_output = df_output.drop_duplicates(subset="sentence_id", keep="last")
    
    for row in df_output.itertuples():
        sentence_id = df_output.at[row.Index, "sentence_id"]

        selected_rows = df_results_to_rows.loc[df_results_to_rows["sentence_id"] == sentence_id]
        df_sentence_results = list(selected_rows["expresses_a_need"].values)

        df_output.at[row.Index, "sentence_id"] = sentence_id
        df_output.at[row.Index, "assignment_id"] = selected_rows["assignment_id"].values[0]
        df_output.at[row.Index, "worker_id"] = selected_rows["worker_id"].values[0]
        df_output.at[row.Index, "worker_life_time_approval_rate"] = selected_rows["worker_life_time_approval_rate"].values[0]
        df_output.at[row.Index, "worker_last_30_days_approval_rate"] = selected_rows["worker_last_30_days_approval_rate"].values[0]
        df_output.at[row.Index, "worker_last_7_days_approval_rate"] = selected_rows["worker_last_7_days_approval_rate"].values[0]
        df_output.at[row.Index, "sentence_group_number"] = selected_rows["sentence_group_number"].values[0]
        df_output.at[row.Index, "expresses_a_need_grouped"] = get_grouped_result(df_sentence_results)
        df_output.at[row.Index, "sentence"] = selected_rows["sentence"].values[0]


    # Write output file
    filename = "sample_mturk_no2_results_grouped.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH,  "mturk", "submission_mturk_no2", "results", filename]
    output_file = os.path.join("", *output_path)
    df_output.to_csv(output_file, sep=",", encoding="utf-8", index=False)
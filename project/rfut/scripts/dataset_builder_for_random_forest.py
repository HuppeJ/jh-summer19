# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

# New labels:
# expresses_a_need_grouped: 1 & 2 are mapped to expresses_a_need_final: 1
# expresses_a_need_grouped: 3 & 4 are mapped to expresses_a_need_final: 2

def run():
    # Load data
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "mturk", "submission_mturk_no2", "results", "sample_dataset_mturk_no2_merged_results.csv"]
    input_file = os.path.join("", *file_path)
    df_input = pd.read_csv(input_file)


    df_yes = df_input.loc[(df_input["expresses_a_need_grouped"]==1) | (df_input["expresses_a_need_grouped"] == 2)]

    df_yes["expresses_a_need_final"] = 1

    df_no = df_input.loc[(df_input["expresses_a_need_grouped"]==3) | (df_input["expresses_a_need_grouped"] == 4)]

    df_no["expresses_a_need_final"] = 0

    df_yes = df_yes.append(df_no, ignore_index=True)


    # Write output file
    filename = "dataset_for_random_forest.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH,  "mturk", "submission_mturk_no2", "results", filename]
    output_file = os.path.join("", *output_path)
    df_yes.to_csv(output_file, sep=",", encoding="utf-8", index=False)
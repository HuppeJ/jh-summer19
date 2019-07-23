# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

def run():

    # Load data
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "sample_dataset_mturk_no1.csv"]
    input_file = os.path.join('', *file_path)
    df_input = pd.read_csv(input_file)

    df_input_1 = df_input.iloc[0:1000]
    df_input_2 = df_input.iloc[1000:10600]

    # Write df_sample_dataset
    filename = "sample_0_to_999_dataset_mturk_no1.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_input_1.to_csv(output_file, sep=',', encoding='utf-8', index=False) 

    # Write df_sample_dataset
    filename = "sample_1000_to_10500_dataset_mturk_no1.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_input_2.to_csv(output_file, sep=',', encoding='utf-8', index=False)
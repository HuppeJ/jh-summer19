# Imports
import os
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

def run():

    # Load data
    input_file_name = "threads_summarized_lexrank_20_to_20_no_text_to_sentences.csv"
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH,"summarization", "summarization_with_sample_dataset_mturk_no2", "sentences", input_file_name]
    input_file = os.path.join('', *file_path)
    df_input = pd.read_csv(input_file)

    # Create sample datasets 
    # Should only be runned once
    sample_df_summary_sentences = df_input.sample(3500)
    
    # Write df_sample_dataset
    filename = "sample_summary_sentences_no2.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "summarization_with_sample_dataset_mturk_no2", "sentences", filename]
    output_file = os.path.join('', *output_path)
    sample_df_summary_sentences.to_csv(output_file, sep=',', encoding='utf-8') 

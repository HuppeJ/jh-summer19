# Imports
import os
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH



def run():

    # Load data
    input_file_name = "threads_summarized_lexrank_20_to_20_no_text.csv"
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH,"summarization", "summarization_with_sample_dataset_mturk_no2", "sentences", input_file_name]
    input_file = os.path.join("", *file_path)
    df_threads_summarized_lexrank = pd.read_csv(input_file)

    df_sentences = pd.DataFrame()


    for row in df_threads_summarized_lexrank.itertuples():
        thread_id = df_threads_summarized_lexrank.at[row.Index, "thread_id"]
        sentence_number = 1
        all_sentences = str(df_threads_summarized_lexrank.at[row.Index, "lexrank_20_sent"])
        list_of_sentences = all_sentences.split("\n")

        for sentence in list_of_sentences:
            new_sentence_row = {
                "thread_id": thread_id,
                "sentence_number": sentence_number,
                "sentence": sentence,
            }
            df_sentences = df_sentences.append(new_sentence_row, ignore_index=True)

            sentence_number = sentence_number + 1



    # Write 
    filename = "threads_summarized_lexrank_20_to_20_no_text_to_sentences.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "summarization_with_sample_dataset_mturk_no2", "sentences", filename]
    output_file = os.path.join('', *output_path)
    df_sentences.to_csv(output_file, sep=',', encoding='utf-8', index=False) 
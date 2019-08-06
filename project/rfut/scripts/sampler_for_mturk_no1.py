# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH

def run():

    # Load data
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "parsed_0.02_kept_threads_with_is_question_and_annotations.csv"]
    input_file = os.path.join('', *file_path)
    df_input = pd.read_csv(input_file)

    mask_questions = df_input["is_question"]
    df_questions = df_input[mask_questions]

    mask_annotations = df_input["has_annotations"]
    df_annotations = df_input[mask_annotations]

    mask_none = ~(mask_questions | mask_annotations)
    df_none = df_input[mask_none]

    nb_questions = len(df_questions)
    nb_annotations = len(df_annotations)
    nb_none = len(df_none)

    # Separate the dataset in three groups
    # 1: All question sentences
    # 2: Sentences with annotations that are not in question form
    # 3: All other sentences

    mask_annotations_without_questions = mask_annotations & ~mask_questions
    df_annotations_without_questions = df_input[mask_annotations_without_questions]
    nb_annotations_without_questions = len(df_annotations_without_questions)


    mask_annotations_with_questions = mask_annotations & mask_questions
    df_annotations_with_questions = df_input[mask_annotations_with_questions]
    nb_annotations_with_questions = len(df_annotations_with_questions)


    # Write output files
    filename = "all_question_sentences_mturk_no2.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_questions.to_csv(output_file, sep=',', encoding='utf-8', index=False) 

    filename = "all_annotations_without_questions_sentences_mturk_no2.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_annotations_without_questions.to_csv(output_file, sep=',', encoding='utf-8', index=False) 

    filename = "all_other_sentences_mturk_no2.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_none.to_csv(output_file, sep=',', encoding='utf-8', index=False)

    print("")
    print("Separate the dataset in three groups:")
    print("- 1: All question sentences")
    print("- 2: Sentences with annotations that are not in question form")
    print("- 3: All other sentences")

    print("")
    
    print("Nb. of question sentences", nb_questions)
    print("Nb. of sentences with annotations that are not in question form", nb_annotations_without_questions)
    print("Nb. of sentences that are not questions and have no annotations", nb_none)
    print("Total: ", nb_questions + nb_annotations_without_questions + nb_none)
    print("")
    print("Additional info:")
    print("")
    print("Nb. of sentences with annotations", nb_annotations)
    print("Nb. of sentences with annotations that are in question form", nb_annotations_with_questions)

    # Create sample datasets 
    # Should only be runned once
    sample_df_questions = df_questions.sample(3500)
    sample_df_annotations_without_questions = df_annotations_without_questions.sample(3500)
    sample_df_none = df_none.sample(3500)
    
    sample_df_annotations_without_questions_and_df_none = sample_df_annotations_without_questions.append(sample_df_none)
    df_sample_dataset = sample_df_annotations_without_questions_and_df_none.append(sample_df_questions)    
    
    # Write df_sample_dataset
    filename = "[No_overwrite]sample_dataset_mturk_no2.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_sample_dataset.to_csv(output_file, sep=',', encoding='utf-8') 

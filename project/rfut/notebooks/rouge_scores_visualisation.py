#%%
# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH, IMG_OUTPUT_PATH
import numpy as np
import matplotlib.pyplot as plt 

# Init dictionary
data = {}

def export_graph_as_pdf(plt, filename):
    file_name = filename
    file_path = [PROJECT_PATH, IMG_OUTPUT_PATH, file_name]
    file = os.path.join("", *file_path)
    plt.savefig(file)


def get_scores_means_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences): 
    return "scores_means_" + summarization_technique + "_" + score_technique + "_" + str(min_nb_sentences) + "_to_" + str(max_nb_sentences)

def get_nb_sentences_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences):
    return "nb_sentences_" + summarization_technique + "_" + score_technique + "_" + str(min_nb_sentences) + "_to_" + str(max_nb_sentences)

summarization_techniques = ["sumbasic", "lexrank", "textrank"]
score_techniques = ["rouge_1", "rouge_2", "rouge_3", "rouge_4"]

def load_data_in_data_object(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences):
    input_file_name = "threads_summarized_" + summarization_technique + "_" + score_technique + "_scores_" + str(min_nb_sentences) + "_to_" + str(max_nb_sentences) + ".csv"

    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "summarization_with_sample_dataset_mturk_no1", "sentences", input_file_name]
    input_file = os.path.join("", *file_path)
    df_input = pd.read_csv(input_file)

    scores_means = []
    nb_sentences = []
    for nb_sentence in range(min_nb_sentences, max_nb_sentences + 1):
        nb_sentences.append(nb_sentence)
        score_column = summarization_technique + "_" + str(nb_sentence) + "_sent" + "_" + score_technique
        scores_means.append(df_input[score_column].mean())

    # Keep data in dictionary "data" to create graphs with multiple lines
    scores_means_key = get_scores_means_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences)
    data[scores_means_key] = scores_means
    nb_sentences_key = get_nb_sentences_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences)
    data[nb_sentences_key] = nb_sentences

sumy_score_techniques = ["rouge_2", "rouge_3"]
def load_sumy_texrank_data_in_data_object(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences):
    input_file_name = "threads_summarized_" + summarization_technique + "_sumy_" + score_technique + "_scores_" + str(min_nb_sentences) + "_to_" + str(max_nb_sentences) + ".csv"

    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "summarization_with_sample_dataset_mturk_no1", "sentences", input_file_name]
    input_file = os.path.join("", *file_path)
    df_input = pd.read_csv(input_file)

    scores_means = []
    nb_sentences = []
    for nb_sentence in range(min_nb_sentences, max_nb_sentences + 1):
        nb_sentences.append(nb_sentence)
        score_column = summarization_technique + "_" + str(nb_sentence) + "_sent" + "_" + score_technique
        scores_means.append(df_input[score_column].mean())

    # Keep data in dictionary "data" to create graphs with multiple lines
    scores_means_key = "sumy_" + get_scores_means_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences)
    data[scores_means_key] = scores_means
    nb_sentences_key = "sumy_" + get_nb_sentences_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences)
    data[nb_sentences_key] = nb_sentences

#%% 
# Loading the data in the data object for plotting graphs
min_nb_sentences = 1
max_nb_sentences = 50

for summarization_technique in summarization_techniques:
    for score_technique in score_techniques:
        load_data_in_data_object(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences)


for score_technique in sumy_score_techniques:
    load_sumy_texrank_data_in_data_object("textrank", score_technique, min_nb_sentences, max_nb_sentences)


#%%
# Plot all summarization techniques with all Rouge scores in function of the nb. of sentences
for summarization_technique in summarization_techniques:
    for score_technique in score_techniques:
        scores_means_key = get_scores_means_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences)
        nb_sentences_key = get_nb_sentences_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences)

        # Plot graph
        x = data[nb_sentences_key]
        y = data[scores_means_key]
        
        plt.plot(x, y, color="green", linestyle="dashed", linewidth = 1, marker=".", markerfacecolor="blue") 

        plt.xlim(min_nb_sentences - 1, max_nb_sentences + 1) 
        plt.ylim(0,1) 

        plt.title(summarization_technique.upper() + ": " + score_technique.upper() + " scores in function of the nb. of sentences") 
        plt.xlabel("Nb. of sentences") 
        plt.ylabel(score_technique.upper() + " score") 
        
        plt.show()
#%%

for score_technique in score_techniques:
    for summarization_technique in summarization_techniques:
        scores_means_key = get_scores_means_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences)
        nb_sentences_key = get_nb_sentences_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences)
        plt.plot(data[nb_sentences_key], data[scores_means_key], linestyle="dashed", linewidth = 1, marker=".") 

    if summarization_technique == "textrank":
        if score_technique in sumy_score_techniques:
            sumy_scores_means_key = "sumy_" + get_scores_means_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences)
            sumy_nb_sentences_key = "sumy_" + get_nb_sentences_key(summarization_technique, score_technique, min_nb_sentences, max_nb_sentences)

            #plt.plot(data[sumy_nb_sentences_key], data[sumy_scores_means_key], linestyle="dashed", linewidth = 1, marker=".") 

    plt.xlim(min_nb_sentences - 1, max_nb_sentences + 1) 
    plt.ylim(0,1) 

    # plt.title(score_technique.upper() + " scores in function \n of the number of sentences in the summary") 
    plt.xlabel("Number of sentences in the summary") 
    plt.ylabel(score_technique.upper() + " score") 
    
    legend = summarization_techniques
    if summarization_technique == "textrank":
        if score_technique in sumy_score_techniques:
            legend = summarization_techniques + ["sumy_textrank"]

    plt.legend(legend, loc='lower right')

    if score_technique == "rouge_2":
        plt.ylabel("Average ROUGE-2 score") 
        export_graph_as_pdf(plt, "rouge_2_scores_in_function_of_the_number_of_sentences_in_the_summary.pdf")

    plt.show()







#%%



#%%

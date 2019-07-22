#%%
# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH, IMG_OUTPUT_PATH
import numpy as np
import matplotlib.pyplot as plt 
from rfut.objects.thread_analyser import ThreadAnalyzer 
from rfut.objects.sentence_parser import SentenceParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from matplotlib.ticker import FormatStrFormatter

def export_graph_as_pdf(plt, filename):
    file_name = filename
    file_path = [PROJECT_PATH, IMG_OUTPUT_PATH, file_name]
    file = os.path.join("", *file_path)
    plt.savefig(file)

    
# Init tools 
ta = ThreadAnalyzer()
sp = SentenceParser()

# Load sample_dataset_mturk_no2 (First dataset ready to sumbit to mturk)
input_file_name_1 = "sample_dataset_mturk_no12.csv"
threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "check_stat_nb_sent_in_mturk_and_sum_datasets", input_file_name_1]
input_file = os.path.join("", *threads_sample_path)
df_dataset_mturk_no2 = pd.read_csv(input_file)

#"check_stat_nb_sent_in_mturk_and_sum_datasets",

# Get_list_of_sent_for_each_thread for the dataset sample_dataset_mturk_no2
df_dataset_mturk_no2_list_of_sent = ta.get_list_of_sent_for_each_thread(df_dataset_mturk_no2)

# Load Threads summarized with LexRank
input_file_name = "threads_summarized_lexrank_20_to_20.csv"
threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH,"summarization", "summarization_with_sample_dataset_mturk_no2", "sentences", input_file_name]
input_file = os.path.join("", *threads_sample_path)
df_threads_summarized_lexrank = pd.read_csv(input_file)

# Create dict with all the thread_ids of df_threads_summarized_lexrank
thread_ids = df_threads_summarized_lexrank["thread_id"]
df_threads_summarized_lexrank_list_of_sent = dict.fromkeys(thread_ids, []) 

# For each thread id, add to df_threads_summarized_lexrank_list_of_sent dict to the list of sentences composing the summary
# In this case we selected summaries with 20 sentences, so we selected the column "lexrank_20_sent"
for row in df_threads_summarized_lexrank.itertuples():
    sentences = str(df_threads_summarized_lexrank.at[row.Index, "lexrank_20_sent"])
    list_sentences = sentences.split("\n")
    thread_id = df_threads_summarized_lexrank.at[row.Index, "thread_id"]
    df_threads_summarized_lexrank_list_of_sent[thread_id] = list_sentences

# Create dataframe of statistics to keep all the statistics
t_id_list = df_dataset_mturk_no2["thread_id"].unique().tolist()
df_stats = pd.DataFrame(t_id_list, columns=['thread_id'])

df_sentences_in_both_datasets = pd.DataFrame()
df_sentences_in_both_datasets["thread_id"] = ""
df_sentences_in_both_datasets["sentences_in_both_datasets"] = ""

df_stats["nb_of_sent_from_df_dataset_mturk_no2_in_threads_summarized_lexrank"] = 0
for row in df_stats.itertuples():
    thread_id = str(df_stats.at[row.Index, "thread_id"])
    summary_list_of_sent = df_threads_summarized_lexrank_list_of_sent[thread_id]
    mturk_list_of_sent = df_dataset_mturk_no2_list_of_sent[thread_id]
    count = 0
    for mturk_sent in mturk_list_of_sent:
        for summary_sent in summary_list_of_sent:
            if mturk_sent == summary_sent:
                count = count + 1
                temp = {
                    "thread_id": thread_id,
                    "sentences_in_both_datasets": mturk_sent,
                }
                df_sentences_in_both_datasets = df_sentences_in_both_datasets.append(temp, ignore_index=True)
    df_stats.at[row.Index, "nb_of_sent_from_df_dataset_mturk_no2_in_threads_summarized_lexrank"] = count

print("Statistics about the nb. of sentences in the thread summaries that are in " + input_file_name_1)
print(df_stats["nb_of_sent_from_df_dataset_mturk_no2_in_threads_summarized_lexrank"].describe())
print("")

# Log results
## Total number of sent from df dataset mturk no2 in threads summarized lexrank
total_number_of_sent_from_df_dataset_mturk_no2_in_threads_summarized_lexrank = df_stats["nb_of_sent_from_df_dataset_mturk_no2_in_threads_summarized_lexrank"].sum()
print("total_number_of_sent_from_df_dataset_mturk_no2_in_threads_summarized_lexrank", total_number_of_sent_from_df_dataset_mturk_no2_in_threads_summarized_lexrank)

## Summaries of threads that have at least one sentence in dataset mturk no2
df_at_least_one_sent =  df_stats.loc[df_stats["nb_of_sent_from_df_dataset_mturk_no2_in_threads_summarized_lexrank"] > 0]
nb_of_summaries_with_at_least_one_sent_in_dataset_mturk_no2 = len(df_at_least_one_sent)
nb_of_summaries = len(df_stats)
print("nb_of_summaries_with_at_least_one_sent_in_dataset_mturk_no2: ", nb_of_summaries_with_at_least_one_sent_in_dataset_mturk_no2)
print("nb_of_summaries: ", nb_of_summaries)


#%%
# Output list of sentences that are in both dataset summary and mturk
filename = "df_sentences_in_both_datasets_2.csv"
output_file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
output_file = os.path.join('', *output_file_path)
#df_sentences_in_both_datasets.to_csv(output_file, sep=',', encoding='utf-8', index=False)  


#%%

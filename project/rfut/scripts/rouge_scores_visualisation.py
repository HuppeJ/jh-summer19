
#%%
def run():
    print("Running : get_datasets_for_summarization")

    # Init tools 
    summarizer_tool = SummarizerTool()

    # Load thread text data in dataframe
    thread_text_file = [PROJECT_PATH, DATA_OUTPUT_PATH, "threads_text_for_summarization_no1.csv"]
    input_file = os.path.join("", *thread_text_file)
    df_threads_text = pd.read_csv(input_file)

    # TODO REMOVE LINE BELOW
    df_threads_text = df_threads_text[:2]


    min_nb_sentences = 1
    max_nb_sentences = 20
    
    for row in df_threads_text.itertuples():
        # Text data
        thread_text = str(df_threads_text.at[row.Index, "thread_text"])
        parsed_text = PlaintextParser.from_string(thread_text, Tokenizer("english"))

        for nb_sentence in range(min_nb_sentences, max_nb_sentences):
            # Summary data
            lexRank_summary_sentences = summarizer_tool.lexRankSummarizer(parsed_text.document, nb_sentence)
            # lexRank_summary = summarizer_tool.sentences_to_string(lexRank_summary_sentences)
            # df_threads_text.at[row.Index, "lexRank_summary"] = lexRank_summary

            # Score data        
            lexRank_rouge_1 = rouge_1(lexRank_summary_sentences, parsed_text.document.sentences)
            colum_name = "lexRank_" + str(nb_sentence) + "_sent" + "_rouge_1"
            df_threads_text.at[row.Index, colum_name] = lexRank_rouge_1


    df_threads_text = df_threads_text.drop(["thread_text"], axis=1)

    # Write df_sample_dataset
    filename = "threads_summarized_sumy_4_sent.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join("", *posts_path)
    df_threads_text.to_csv(output_file, sep=",", encoding="utf-8", index=False) 



#%%
# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
import numpy as np
import matplotlib.pyplot as plt 



# Load sample of threads data in dataframe
threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "threads_summarized_rouge_1_scores_no_text.csv"]
input_file = os.path.join('', *threads_sample_path)
df_input = pd.read_csv(input_file)

min_nb_sentences = 1
max_nb_sentences = 20
scores_means = []
nb_sentences = []
for nb_sentence in range(min_nb_sentences, max_nb_sentences):
    nb_sentences.append(nb_sentence)
    colum_name = "lexRank_" + str(nb_sentence) + "_sent" + "_rouge_1"
    scores_means.append(df_input[colum_name].mean())

# Plot graph
x = nb_sentences
y = scores_means
  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 1, markersize=12) 
  
plt.ylim(0.3,1) 
plt.xlim(0,21) 
  
plt.xlabel('Nb. of sentences') 
plt.ylabel('ROUGE-1 score') 
plt.title('ROUGE-1 score in function of the nb. of sentences') 
  
plt.show()

#%%

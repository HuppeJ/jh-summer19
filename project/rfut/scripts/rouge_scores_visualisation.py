#%%
# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
import numpy as np
import matplotlib.pyplot as plt 

# Init dictionary
data = {}

#%%
# Load sample of threads data in dataframe
threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "threads_summarized_rouge_1_scores_20_sent.csv"]
input_file = os.path.join("", *threads_sample_path)
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
  
plt.plot(x, y, color="green", linestyle="dashed", linewidth = 1, marker=".", markerfacecolor="blue") 

plt.xlim(0,21) 
plt.ylim(0.3,1) 

plt.title("LexRank: ROUGE-1 score in function of the nb. of sentences") 
plt.xlabel("Nb. of sentences") 
plt.ylabel("ROUGE-1 score") 
  
plt.show()

#%%

# Load sample of threads data in dataframe

summarization_technique = "lexrank"
score_technique = "rouge_2"
input_file_name = "threads_summarized_" + summarization_technique + "_" + score_technique + "_scores.csv"

threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, input_file_name]
input_file = os.path.join("", *threads_sample_path)
df_input = pd.read_csv(input_file)

min_nb_sentences = 2
max_nb_sentences = 10

scores_means = []
nb_sentences = []
for nb_sentence in range(min_nb_sentences, max_nb_sentences + 1):
    nb_sentences.append(nb_sentence)
    score_column = summarization_technique + "_" + str(nb_sentence) + "_sent" + "_" + score_technique
    scores_means.append(df_input[score_column].mean())

# Keep data in dictionary "data" to create graphs with multiple lines
scores_means_key = "scores_means_" + summarization_technique + "_" + score_technique
data[scores_means_key] = scores_means
nb_sentences_key = "nb_sentences_" + summarization_technique + "_" + score_technique
data[nb_sentences_key] = nb_sentences

# Plot graph
x = nb_sentences
y = scores_means
  
plt.plot(x, y, color="green", linestyle="dashed", linewidth = 1, marker=".", markerfacecolor="blue") 

plt.xlim(min_nb_sentences - 1,max_nb_sentences + 1) 
plt.ylim(0.3,1) 

plt.title(summarization_technique.upper() + ": " + score_technique.upper() + " scores in function of the nb. of sentences") 
plt.xlabel("Nb. of sentences") 
plt.ylabel(score_technique.upper() + " score") 
  
plt.show()

#%%

# Load sample of threads data in dataframe

summarization_technique = "lexrank"
score_technique = "rouge_3"
input_file_name = "threads_summarized_" + summarization_technique + "_" + score_technique + "_scores.csv"

threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, input_file_name]
input_file = os.path.join("", *threads_sample_path)
df_input = pd.read_csv(input_file)

min_nb_sentences = 2
max_nb_sentences = 10

scores_means = []
nb_sentences = []
for nb_sentence in range(min_nb_sentences, max_nb_sentences + 1):
    nb_sentences.append(nb_sentence)
    score_column = summarization_technique + "_" + str(nb_sentence) + "_sent" + "_" + score_technique
    scores_means.append(df_input[score_column].mean())

# Keep data in dictionary "data" to create graphs with multiple lines
scores_means_key = "scores_means_" + summarization_technique + "_" + score_technique
data[scores_means_key] = scores_means
nb_sentences_key = "nb_sentences_" + summarization_technique + "_" + score_technique
data[nb_sentences_key] = nb_sentences

# Plot graph
x = nb_sentences
y = scores_means
  
plt.plot(x, y, color="green", linestyle="dashed", linewidth = 1, marker=".", markerfacecolor="blue") 

plt.xlim(min_nb_sentences - 1,max_nb_sentences + 1) 
plt.ylim(0.3,1) 

plt.title(summarization_technique.upper() + ": " + score_technique.upper() + " scores in function of the nb. of sentences") 
plt.xlabel("Nb. of sentences") 
plt.ylabel(score_technique.upper() + " score") 
  
plt.show()

#%%

# Load sample of threads data in dataframe

summarization_technique = "sumbasic"
score_technique = "rouge_2"
input_file_name = "threads_summarized_" + summarization_technique + "_" + score_technique + "_scores.csv"

threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, input_file_name]
input_file = os.path.join("", *threads_sample_path)
df_input = pd.read_csv(input_file)

min_nb_sentences = 2
max_nb_sentences = 10

scores_means = []
nb_sentences = []
for nb_sentence in range(min_nb_sentences, max_nb_sentences + 1):
    nb_sentences.append(nb_sentence)
    score_column = summarization_technique + "_" + str(nb_sentence) + "_sent" + "_" + score_technique
    scores_means.append(df_input[score_column].mean())

# Keep data in dictionary "data" to create graphs with multiple lines
scores_means_key = "scores_means_" + summarization_technique + "_" + score_technique
data[scores_means_key] = scores_means
nb_sentences_key = "nb_sentences_" + summarization_technique + "_" + score_technique
data[nb_sentences_key] = nb_sentences

# Plot graph
x = nb_sentences
y = scores_means
  
plt.plot(x, y, color="green", linestyle="dashed", linewidth = 1, marker=".", markerfacecolor="blue") 

plt.xlim(min_nb_sentences - 1,max_nb_sentences + 1) 
plt.ylim(0.3,1) 

plt.title(summarization_technique.upper() + ": " + score_technique.upper() + " scores in function of the nb. of sentences") 
plt.xlabel("Nb. of sentences") 
plt.ylabel(score_technique.upper() + " score") 
  
plt.show()

#%%

# Load sample of threads data in dataframe

summarization_technique = "sumbasic"
score_technique = "rouge_3"
input_file_name = "threads_summarized_" + summarization_technique + "_" + score_technique + "_scores.csv"

threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, input_file_name]
input_file = os.path.join("", *threads_sample_path)
df_input = pd.read_csv(input_file)

min_nb_sentences = 2
max_nb_sentences = 10

scores_means = []
nb_sentences = []
for nb_sentence in range(min_nb_sentences, max_nb_sentences + 1):
    nb_sentences.append(nb_sentence)
    score_column = summarization_technique + "_" + str(nb_sentence) + "_sent" + "_" + score_technique
    scores_means.append(df_input[score_column].mean())

# Keep data in dictionary "data" to create graphs with multiple lines
scores_means_key = "scores_means_" + summarization_technique + "_" + score_technique
data[scores_means_key] = scores_means
nb_sentences_key = "nb_sentences_" + summarization_technique + "_" + score_technique
data[nb_sentences_key] = nb_sentences

# Plot graph
x = nb_sentences
y = scores_means
  
plt.plot(x, y, color="green", linestyle="dashed", linewidth = 1, marker=".", markerfacecolor="blue") 

plt.xlim(min_nb_sentences - 1,max_nb_sentences + 1) 
plt.ylim(0.3,1) 

plt.title(summarization_technique.upper() + ": " + score_technique.upper() + " scores in function of the nb. of sentences") 
plt.xlabel("Nb. of sentences") 
plt.ylabel(score_technique.upper() + " score") 
  
plt.show()


#%%

# Load sample of threads data in dataframe

summarization_technique = "textrank"
score_technique = "rouge_2"
input_file_name = "threads_summarized_" + summarization_technique + "_" + score_technique + "_scores.csv"

threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, input_file_name]
input_file = os.path.join("", *threads_sample_path)
df_input = pd.read_csv(input_file)

min_nb_sentences = 2
max_nb_sentences = 10

scores_means = []
nb_sentences = []
for nb_sentence in range(min_nb_sentences, max_nb_sentences + 1):
    nb_sentences.append(nb_sentence)
    score_column = summarization_technique + "_" + str(nb_sentence) + "_sent" + "_" + score_technique
    scores_means.append(df_input[score_column].mean())

# Keep data in dictionary "data" to create graphs with multiple lines
scores_means_key = "scores_means_" + summarization_technique + "_" + score_technique
data[scores_means_key] = scores_means
nb_sentences_key = "nb_sentences_" + summarization_technique + "_" + score_technique
data[nb_sentences_key] = nb_sentences

# Plot graph
x = nb_sentences
y = scores_means
  
plt.plot(x, y, color="green", linestyle="dashed", linewidth = 1, marker=".", markerfacecolor="blue") 

plt.xlim(min_nb_sentences - 1,max_nb_sentences + 1) 
plt.ylim(0.3,1) 

plt.title(summarization_technique.upper() + ": " + score_technique.upper() + " scores in function of the nb. of sentences") 
plt.xlabel("Nb. of sentences") 
plt.ylabel(score_technique.upper() + " score") 
  
plt.show()


#%%

# Load sample of threads data in dataframe

summarization_technique = "textrank"
score_technique = "rouge_3"
input_file_name = "threads_summarized_" + summarization_technique + "_" + score_technique + "_scores.csv"

threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, input_file_name]
input_file = os.path.join("", *threads_sample_path)
df_input = pd.read_csv(input_file)

min_nb_sentences = 2
max_nb_sentences = 10

scores_means = []
nb_sentences = []
for nb_sentence in range(min_nb_sentences, max_nb_sentences + 1):
    nb_sentences.append(nb_sentence)
    score_column = summarization_technique + "_" + str(nb_sentence) + "_sent" + "_" + score_technique
    scores_means.append(df_input[score_column].mean())

# Keep data in dictionary "data" to create graphs with multiple lines
scores_means_key = "scores_means_" + summarization_technique + "_" + score_technique
data[scores_means_key] = scores_means
nb_sentences_key = "nb_sentences_" + summarization_technique + "_" + score_technique
data[nb_sentences_key] = nb_sentences

# Plot graph
x = nb_sentences
y = scores_means
  
plt.plot(x, y, color="green", linestyle="dashed", linewidth = 1, marker=".", markerfacecolor="blue") 

plt.xlim(min_nb_sentences - 1,max_nb_sentences + 1) 
plt.ylim(0.3,1) 

plt.title(summarization_technique.upper() + ": " + score_technique.upper() + " scores in function of the nb. of sentences") 
plt.xlabel("Nb. of sentences") 
plt.ylabel(score_technique.upper() + " score") 
  
plt.show()



#%%

score_technique = "rouge_2"

# Plot graph
x = nb_sentences
y = scores_means
  
summarization_technique_1 = "lexrank"
summarization_technique_2 = "sumbasic"
summarization_technique_3 = "textrank"

scores_means_key_1 = "scores_means_" + summarization_technique_1 + "_" + score_technique
scores_means_key_2 = "scores_means_" + summarization_technique_2 + "_" + score_technique
scores_means_key_3 = "scores_means_" + summarization_technique_3 + "_" + score_technique

nb_sentences_key = "nb_sentences_" + summarization_technique + "_" + score_technique

plt.plot(data[nb_sentences_key], data[scores_means_key_1], linestyle="dashed", linewidth = 1, marker=".") 
plt.plot(data[nb_sentences_key], data[scores_means_key_2], linestyle="dashed", linewidth = 1, marker=".") 
plt.plot(data[nb_sentences_key], data[scores_means_key_3], linestyle="dashed", linewidth = 1, marker=".") 

plt.xlim(min_nb_sentences - 1,max_nb_sentences + 1) 
plt.ylim(0.3,1) 

plt.title(score_technique.upper() + " scores in function of the nb. of sentences") 
plt.xlabel("Nb. of sentences") 
plt.ylabel(score_technique.upper() + " score") 
  
plt.legend([summarization_technique_1, summarization_technique_2, summarization_technique_3], loc='lower right')

plt.show()


#%%
score_technique = "rouge_3"

# Plot graph
x = nb_sentences
y = scores_means
  
summarization_technique_1 = "lexrank"
summarization_technique_2 = "sumbasic"
summarization_technique_3 = "textrank"

scores_means_key_1 = "scores_means_" + summarization_technique_1 + "_" + score_technique
scores_means_key_2 = "scores_means_" + summarization_technique_2 + "_" + score_technique
scores_means_key_3 = "scores_means_" + summarization_technique_3 + "_" + score_technique

nb_sentences_key = "nb_sentences_" + summarization_technique + "_" + score_technique

plt.plot(data[nb_sentences_key], data[scores_means_key_1], linestyle="dashed", linewidth = 1, marker=".") 
plt.plot(data[nb_sentences_key], data[scores_means_key_2], linestyle="dashed", linewidth = 1, marker=".") 
plt.plot(data[nb_sentences_key], data[scores_means_key_3], linestyle="dashed", linewidth = 1, marker=".") 

plt.xlim(min_nb_sentences - 1,max_nb_sentences + 1) 
plt.ylim(0.3,1) 

plt.title(score_technique.upper() + " scores in function of the nb. of sentences") 
plt.xlabel("Nb. of sentences") 
plt.ylabel(score_technique.upper() + " score") 
  
plt.legend([summarization_technique_1, summarization_technique_2, summarization_technique_3], loc='lower right')

plt.show()

#%%


#%%

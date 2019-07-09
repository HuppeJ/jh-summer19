#%%
# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
import numpy as np
import matplotlib.pyplot as plt 
from rfut.objects.thread_analyser import ThreadAnalyzer 
from rfut.objects.sentence_parser import SentenceParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Init tools 
ta = ThreadAnalyzer()
sp = SentenceParser()

# Load Dataset1 (First dataset ready to sumbit to mturk)
input_file_name = "sample_dataset_mturk_no1.csv"
threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, input_file_name]
input_file = os.path.join("", *threads_sample_path)
df_dataset_mturk_no1 = pd.read_csv(input_file)

df_dataset_mturk_no1_list_of_sent = ta.get_list_of_sent_for_each_thread(df_dataset_mturk_no1)


# Load Threads summarized with LexRank
input_file_name = "threads_summarized_lexrank_1_to_50.csv"
threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "sentences", input_file_name]
input_file = os.path.join("", *threads_sample_path)
df_threads_summarized_lexrank = pd.read_csv(input_file)

thread_ids = df_threads_summarized_lexrank["thread_id"]
df_threads_summarized_lexrank_list_of_sent = dict.fromkeys(thread_ids, []) 

for row in df_threads_summarized_lexrank.itertuples():
    sentences = str(df_threads_summarized_lexrank.at[row.Index, "lexrank_20_sent"])
    list_sentences = sentences.split("\n")
    thread_id = df_threads_summarized_lexrank.at[row.Index, "thread_id"]
    df_threads_summarized_lexrank_list_of_sent[thread_id] = list_sentences


df_stats = df_threads_summarized_lexrank[["thread_id"]].copy()


#%%

df_stats["avg_len_of_sent_in_dataset_mturk_no1"] = 0
for row in df_stats.itertuples():
    thread_id = df_stats.at[row.Index, "thread_id"]
    list_of_sent = df_dataset_mturk_no1_list_of_sent[thread_id]
    total_nb_of_words = 0
    for sent in list_of_sent:
        total_nb_of_words += sp.word_count(sent)
    avg = total_nb_of_words / len(list_of_sent)
    df_stats.at[row.Index, "avg_len_of_sent_in_dataset_mturk_no1"] = avg


df_stats["avg_len_of_sent_in_df_threads_summarized_lexrank"] = 0
for row in df_stats.itertuples():
    thread_id = df_stats.at[row.Index, "thread_id"]
    list_of_sent = df_threads_summarized_lexrank_list_of_sent[thread_id]
    total_nb_of_words = 0
    for sent in list_of_sent:
        total_nb_of_words += sp.word_count(sent)
    avg = total_nb_of_words / len(list_of_sent)
    df_stats.at[row.Index, "avg_len_of_sent_in_df_threads_summarized_lexrank"] = avg

#%%
# Boxplot Nb. of words in sentences
dataset_mturk_no1 = df_stats["avg_len_of_sent_in_dataset_mturk_no1"]
threads_summarized_lexrank = df_stats["avg_len_of_sent_in_df_threads_summarized_lexrank"]

fig = plt.figure()
ax = fig.add_subplot(111)
fig.suptitle("Average nb. of words in sentences for dataset_mturk_no1 and threads_summarized_lexrank")
plt.ylabel("Average nb. of words in sentences")
ax.boxplot([dataset_mturk_no1,threads_summarized_lexrank], labels=["dataset_mturk_no1", "threads_summarized_lexrank"]);
#ax.set(ylim=(0, 50))

#%%
# Notch Boxplot Nb. of words in sentences
fig = plt.figure()
ax = fig.add_subplot(111)
fig.suptitle("Average nb. of words in sentences for dataset_mturk_no1 and threads_summarized_lexrank")
plt.ylabel("Average nb. of words in sentences")
ax.boxplot([dataset_mturk_no1,threads_summarized_lexrank], notch = True, labels=["dataset_mturk_no1", "threads_summarized_lexrank"]);
#ax.set(ylim=(0, 50))

#%% 

# Statistic tests to find if there is a significant relation 
x1 = df_stats["avg_len_of_sent_in_dataset_mturk_no1"]
x2 = df_stats["avg_len_of_sent_in_df_threads_summarized_lexrank"]
print("T-test using scipy:")
# https://machinelearningmastery.com/parametric-statistical-significance-tests-in-python/
t, p = stats.ttest_ind(x1, x2)
print("t = " + str(t))
print("p = " + str(p))
# interpret
alpha = 0.05
if p > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')


# The code is good I think there is a problem with the jupyter environnement 
# Maybe the solution would be to uninstall statsmodel and reinstall it with "pip install statsmodel"
tstat, pvalue, df = sm.stats.weightstats.ttest_ind(x1, x2)
# interpret
alpha = 0.05
if pvalue > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')


print("")
print("Anova test using scipy:")
F, p = stats.f_oneway(df_stats["avg_len_of_sent_in_dataset_mturk_no1"], df_stats["avg_len_of_sent_in_df_threads_summarized_lexrank"])
print("F-statistic:", F)
print("p-value:", p)

print("")
print("Anova test using statsmodel:")
results  = ols('avg_len_of_sent_in_df_threads_summarized_lexrank~avg_len_of_sent_in_dataset_mturk_no1', data=df_stats).fit()
#result = ols(df_stats["avg_len_of_sent_in_dataset_mturk_no1"], df_stats["avg_len_of_sent_in_df_threads_summarized_lexrank"])
#results.summary()       


#%%
# Summary of threads that have at least one sentence in dataset mturk no1

df_stats["nb_of_sent_from_df_dataset_mturk_no1_in_threads_summarized_lexrank"] = 0
for row in df_stats.itertuples():
    thread_id = df_stats.at[row.Index, "thread_id"]
    summary_list_of_sent = df_threads_summarized_lexrank_list_of_sent[thread_id]
    mturk_list_of_sent = df_dataset_mturk_no1_list_of_sent[thread_id]
    count = 0
    for mturk_sent in mturk_list_of_sent:
        for summary_sent in summary_list_of_sent:
            if mturk_sent in summary_sent:
                count = count + 1
    df_stats.at[row.Index, "nb_of_sent_from_df_dataset_mturk_no1_in_threads_summarized_lexrank"] = count

fig = plt.figure()
ax = fig.add_subplot(111)
fig.suptitle("Summary of threads that have at least one sentence in dataset mturk no1")
plt.ylabel("Nb. of sentences")
ax.boxplot([df_stats["nb_of_sent_from_df_dataset_mturk_no1_in_threads_summarized_lexrank"]], labels=["Distribution"])
#ax.set(ylim=(0, 2))


#%%
# Distribution Nb. of sentences per thread

df_stats["nb_of_sent_per_thread"] = 0


# Load parsed_0.02_of_threads_to_sentences_kept_sentences.csv
input_file_name = "parsed_0.02_of_threads_to_sentences_kept_sentences.csv"
threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, input_file_name]
input_file = os.path.join("", *threads_sample_path)
df_threads_text = pd.read_csv(input_file)

#list_selected_thread_ids = df_threads_summarized_lexrank["thread_id"].tolist()
# Only take the thread text of the selected thread (st)
#df_threads_text_st = df_threads_text.loc[df_threads_text['thread_id'].isin(list_selected_thread_ids)]

value_counts = df_threads_text["thread_id"].value_counts()

for row in df_stats.itertuples():
    thread_id = df_stats.at[row.Index, "thread_id"]
    df_stats.at[row.Index, "nb_of_sent_per_thread"] = value_counts[thread_id]


print("Average number of sentences per thread:" , round(df_stats["nb_of_sent_per_thread"].mean()))

fig = plt.figure()
ax = fig.add_subplot(111)
fig.suptitle("Distribution of the number of sentences per thread")
plt.ylabel("Nb. of sentences")
ax.boxplot([df_stats["nb_of_sent_per_thread"]], labels=["Distribution"])



fig = plt.figure()
ax = fig.add_subplot(111)
fig.suptitle("Distribution of the number of sentences per thread")
plt.ylabel("Nb. of sentences")
ax.boxplot([df_stats["nb_of_sent_per_thread"]], labels=["Distribution"])
ax.set(ylim=(0, 200))

#%%
# Histogram of Nb. of sentences per thread
n, bins, patches = plt.hist(x=df_stats["nb_of_sent_per_thread"], bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Nb. of sentences per thread')
plt.ylabel('Frequency')
plt.title('Frequency of the Nb. of sentences per thread')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

#%%
# Histogram of Nb. of sentences per thread
n, bins, patches = plt.hist(x=df_stats["nb_of_sent_per_thread"], bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Nb. of sentences per thread')
plt.ylabel('Frequency')
plt.title('Frequency of the Nb. of sentences per thread')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.xlim(0, 200)


#%%

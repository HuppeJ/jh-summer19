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

# Load Dataset parsed_0.02_kept_threads_with_is_question_and_annotations
input_file_name = "parsed_0.02_kept_threads_with_is_question_and_annotations.csv"
threads_sample_path = [PROJECT_PATH, DATA_OUTPUT_PATH, input_file_name]
input_file = os.path.join("", *threads_sample_path)
df_input = pd.read_csv(input_file)


#%%
#df2 = pd.DataFrame(np.random.rand(10, 4), columns=['is_question', 'has_annotations'])

#df_input[['is_question', 'has_annotations']].plot.bar();
df_stats = pd.DataFrame()

grouped = df_input.groupby("subforum_number")

df_stats["subforum_number"] = grouped.groups
df_stats["nb_of_is_question"] = 0
df_stats["nb_of_has_annotations"] = 0

for row in df_stats.itertuples():
    subforum_number = int(df_stats.at[row.Index, "subforum_number"])
    subforum_data = grouped.get_group(subforum_number)
    # Counts the number of True values in respective columns
    nb_of_is_question = subforum_data["is_question"].sum()
    nb_of_has_annotations = subforum_data["has_annotations"].sum()
    # Write new values in df_stats
    df_stats.at[row.Index, "nb_of_is_question"] = nb_of_is_question
    df_stats.at[row.Index, "nb_of_has_annotations"] = nb_of_has_annotations

df_stats[["nb_of_is_question", "nb_of_has_annotations"]].plot.bar()

df_stats[["nb_of_is_question"]].plot.bar()

df_stats[["nb_of_has_annotations"]].plot.bar()
#%%

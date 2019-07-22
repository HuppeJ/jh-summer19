# Imports
import os
import pandas as pd
import numpy as np
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from sumy.summarizers.lex_rank import LexRankSummarizer 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from rfut.objects.summarizer_tool import SummarizerTool

# ROUGE (metric): https://en.wikipedia.org/wiki/ROUGE_(metric)
# Sumy ROUGE: http://pydoc.net/sumy/0.4.1/sumy.evaluation.rouge/

# [✓] ROUGE-N: Overlap of N-grams[2] between the system and reference summaries.
# [✓] ROUGE-1 refers to the overlap of 1-gram (each word) between the system and reference summaries.
# [✓] ROUGE-2 refers to the overlap of bigrams between the system and reference summaries.
# [✓] ROUGE-L: Longest Common Subsequence (LCS)[3] based statistics. Longest common subsequence problem takes into account sentence level structure similarity naturally and identifies longest co-occurring in sequence n-grams automatically.
# [x] ROUGE-W: Weighted LCS-based statistics that favors consecutive LCSes .
# [x] ROUGE-S: Skip-bigram[4] based co-occurrence statistics. Skip-bigram is any pair of words in their sentence order.
# [x] ROUGE-SU: Skip-bigram plus unigram-based co-occurrence statistics.

# Computes ROUGE-N of two text collections of sentences.
from sumy.evaluation.rouge import rouge_n
# Rouge-N where N=1.  This is a commonly used metric.
from sumy.evaluation.rouge import rouge_1
# Rouge-N where N=2.  This is a commonly used metric.
from sumy.evaluation.rouge import rouge_2
# Computes ROUGE-L (sentence level) of two text collections of sentences.
from sumy.evaluation.rouge import rouge_l_sentence_level


# Check list: 
# [ - ]: Change summarization_technique 
# [ - ]: Change score_technique 
# [ - ]: Change min&max_nb_sentences?
# [ - ]: Change the score technique used rouge_X(summary_sentences, parsed_text.document.sentences)

def run():
    print("Running : thread_summary_rouge_scores")
    summarization_technique = "sumbasic"
    score_technique = "rouge_2"
    min_nb_sentences = 1
    max_nb_sentences = 25

    input_file_name = "threads_summarized_" + summarization_technique + "_" + str(min_nb_sentences) + "_to_" + str(max_nb_sentences) + ".csv"
  
    # Init tools 
    summarizer_tool = SummarizerTool()

    # Load thread text data in dataframe
    thread_text_file = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "sentences", input_file_name]
    input_file = os.path.join("", *thread_text_file)
    df_threads_summaries = pd.read_csv(input_file)

    # TODO REMOVE LINE BELOW
    #df_threads_summaries = df_threads_summaries[:2]

    df_scores = df_threads_summaries[["thread_id"]].copy()

    for row in df_threads_summaries.itertuples():
        # See progress
        if (row.Index % 100 == 0):
            print(row.Index / len(df_threads_summaries))

        # Text data
        thread_text = str(df_threads_summaries.at[row.Index, "thread_text"])
        parsed_text = PlaintextParser.from_string(thread_text, Tokenizer("english"))

        for nb_sentence in range(min_nb_sentences, max_nb_sentences + 1):
            # Summary data
            summary_column = summarization_technique + "_" + str(nb_sentence) + "_sent"
            summary_text = str(df_threads_summaries.at[row.Index, summary_column])
            parsed_summary = PlaintextParser.from_string(summary_text, Tokenizer("english"))
            summary_sentences = parsed_summary.document.sentences
            
            #print(nb_sentence)
            #print(summary_text)
            #print(parsed_summary.document)
            #print(summary_sentences)
            
            # Score data
            # TODO: Change the score technique used
            if len(summary_sentences) > 0:
                score = rouge_n(summary_sentences, parsed_text.document.sentences, 2)
            else:
                score = np.nan
            score_column = summarization_technique + "_" + str(nb_sentence) + "_sent" + "_" + score_technique
            df_scores.at[row.Index, score_column] = score

    # Write df_sample_dataset
    filename = "threads_summarized_" + summarization_technique + "_" + score_technique + "_scores_" + str(min_nb_sentences) + "_to_" + str(max_nb_sentences) + ".csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "sentences", filename]
    output_file = os.path.join("", *output_path)
    df_scores.to_csv(output_file, sep=",", encoding="utf-8", index=False) 

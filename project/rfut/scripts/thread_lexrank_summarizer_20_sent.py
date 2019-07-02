# Imports
import os
import pandas as pd
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


def run():
    print("Running : thread_lexrank_summarizer_20_sent")

    # Init tools 
    summarizer_tool = SummarizerTool()

    # Load thread text data in dataframe
    thread_text_file = [PROJECT_PATH, DATA_OUTPUT_PATH, "threads_text_for_summarization_no1.csv"]
    input_file = os.path.join("", *thread_text_file)
    df_threads_text = pd.read_csv(input_file)

    # TODO REMOVE LINE BELOW
    # df_threads_text = df_threads_text[:2]

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
    filename = "threads_summarized_rouge_1_scores_20_sent.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join("", *posts_path)
    df_threads_text.to_csv(output_file, sep=",", encoding="utf-8", index=False) 

# Imports
import os
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from sumy.summarizers.lex_rank import LexRankSummarizer 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

def run():
    print("Running : get_datasets_for_summarization")

    # Init tools 
    summarizer = LexRankSummarizer()

    # Load thread text data in dataframe
    thread_text_file = [PROJECT_PATH, DATA_OUTPUT_PATH, "threads_text_for_summarization_no1.csv"]
    input_file = os.path.join("", *thread_text_file)
    df_threads_text = pd.read_csv(input_file)

    df_threads_text["thread_summary"] = ""
    # Nb. of sentences for summary
    nb_sentences = 4

    for row in df_threads_text.itertuples():
        thread_text = str(df_threads_text.at[row.Index, "thread_text"])
        parser = PlaintextParser.from_string(thread_text, Tokenizer("english"))
        summary = summarizer(parser.document, nb_sentences)
        summary_string = ""
        for sentence in summary:
            summary_string += "\n " + str(sentence)
        summary_string = summary_string[2:]
        df_threads_text.at[row.Index, "thread_summary"] = summary_string

    df_threads_text = df_threads_text.drop(["thread_text"], axis=1)

    # Write df_sample_dataset
    filename = "threads_summarized_sumy_4_sent.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join("", *posts_path)
    df_threads_text.to_csv(output_file, sep=",", encoding="utf-8") 

# Imports
import os
import sys
import pandas as pd
import numpy as np
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH, HUPPEJ_GENSIM_PROJECT_PATH
from sumy.summarizers.lex_rank import LexRankSummarizer 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from rfut.objects.summarizer_tool import SummarizerTool

# Import local huppej_gensim project 
# Note: Using insert to overwrite the original gensim package
# https://stackoverflow.com/questions/43627020/import-forked-module-in-python-instead-of-installed-module
# https://stackoverflow.com/questions/44070953/python-import-package-from-different-project
# https://stackoverflow.com/questions/14509192/how-to-import-functions-from-other-projects-in-python
sys.path.insert(0, os.path.abspath(HUPPEJ_GENSIM_PROJECT_PATH))

from gensim.summarization.summarizer import summarize as gensim_textrank_summarize
from gensim.summarization.summarizer import _format_results 
#from huppej_gensim.gesim.summarization import keywords

# TIMES : 
# When the text was separated by posts 
# LexRank: --- 850.9803490638733 seconds --- 14.20 min
# TextRank --- 18994.14727139473 seconds --- 5h17 min
# SumBasic --- 82.4651882648468 seconds ---  1.38 min
#
# When the text was separated by sentences for 500 threads
# LexRank:
# TextRank 
# SumBasic --- 1000.7766623497009 seconds ---
#
# When the text was separated by sentences for 1600 threads
# LexRank:
# TextRank: --- 105621.08 seconds ---  ~30h
# SumBasic: 

# Important Note: 
# SumBasic uses sumy
# LexRank uses sumy
# TextRank uses modified algo of Gensim (it is the Gensim algo, but adjusted to get the all the summaries of 1 to 50 sentences at once.)

# Check list: 
# [ - ]: Change name of variable summarization_technique
# [ - ]: Change min&max_nb_sentences?
# [ - ]: Change the summarizer used summarizer_tool.X


def get_n_best_extracted_sentences_text(extracted_sentences, nb_sentence):
    n_best_extracted_sentences = extracted_sentences[:nb_sentence]
    n_best_extracted_sentences.sort(key=lambda s: s.index)
    return _format_results(n_best_extracted_sentences, True)

def run():
    print("Running : thread_summarizer")
    
    summarization_technique = "lexrank"    

    # Init tools 
    summarizer_tool = SummarizerTool()

    # Load thread text data in dataframe
    thread_text_file = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "summarization_with_sample_dataset_mturk_no2", "threads_text_for_summarization_no2.csv"]
    input_file = os.path.join("", *thread_text_file)
    df_threads_text = pd.read_csv(input_file)
    
    # TODO REMOVE LINE BELOW
    #df_threads_text = df_threads_text[:1]

    min_nb_sentences = 20
    max_nb_sentences = 20
    
    for row in df_threads_text.itertuples():
        # See progress
        if (row.Index % 100 == 0):
            print(row.Index / len(df_threads_text))

        # Text data
        thread_text = str(df_threads_text.at[row.Index, "thread_text"])
        parsed_text = PlaintextParser.from_string(thread_text, Tokenizer("english"))

        if summarization_technique == "textrank":  
            text = summarizer_tool.sentences_to_string(parsed_text.document.sentences)
            try:
                extracted_sentences = gensim_textrank_summarize(text, nb_sentences=max_nb_sentences, split=True) 
            except Exception as e: 
                print(e)
                extracted_sentences = np.nan
        
        for nb_sentence in range(min_nb_sentences, max_nb_sentences + 1):
            # Summary data
            # TODO: Change the summarizer
            if summarization_technique == "sumbasic":
                summary_sentences = summarizer_tool.sumBasicSummarizer(parsed_text.document, nb_sentence)
            elif summarization_technique == "lexrank":  
                summary_sentences = summarizer_tool.lexRankSummarizer(parsed_text.document, nb_sentence)
            elif summarization_technique == "textrank":  
                # summary_sentences = summarizer_tool.textRankSummarizer(parsed_text.document, nb_sentence)
                if extracted_sentences is not np.nan:
                    summary_sentences = get_n_best_extracted_sentences_text(extracted_sentences, nb_sentence)
                else:
                    summary_sentences = ""
                    
            summary_string = summarizer_tool.sentences_to_string(summary_sentences)
            colum_name = summarization_technique + "_" + str(nb_sentence) + "_sent"
            df_threads_text.at[row.Index, colum_name] = summary_string


    # Write df_sample_dataset
    filename = "threads_summarized_" + summarization_technique + "_" + str(min_nb_sentences) + "_to_" + str(max_nb_sentences)
    filename_with_text = filename + ".csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "summarization_with_sample_dataset_mturk_no2", "sentences", filename_with_text]
    output_file = os.path.join("", *posts_path)
    df_threads_text.to_csv(output_file, sep=",", encoding="utf-8", index=False) 

    df_threads_text = df_threads_text.drop(["thread_text"], axis=1)

    filename_without_text = filename + "_no_text.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "summarization", "summarization_with_sample_dataset_mturk_no2", "sentences", filename_without_text]
    output_file = os.path.join("", *posts_path)
    df_threads_text.to_csv(output_file, sep=",", encoding="utf-8", index=False) 


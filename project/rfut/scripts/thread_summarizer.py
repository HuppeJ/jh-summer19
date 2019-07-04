# Imports
import os
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from sumy.summarizers.lex_rank import LexRankSummarizer 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from rfut.objects.summarizer_tool import SummarizerTool

# Check list: 
# [ - ]: Change name of variable summarization_technique
# [ - ]: Change min&max_nb_sentences?
# [ - ]: Change the summarizer used summarizer_tool.X


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
# TextRank 
# SumBasic 

def run():
    print("Running : thread_summarizer")
    
    summarization_technique = "sumbasic"    

    # Init tools 
    summarizer_tool = SummarizerTool()

    # Load thread text data in dataframe
    thread_text_file = [PROJECT_PATH, DATA_OUTPUT_PATH, "threads_text_for_summarization_no1.csv"]
    input_file = os.path.join("", *thread_text_file)
    df_threads_text = pd.read_csv(input_file)
    
    # TODO REMOVE LINE BELOW
    #df_threads_text = df_threads_text[:50]

    min_nb_sentences = 26
    max_nb_sentences = 50
    
    for row in df_threads_text.itertuples():
        # See progress
        if (row.Index % 100 == 0):
            print(row.Index / len(df_threads_text))

        # Text data
        thread_text = str(df_threads_text.at[row.Index, "thread_text"])
        parsed_text = PlaintextParser.from_string(thread_text, Tokenizer("english"))

        for nb_sentence in range(min_nb_sentences, max_nb_sentences + 1):
            # Summary data
            # TODO: Change the summarizer
            if summarization_technique == "sumbasic":
                summary_sentences = summarizer_tool.sumBasicSummarizer(parsed_text.document, nb_sentence)
            elif summarization_technique == "lexrank":  
                summary_sentences = summarizer_tool.lexRankSummarizer(parsed_text.document, nb_sentence)
            elif summarization_technique == "textrank":  
                summary_sentences = summarizer_tool.textRankSummarizer(parsed_text.document, nb_sentence)

            summary_string = summarizer_tool.sentences_to_string(summary_sentences)
            colum_name = summarization_technique + "_" + str(nb_sentence) + "_sent"
            df_threads_text.at[row.Index, colum_name] = summary_string


    # Write df_sample_dataset
    filename = "threads_summarized_" + summarization_technique + "_" + str(min_nb_sentences) + "_to_" + str(max_nb_sentences)
    filename_with_text = filename + ".csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename_with_text]
    output_file = os.path.join("", *posts_path)
    df_threads_text.to_csv(output_file, sep=",", encoding="utf-8", index=False) 

    df_threads_text = df_threads_text.drop(["thread_text"], axis=1)

    filename_without_text = filename + "_no_text.csv"
    posts_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename_without_text]
    output_file = os.path.join("", *posts_path)
    df_threads_text.to_csv(output_file, sep=",", encoding="utf-8", index=False) 


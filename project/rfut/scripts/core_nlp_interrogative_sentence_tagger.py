### Set it up
# 1: Download Stanford-core nlp: https://stanfordnlp.github.io/CoreNLP/download.html
# 2: Unzip downloaded file
# 3: Open a Microsoft Windows Command Prompt (not powershell) and navigate inside the unzipped file
# 4: Run the command: 
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer \
# -preload tokenize,ssplit,pos,lemma,ner,parse,depparse \
# -status_port 9000 -port 9000 -timeout 15000 & 
# Now the Core-NLP server should be running and you should see the message below: 
# "[...] StanfordCoreNLPServer listening at /0:0:0:0:0:0:0:0:9000 [...]"


## Algorithm 
# For each sentence we retrieved the Clause Level Tag of the sentence with the CoreNLP parser
# Here are the different possible Clause Level Tags and the numbers we associated to them:
# 1: S - simple declarative clause, i.e. one that is not introduced by a (possible empty) subordinating conjunction or a wh-word and that does not exhibit subject-verb inversion.
# 2: SBAR - Clause introduced by a (possibly empty) subordinating conjunction.
# 3: SBARQ - Direct question introduced by a wh-word or a wh-phrase. Indirect questions and relative clauses should be bracketed as SBAR, not SBARQ.
# 4: SINV - Inverted declarative sentence, i.e. one in which the subject follows the tensed verb or modal.
# 5: SQ - Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.
# 6: Null Value

# Here are two links to Penn Treebank II Tags documentation:
# http://www.surdeanu.info/mihai/teaching/ista555-fall13/readings/PennTreebankConstituents.html#SINV
# https://gist.github.com/nlothian/9240750

# Imports
import csv
import os
import re
import pandas as pd
from nltk import sent_tokenize
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from rfut.objects.sentence_parser import SentenceParser 

from nltk.parse import CoreNLPParser
parser = CoreNLPParser(url='http://localhost:9000')

def run():
    print("Running : core_nlp_interrogative_sentence_tagger")

    # Init tools 
    sp = SentenceParser()

    # First run of the program
    # Load sample of threads data in dataframe
    #file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "parsed_0.02_of_threads_kept_threads.csv"]
    #input_file = os.path.join('', *file_path)
    #df_input = pd.read_csv(input_file)
    #df_input["core_nlp_clause_tag"] = 0

    # Second run and more of the program
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "parsed_0.02_kept_threads_with_core_nlp_clause_tags.csv"]
    input_file = os.path.join('', *file_path)
    df_input = pd.read_csv(input_file)

    #df_input_1 = df_input.iloc[0:10000]
    #df_input_2 = df_input.iloc[10000:20000]
    #df_input_3 = df_input.iloc[20000:30000]
    #df_input_4 = df_input.iloc[30000:40000]
    #df_input_5 = df_input.iloc[40000:50000]
    #df_input_6 = df_input.iloc[50000:60000]
    #df_input_7 = df_input.iloc[60000:70000]
    #df_input_8 = df_input.iloc[70000:80000]
    df_input_8 = df_input.iloc[80000:90000]
    #df_input_9 = df_input.iloc[90000:100000]
    df_input_10 = df_input.iloc[100000:110000]
    df_input_sample = df_input_8
    
    # Second and more run of the program
    for row in df_input_sample.itertuples():
        # Log progress
        if (row.Index % 100 == 0):
            progress = (row.Index / len(df_input_sample)) * 100
            print(round(progress), r"% done.")
            
        sentence = str(df_input_sample.at[row.Index, "sentence"])
        try:
            t_iterator = parser.raw_parse(sentence)
            t_root = next(t_iterator)
            t = t_root[0]
            label = t.label()

            if label == "S":
                df_input.at[row.Index, "core_nlp_clause_tag"] = 1
            elif label == "SBAR":
                df_input.at[row.Index, "core_nlp_clause_tag"] = 2
            elif label == "SBARQ":
                df_input.at[row.Index, "core_nlp_clause_tag"] = 3
            elif label == "SINV":
                df_input.at[row.Index, "core_nlp_clause_tag"] = 4
            elif label == "SQ":
                df_input.at[row.Index, "core_nlp_clause_tag"] = 5
            else:
                df_input.at[row.Index, "core_nlp_clause_tag"] = 6
        except:
            print("An exception occurred with", sentence)
     

    # Write output file
    filename = "parsed_0.02_kept_threads_with_core_nlp_clause_tags.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH, filename]
    output_file = os.path.join('', *output_path)
    df_input.to_csv(output_file, sep=',', encoding='utf-8', index=False)
    




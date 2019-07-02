from sumy.summarizers.lex_rank import LexRankSummarizer 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer


class SummarizerTool(object):
    
    def __init__(self):
        self.lexRankSummarizer = LexRankSummarizer()
        pass

    def sentences_to_string(self, sentences):
        summary_string = ""
        for sentence in sentences:
            summary_string += "\n " + str(sentence)
        summary_string = summary_string[2:]
        return summary_string

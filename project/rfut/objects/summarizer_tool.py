from sumy.summarizers.lex_rank import LexRankSummarizer 
from sumy.summarizers.text_rank import TextRankSummarizer  
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from rfut.objects.sentence_parser import SentenceParser 

class SummarizerTool(object):
    
    def __init__(self):
        self.sp = SentenceParser()
        self.lexRankSummarizer = LexRankSummarizer()
        self.textRankSummarizer = TextRankSummarizer()
        self.sumBasicSummarizer = SumBasicSummarizer()
        pass

    def sentences_to_string(self, sentences):
        summary_string = ""
        for sentence in sentences:
            summary_string += "\n " + str(sentence)
        summary_string = summary_string[2:]
        #summary_string = self.sp.remove_quotes_symbols(summary_string)

        return summary_string

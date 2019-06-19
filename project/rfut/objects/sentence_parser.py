import re
from nltk import sent_tokenize

class SentenceParser(object):
    
    def __init__(self):
        pass

    def remove_links(self, text):
        return re.sub(r"https?://\S+", "" , text)

    def remove_special_characters(self, text):
        return re.sub(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " " , text)

    # TODO
    def replace_at_symbols(self,text):
        return re.sub(r"@", "at" , text)

    def clean_text(self, text):
        cleanned_text = self.remove_links(text)
        cleanned_text = self.remove_special_characters(cleanned_text)
        cleanned_text = self.replace_at_symbols(cleanned_text)
        # cleanned_text = cleanned_text.lower()
        return cleanned_text

    def parse_text_to_sentences(self, text):
        sentences = sent_tokenize(text)
        for i, sentence in enumerate(sentences):
            # Clean sentences text
            sentences[i] = self.clean_text(sentences[i])
        return sentences

    def alnum_count(self, string):
        count = 0
        for c in string:
            if c.isalnum():
                count = count + 1
        return count

    def word_count(self, string):
        return len(re.findall(r'\w+', string))
        # tokens = string.split()
        # n_tokens = len(tokens)
        # return n_tokens
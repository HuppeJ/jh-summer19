# Inspired from :
# - https://github.com/nltk/nltk/wiki/Stanford-CoreNLP-API-in-NLTK
# - https://bbengfort.github.io/snippets/2018/06/22/corenlp-nltk-parses.html
# - https://nbviewer.jupyter.org/github/gmonce/nltk_parsing/blob/master/1.%20NLTK%20Syntax%20Trees.ipynb

#%%
from nltk.parse import CoreNLPParser

# Lexical Parser
parser = CoreNLPParser(url='http://localhost:9000')

#%%
# Parse tokenized text.
# parse method to pass in tokenized and tagged text using other NLTK methods
temp = list(parser.parse('What is the airspeed of an unladen swallow ?'.split()))
print(temp)
# Output: [Tree('ROOT', [Tree('SBARQ', [Tree('WHNP', [Tree('WP', ['What'])]), Tree('SQ', [Tree('VBZ', ['is']), Tree('NP', [Tree('NP', [Tree('DT', ['the']), Tree('NN', ['airspeed'])]), Tree('PP', [Tree('IN', ['of']), Tree('NP', [Tree('DT', ['an']), Tree('JJ', ['unladen'])])]), Tree('S', [Tree('VP', [Tree('VB', ['swallow'])])])])]), Tree('.', ['?'])])])]

#%%
# Parse raw string.
# The raw_parse method expects a single sentence as a string
temp = list(parser.raw_parse('What is the airspeed of an unladen swallow ?'))
print(temp)
# Output: [Tree('ROOT', [Tree('SBARQ', [Tree('WHNP', [Tree('WP', ['What'])]), Tree('SQ', [Tree('VBZ', ['is']), Tree('NP', [Tree('NP', [Tree('DT', ['the']), Tree('NN', ['airspeed'])]), Tree('PP', [Tree('IN', ['of']), Tree('NP', [Tree('DT', ['an']), Tree('JJ', ['unladen'])])]), Tree('S', [Tree('VP', [Tree('VB', ['swallow'])])])])]), Tree('.', ['?'])])])]

#%%
# Neural Dependency Parser
from nltk.parse.corenlp import CoreNLPDependencyParser
dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
parses = dep_parser.parse('What is the airspeed of an unladen swallow ?'.split())
[[print(governor, dep, dependent) for governor, dep, dependent in parse.triples()] for parse in parses]
# Output: [[(('What', 'WP'), 'cop', ('is', 'VBZ')), (('What', 'WP'), 'nsubj', ('airspeed', 'NN')), (('airspeed', 'NN'), 'det', ('the', 'DT')), (('airspeed', 'NN'), 'nmod', ('swallow', 'VB')), (('swallow', 'VB'), 'case', ('of', 'IN')), (('swallow', 'VB'), 'det', ('an', 'DT')), (('swallow', 'VB'), 'amod', ('unladen', 'JJ')), (('What', 'WP'), 'punct', ('?', '.'))]]

#%%
# Tokenizer
parser = CoreNLPParser(url='http://localhost:9000')
temp = list(parser.tokenize('What is the airspeed of an unladen swallow?'))
print(temp)
# Output: ['What', 'is', 'the', 'airspeed', 'of', 'an', 'unladen', 'swallow', '?']

#%%
# POS Tagger
pos_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='pos')
temp = list(pos_tagger.tag('What is the airspeed of an unladen swallow ?'.split()))
print(temp)
# Output: [('What', 'WP'), ('is', 'VBZ'), ('the', 'DT'), ('airspeed', 'NN'), ('of', 'IN'), ('an', 'DT'), ('unladen', 'JJ'), ('swallow', 'VB'), ('?', '.')]

#%%
# NER Tagger
ner_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='ner')
temp = list(ner_tagger.tag(('Rami Eid is studying at Stony Brook University in NY'.split())))
print(temp)
# Output: [('Rami', 'PERSON'), ('Eid', 'PERSON'), ('is', 'O'), ('studying', 'O'), ('at', 'O'), ('Stony', 'ORGANIZATION'), ('Brook', 'ORGANIZATION'), ('University', 'ORGANIZATION'), ('in', 'O'), ('NY', 'STATE_OR_PROVINCE')]

#%%
# The parser actually returns a generator of parses, starting with the most likely. 
# By using next, we’re selecting only the first, most likely parse.
temp = next(parser.raw_parse("What is the longest river in the world?"))
print(temp)

#%%
# To get a Stanford dependency parse with Python:
# Constituency parses are deep and contain a lot of information, 
# but often dependency parses are more useful for text analytics and information extraction. 
from nltk.parse.corenlp import CoreNLPDependencyParser

parser = CoreNLPDependencyParser()
parse = next(parser.raw_parse("I put the book in the box on the table."))
#%%
from nltk.corpus import treebank
from nltk.parse import CoreNLPParser

parser = CoreNLPParser(url='http://localhost:9000')

t_iterator = parser.raw_parse('What is the airspeed of an unladen swallow ?')
t_root = next(t_iterator)
t = t_root[0]

label = t.label()

print("Tree: ", t)
print("Label: ", label)
#%%

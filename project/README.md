# Structure python project

https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6

- from omission.common.game_enums import GameMode
- from ..common.game_enums import GameMode
- from .game_round_settings import GameRoundSettings

## Classes

https://dev.to/codemouse92/dead-simple-python-classes-42f7

- @engine_strain.setter: uss_enterprise.engine_strain = 10

## Steps to work with Core NLP with NLTK

- Stanford CoreNLP API in NLTK: https://github.com/nltk/nltk/wiki/Stanford-CoreNLP-API-in-NLTK
- In the folder ```stanford-corenlp-full-2018-10-05``` start the server with in the Command Prompt :
  - ```java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer preload tokenize,ssplit,pos,lemma,ner,parse,depparse status_port 9000 -port 9000 -timeout 15000 &```
- In the Anaconda prompt execute script in the activated desired virtual environnement: 
  - ```scripts/test_core_nlp.py```

## Run project

- From the folder jh-summer19/project/ run in the anaconda prompt the command: 
- ```python -m rfut```

# Notes

Machine learning techniques can be used with following features,  

Sentence Starting with Wh word
Sentence starting with helping verb
Subject verb inversion
Presence of question mark
Context information for cases like "What he said was more important that what he accomplished.", in which sentence starts with Wh word but it is not actually interrogative sentence.

- Where can I find a dataset of sentences classified by type (interrogative, declarative. etc)? (Build your own by combining question with declarative sentences) https://www.quora.com/Where-can-I-find-a-dataset-of-sentences-classified-by-type-interrogative-declarative-etc s

## Sentence is a question? https://stackoverflow.com/questions/4083060/determine-if-a-sentence-is-an-inquiry

Finding out if a sentence is a question is not an easiest task, because there is many ways how people asks questions, many of them do not follows grammar rules. Therefore it is hard to find a good rule set for the detection. In such situations, I would go for machine learning and train an algorithm using annotated text corpus (creating a corpus and selecting a feature set can take some time). The machine learning based recognition should provide you better recall than the rule based approach. Here is a step by step instruction:

1. Manual creation of train data set: Get an annotated -- with information if it is a question or not -- text collection or create such a corpus on your own (it should be more then 100 documents and many questions must not be straightforward questions )
2. Find most important features - extract part-of-speeches, 5W1H (what, which,..., how), get a position of a verb in each of sentences, and other things that can be useful in the recognition of a question
3. Create a vector for each of sentences of features (you need both, positive and negative examples) based on the extracted information, e.g.,
| Has ? | A verb on second position | Has 5W1H | Is 5W1H on 1st position in sentence | ... | length of sentence | Is a question |
4. Use the vectors to train a machine learning algorithm, e.g., MaximumEntropy, SVM (you can use Wekka or Knime)
5. Use the trained algorithm for the question recognition.
6. If needed (new question examples), repeat steps.

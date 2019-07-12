# Evolution of the files through time

## 1. 0.02-of_threads_random_sample.csv: 

It contains the sample of threads extracted from the selected subforums (2% of threads of each selected subforums)
(see get_percentage_of_threads_data.py)
  
## 2. parsed_0.02_of_threads_to_sentences.csv: 

Took all the posts of 0.02-of_threads_random_sample.csv and parsed them into sentences 
(see parse_posts_to_sentences.py)

## 3. parsed_0.02_of_threads_to_sentences_with_stats.csv: 

Contains all the sentences of the parsed posts with additional info (nb. of words/sentence & nb. of alnum char/sentence)

Removed all the sentences from parsed_0.02_of_threads_to_sentences_with_stats.csv:

- with 0, 1 or 2 alnum characters
- that have 1 words and no question mark (?)
- that are matching one of the short_sentences_to_remove (see below)
(see remove_short_messages.py)
Which gave us the two files below:

## 4. parsed_0.02_of_threads_to_sentences_kept_sentences.csv

## 5. parsed_0.02_of_threads_to_sentences_removed_sentences.csv

After that, from parsed_0.02_of_threads_to_sentences_kept_sentences.csv, we removed the introduction threads threads starting with Hi, Hello, New here, etc. 
Note: those files are poorly named, we are not removing threads, but sentences.
(see remove_introduction_threads.py) 
Which gave us the two files below:
  
## 6. parsed_0.02_of_threads_kept_threads.csv

## 7. parsed_0.02_of_threads_removed_threads.csv

Tagged sentences of parsed_0.02_of_threads_kept_threads.csv with core_nlp_clause_tag with core_nlp parser which gave us:
(see core_nlp_interrogative_sentence_tagger.py)
Which gave us the file below:

## 7.1 parsed_0.02_kept_threads_with_core_nlp_clause_tags.csv

Tagged sentences of parsed_0.02_kept_threads_with_core_nlp_clause_tags.csv with is_question based on the core_nlp_clause_tags:
(see core_nlp_clause_tags_to_is_question.py)
Which gave us the file below:
  
## 8. parsed_0.02_kept_threads_with_is_question.csv

Tagged sentences of parsed_0.02_kept_threads_with_is_question.csv with has_annotations with keywords parser which gave us:
(see annotations_tagger.py)
Which gave us the file below:

## 9. parsed_0.02_kept_threads_with_is_question_and_annotations.csv

Took three random sample from parsed_0.02_kept_threads_with_is_question_and_annotations.csv

- Sample dataset #1: 3500 question sentences (is_question tag)
- Sample dataset #2: 3500 sentences that contains annotations and are not question sentences (!is_question and has_annotations tag)
- Sample dataset #3: 3500 sentences that do not contains annotations and are not question sentences (!is_question and !has_annotations tag)
(see sampler_for_mturk_no1.py)
Which gave us the file below:

## 10. sample_dataset_mturk_no1.csv

The dataset sample_dataset_mturk_no1.csv has been split into two datasets:

- One with 1000 sentences
- And the other one with the rest of the sentences (9500 sentences)
- (see pd_tools_dataframe_splitter.py)
- Which gave us the files below:

## 11. sample_0_to_999_dataset_mturk_no1.csv & sample_1000_to_10500_dataset_mturk_no1.csv

**When preparing the dataset for the text summarization there has been a mistake: the point "." character was removed from the text**
**In consequence, there is two groups of files below**

- **The text in the first group ("post") groups the text post by post, so when applying summarization techniques we get the best posts**
- **The text in the second group ("sent") groups the text sentence by sentence, so when applying summarization techniques we get the best sentences**

**First group ("post")**

- **Note: all the files in the first group have summaries of 2 to 10 posts**
  
For each thread_ids selected in the sample_dataset_mturk_no1.csv we retrieved all the thread conversation from 0.02-of_threads_random_sample.csv.
(get_datasets_for_summarization.py)
Which gave us the file below:

## 12. threads_text_for_summarization_post_no1.csv

Based on threads_text_for_summarization_post_no1.csv the thread text has been summarized using lexrank and the rouge-1 score has been directly calculated for summary of length 1 to 20 sentences. The goal was to see the trend between Scores in function of # of sentences in summary.  
(see thread_lexrank_summarizer_20_sent.py)

## 13. threads_post_summarized_rouge_1_scores_20_sent

- Based on threads_text_for_summarization_post_no1.csv the thread text has been summarized using lexrank, sumbasic and textrank: 
- (see thread_summarizer.py)

## 14 threads_post_summarized_lexrank.csv, threads_post_summarized_sumbasic.csv & threads_post_summarized_textrank.csv

- Based on threads_post_summarized_X.csv files the rouge-2 and rouge-3 scores has been calculated:
- (see thread_summary_rouge_scores.py) 

## 15 threads_post_summarized_lexrank_rouge_2_scores.csv, threads_post_summarized_sumbasic_rouge_2_scores.csv & threads_post_summarized_textrank_rouge_2_scores.csv

## 16 threads_post_summarized_lexrank_rouge_3_scores.csv, threads_post_summarized_sumbasic_rouge_3_scores.csv & threads_post_summarized_textrank_rouge_3_scores.csv

**Second group ("sent") [Good one]**

For each thread_ids selected in the sample_dataset_mturk_no1.csv we retrieved all the thread conversation from 0.02-of_threads_random_sample.csv.
(see get_datasets_for_summarization.py)
Which gave us the file below:

## 17. threads_text_for_summarization_no1.csv

For each thread we summarized the hole thread conversation (thread_text in threads_text_for_summarization_no1.csv) for x sentences x going from 1 to 50 sentences.
To generate those summaries different libraries has been used: 

- **threads_summarized_sumbasic_1_to_50.csv**: uses sumy library
- **threads_summarized_lexrank_1_to_50.csv**: uses sumy library
- **threads_summarized_textrank_1_to_50.csv**: uses modified TextRank algo of Gensim library (see: https://github.com/HuppeJ/gensim)
(see thread_summarizer.py)
Which gave us the files below:

## 18 threads_summarized_lexrank_1_to_50.csv, threads_summarized_sumbasic_1_to_50.csv & threads_summarized_textrank_1_to_50.csv

For clarity reason we removed the thread_text property in the files above so that the file could be opened in excel and easily visualized.
(see pd_tools_drop_column.py)
Which gave us the files below:

## 19 threads_summarized_lexrank_1_to_50_no_text.csv, threads_summarized_sumbasic_1_to_50_no_text.csv & threads_summarized_textrank_1_to_50_no_text.csv

Based on threads_summarized_X_1_to_50.csv files the rouge-1, rouge-2, rouge-3 and rouge-4 scores has been calculated:
(see thread_summary_rouge_scores.py) 
Which gave us the files below:

## 20 threads_summarized_lexrank_rouge_1_scores_1_to_50.csv, threads_summarized_sumbasic_rouge_1_scores_1_to_50.csv & threads_summarized_textrank_rouge_1_scores_1_to_50.csv

## 21 threads_summarized_lexrank_rouge_2_scores_1_to_50.csv, threads_summarized_sumbasic_rouge_2_scores_1_to_50.csv & threads_summarized_textrank_rouge_2_scores_1_to_50.csv

## 22 threads_summarized_lexrank_rouge_3_scores_1_to_50.csv, threads_summarized_sumbasic_rouge_3_scores_1_to_50.csv & threads_summarized_textrank_rouge_3_scores_1_to_50.csv

## 23 threads_summarized_lexrank_rouge_4_scores_1_to_50.csv, threads_summarized_sumbasic_rouge_4_scores_1_to_50.csv & threads_summarized_textrank_rouge_4_scores_1_to_50.csv

The TextRank summarization algorithm of sumy has also been ran. 
(see thread_summarizer.py)
Which gave us the files below:

## 24 threads_summarized_textrank_sumy_1_to_50.csv & threads_summarized_textrank_sumy_1_to_50_no_text.csv

Based on threads_summarized_textrank_sumy_1_to_50.csv files the rouge-2 and rouge-3 scores has been calculated:
(see thread_summary_rouge_scores.py) 
Which gave us the files below:

## threads_summarized_textrank_sumy_rouge_2_scores_1_to_50.csv & threads_summarized_textrank_sumy_rouge_3_scores_1_to_50.csv
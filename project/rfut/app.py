import time 

from rfut.scripts.core_nlp_interrogative_sentence_tagger import run as run_core_nlp_interrogative_sentence_tagger
from rfut.scripts.dataset_builder_get_percentage_of_threads_data import run as run_dataset_builder_get_percentage_of_threads_data
from rfut.scripts.parse_posts_to_sentences import run as run_parse_posts_to_sentences
from rfut.scripts.remove_short_messages import run as run_remove_short_messages
from rfut.scripts.get_synonyms import run as run_get_synonyms
from rfut.scripts.remove_introduction_threads import run as run_remove_introduction_threads
from rfut.scripts.annotations_tagger import run as run_annotations_tagger
from rfut.scripts.sampler_for_mturk_no1 import run as run_sampler_for_mturk_no1
from rfut.scripts.pd_tools_dataframe_splitter import run as run_pd_tools_dataframe_splitter
from rfut.scripts.test_bert_extractive_summarizer import run as run_test_bert_extractive_summarizer
from rfut.scripts.get_datasets_for_summarization import run as run_get_datasets_for_summarization
from rfut.scripts.test_lexrank_summarizer_with_lexrank import run as run_test_lexrank_summarizer_with_lexrank
from rfut.scripts.test_lexrank_summarizer_with_sumy import run as run_test_lexrank_summarizer_with_sumy
from rfut.scripts.pd_tools_drop_column import run as run_pd_tools_drop_column
from rfut.scripts.thread_lexrank_summarizer_20_sent import run as run_thread_summarizer_20_sent
from rfut.scripts.thread_summarizer import run as run_thread_summarizer
from rfut.scripts.thread_summary_rouge_scores import run as run_thread_summary_rouge_scores
from rfut.scripts.dataset_builder_posts_to_sentences import run as run_dataset_builder_posts_to_sentences
from rfut.scripts.dataset_builder_first_posts import run as run_dataset_builder_first_posts
from rfut.scripts.dataset_builder_add_subforum_number_to_i_csv_files import run as run_dataset_builder_add_subforum_number_to_i_csv_files
from rfut.scripts.core_nlp_clause_tags_to_is_question import run as run_core_nlp_clause_tags_to_is_question
from rfut.scripts.update_mturk_sample import run as run_update_mturk_sample
from rfut.scripts.add_sentence_id_to_dataset import run as run_add_sentence_id_to_dataset
from rfut.scripts.group_n_sentences_in_one_row_for_mturk import run as run_group_n_sentences_in_one_row_for_mturk
from rfut.scripts.parse_mturk_no2_results import run as run_parse_mturk_no2_results
from rfut.scripts.count_duplicate_sentences_in_summaries import run as run_count_duplicate_sentences_in_summaries
from rfut.scripts.summaries_to_sentences import run as run_summaries_to_sentences
from rfut.scripts.sampler_for_summaries import run as run_sampler_for_summaries



def run():
    start_time = time.time()
    print("Project R.F.U.T. is running!")
    run_pd_tools_dataframe_splitter()
    print("--- %s seconds ---" % (time.time() - start_time))

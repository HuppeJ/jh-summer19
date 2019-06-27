import time 

from rfut.scripts.core_nlp_interrogative_sentence_tagger import run as run_core_nlp_interrogative_sentence_tagger
from rfut.scripts.get_percentage_of_threads_data import run as run_get_percentage_of_threads_data
from rfut.scripts.parse_posts_to_sentences import run as run_parse_posts_to_sentences
from rfut.scripts.remove_short_messages import run as run_remove_short_messages
from rfut.scripts.get_synonyms import run as run_get_synonyms
from rfut.scripts.remove_introduction_threads import run as run_remove_introduction_threads
from rfut.scripts.annotations_tagger import run as run_annotations_tagger
from rfut.scripts.sampler_for_mturk_no1 import run as run_sampler_for_mturk_no1
from rfut.scripts.pd_tools_dataframe_splitter import run as run_pd_tools_dataframe_splitter

def run():
    start_time = time.time()
    print("Project R.F.U.T. is running!")
    run_pd_tools_dataframe_splitter()
    print("--- %s seconds ---" % (time.time() - start_time))

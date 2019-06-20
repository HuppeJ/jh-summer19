import time 

from rfut.scripts.find_questions_with_coreNLP import run as run_find_questions_with_coreNLP
from rfut.scripts.get_percentage_of_threads_data import run as run_get_percentage_of_threads_data
from rfut.scripts.parse_posts_to_sentences import run as run_parse_posts_to_sentences
from rfut.scripts.remove_short_messages import run as run_remove_short_messages
from rfut.scripts.get_synonyms import run as run_get_synonyms
from rfut.scripts.remove_introduction_threads import run as run_remove_introduction_threads

def run():
    start_time = time.time()
    print("Project R.F.U.T. is running!")
    run_remove_introduction_threads()
    print("--- %s seconds ---" % (time.time() - start_time))

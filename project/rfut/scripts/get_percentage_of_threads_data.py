import os
from rfut.common.constants import DIABETES_DATA_PATH, SUBORUMS_DATA_PATH

def run():
    print("Running : get_percentage_of_threads_data")

    # Get the selected subforums
    path = [DIABETES_DATA_PATH, SUBORUMS_DATA_PATH, "subforum_updated_classified.csv"]
    subforum_file = os.path.join('', *path)
    print(subforum_file)

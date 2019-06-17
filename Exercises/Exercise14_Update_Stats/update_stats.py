#%%
import os, csv, json, sys
import pandas as pd

dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise14_Update_Stats"
input_file_name = r"\counts_v2.csv"
df = pd.read_csv(dir_path + input_file_name)

# Adding new column nb_threads_updated_column
nb_threads_updated_column = "nb_threads_updated"
df[nb_threads_updated_column] = 0

# Adding new column subforum_nb_posts_updated_column
subforum_nb_posts_updated_column = "subforum_nb_posts_updated"
df[subforum_nb_posts_updated_column] = 0

# TODO: update nb threads if needed...
#nb_threads_rootdir=r"C:\Users\jerem\Desktop\test_update_stats"
#for subdir, dirs, files in os.walk(rootdir):
#    for file in files:
#        fileInput = subdir + os.sep + file
#        if fileInput.endswith(".csv"):
#            df_input = pd.read_csv(fileInput)
#            filename = file[:-4]
#            nb_rows = len(df_input)
#            row_index = int(filename) - 1
#            df.at[row_index, nb_threads_updated_column] = nb_rows


# Updating nb of posts 

# Note: Greeting and introduction at index 0 but filename is 1.csv so row_index = filename - 1 
# df["subforum_title"][0]

subforum_nb_posts_rootdir=r"C:\Users\jerem\Documents\internship_summer_19\data_scraped\diabetes.co.uk\threads_data\data"
for subdir, dirs, files in os.walk(subforum_nb_posts_rootdir):
    for file in files:
        fileInput = subdir + os.sep + file
        if fileInput.endswith(".csv"):
            df_input = pd.read_csv(fileInput)
            filename = file[:-4]
            nb_rows = len(df_input)
            row_index = int(filename) - 1
            df.at[row_index, subforum_nb_posts_updated_column] = nb_rows


output_file_name = r"\counts_v3_updated.csv"
df.to_csv(dir_path + output_file_name, sep=',', encoding='utf-8')



#%%

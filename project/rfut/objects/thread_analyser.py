import pandas as pd

class ThreadAnalyzer(object):
    
    def __init__(self):
        pass

    def get_list_of_sent_for_each_thread(self, df):
        thread_ids = df["thread_id"].unique()
        dict_list_of_sent = dict.fromkeys(thread_ids, []) 
        for thread_id in thread_ids:
            df_temp = df.loc[df["thread_id"] == thread_id]
            for row in df_temp.itertuples():
                sentence = str(df_temp.at[row.Index, "sentence"])
                dict_list_of_sent[thread_id] = dict_list_of_sent[thread_id] + [sentence]
        return dict_list_of_sent

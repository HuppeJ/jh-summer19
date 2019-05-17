
#%% [markdown]
## Extracting Sentences Containing Requirements Keywords

#%% 
import csv
import os
#%% 


dir_path = os.path.dirname(os.path.realpath("__file__"))

print(dir_path)

dir_path = "c:\Users\jerem\Desktop\jh-summer19\Exercices\Exercice2_Extracting_Sentences_Containing_Requirements_Keywords"


with open(dir_path + "/diabetesForumTestQuestionData.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)

#%%

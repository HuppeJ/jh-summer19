
#%% [markdown]
## Extracting Subforum links

#%% 
import csv

#%%
# Open question database csv file
dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise11_Extract_\scrapyDiabetesForum\getAllSubforumLinks"
input_file_name = r"\counts_v2_totals.csv"

with open(dir_path + input_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    subforumlinks = []
    for row in csv_reader:
        subforumLink = row[3]
        print(subforumLink)
        subforumlinks.append(subforumLink)

print(str(subforumlinks))


#%%

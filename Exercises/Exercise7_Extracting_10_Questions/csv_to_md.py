
#%% [markdown]
## .csv to .md
#%% 
import csv

dir_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise7_Extracting_10_Questions"


number_of_file = 10

for i in range(number_of_file) :
    input_file_name = "\question" + str(i + 1) + ".csv"
    output_file_name = "\question" + str(i + 1) + ".md"

    with open(dir_path + input_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Creating a dictionary with all the sentences of every question
        # data_dict = {"thread_id": sentences of question } 
        with open(dir_path + output_file_name, mode='w', encoding="utf-8", newline='') as md_file:
            for row in csv_reader:
                name = row[0].strip()
                content = row[1].strip()
                if name == "id":
                    pass
                elif name == "title":
                    md_file.write("# " + name + ": " + content + "\n\n")
                else:
                    md_file.write("**" + name + "**" +"\n\n")
                    md_file.write(content + "\n\n")



    

#%%

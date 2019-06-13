#%%
import pandas as pd
file_path = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise13_Extract_Interrogative_Sentences\4_sample_set.csv"
output_sample_10_filename = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise13_Extract_Interrogative_Sentences\4_sample_10.csv"
output_sample_100_filename = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise13_Extract_Interrogative_Sentences\4_sample_100.csv"
output_sample_1000_filename = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise13_Extract_Interrogative_Sentences\4_sample_1000.csv"
output_sample_10000_filename = r"C:\Users\jerem\Desktop\jh-summer19\Exercises\Exercise13_Extract_Interrogative_Sentences\4_sample_10000.csv"

df = pd.read_csv(file_path)
sample = df.sample(10000)
sample.to_csv(output_sample_10000_filename, sep=',', encoding='utf-8')

print(sample) #whatever number of random sample size you want


#%%

# Description of Exercises

Several proofs of concept have been developed to evaluate different ideas. All of these proofs of concept have been grouped under different exercises. The code and datasets of all these exercises can be found in the `jh-summer19/Exercises` folder. The description of each exercise can be found below. 

After analysis, certain proof of concept were selected. The code for these exercises has been refactored and restructured as part of a project called *rfut* see folder `jh-summer19/project`.

The code of each exercises follow the Jupyter Notebooks in Visual Studio Code structure, see documentation [here](https://code.visualstudio.com/docs/python/jupyter-support).

## Exercise1_Extracting_Data_From_Forum

Simple script to retrieve one specific page of the diabetes forum.

## Exercise2_Extracting_Sentences_Containing_Requirements_Keywords

First version of script identifying sentences with requirement keywords (syn. of need keywords and annotations).

## Exercise3_Extracting_Data_set_From_Forum

First script using [scrapy](https://scrapy.org/) to extract data from web pages. Script to extract the first post (named *question post*) of all threads of a sub-forum.

## Exercise4_Extracting_Requirements_Sentences_Questions

Script to identify the requirement sentences in the *question posts* (first posts).

## Exercise5_Creating_Labelled_Datasets

Parsed the question posts to sentences and tagged them with "is requirement sentence".

## Exercise6_Concrete_NLP_Tutorial_Adapted

NLP tutorial.

## Exercise7_Extracting_10_Questions

Script able to extract all the posts of a thread.

## Exercise8_Adding_The_New_Annotations

Script that finds the synonyms of a list of annotations (requirement keywords / need keywords) 

## Exercise9_New_Requirements_Sentence_Parser

Improved the requirement sentence parser.

## Exercise10_Extract_Number_of_Threads_and_Comments

Script using [scrapy](https://scrapy.org/) to extract from the diabetes forum homepage the number of threads and the number of comments in each sub-forums.

## Exercise11_Extract_Threads

Scripts using [scrapy](https://scrapy.org/) to extract all the threads and all the posts of the diabetes forum.

## Exercise12_JSON_to_CSV

Script that converts data extracted from the diabetes forum from JSON datasets into CSV datasets. 

## Exercise13_Creating_Sample_Datasets

Script that can sample from a .CSV dataset.

## Exercise14_Update_Stats

Script that updates the data retrieved at *Exercise10_Extract_Number_of_Threads_and_Comments* based on the data collected at *Exercise11_Extract_Threads*.

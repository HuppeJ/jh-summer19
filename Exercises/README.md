# Description of Exercises

At the beginning of the internship I decided to group the different analysis in multiple exercises as proof of concept. The code and datasets of all those exercises can be fin under the folder `jh-summer19/Exercises`. The description of those exercises can be found in this file. After analysis, certain proof of concept have been selected. The code of those exercises have been refactored and restructured under a project called rfut see folder `jh-summer19/project`.

## Exercise1_Extracting_Data_From_Forum

Simple script to retrieve one specific page of the diabetes forum.

## Exercise2_Extracting_Sentences_Containing_Requirements_Keywords

First version of script for identifying sentences with requirement keywords which are synonyms of need keywords and annotations.

## Exercise3_Extracting_Data_set_From_Forum

First script using scrapy to extract data from web pages. Script to extract the first post (named _question_) of all threads of a sub-forum.

## Exercise4_Extracting_Requirements_Sentences_Questions

Script to identify the requirement sentences in the question posts (first posts).

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

Script using scrapy to extract from the diabetes forum welcome age the number of threads and the number of comments in each subforum.

## Exercise11_Extract_Threads

Scripts using scrapy to extract all the threads and all the posts of the diabetes forum.

## Exercise12_JSON_to_CSV

Script able to convert the extracted data of the diabetes forum from JSON to CSV datasets. 

## Exercise13_Creating_Sample_Datasets

Script able to sample from a .CSV dataset.

## Exercise14_Update_Stats

Script that updated the data retrieved at Exercise10_Extract_Number_of_Threads_and_Comments based on the data collected at Exercise11_Extract_Threads.

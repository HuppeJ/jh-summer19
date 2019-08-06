# Software Requirements from Unstructured Text

This repository presents the source code of the project **Software Requirements from Unstructured Text**. 

I started the project **Software Requirements from Unstructured Text** during my 2019 summer internship. The goal of this project is to find needs expressed in unstructured conversations and mapped them to software requirements. 

The final code of the project can be found under the folder `jh-summer19/project`.

## First Steps of the Project

### Identify needs in sentences

1. Retrieve conversations from forums
   - Parse the conversations into sentences and create new datasets
2. Identify if a sentence expresses a need
   - Create a dataset with sentences labelled with 1 and 0:
     -  1: indicates that the sentence expresses a need 
     -  0: indicates that the sentence expresses a need 
   - Create training set and a test set
   - Train a classifier on the labelled dataset
3. Identify the need in a sentence

### Identify needs in posts

1. Retrieve conversations from forums
   - Parse the conversations into posts and create new datasets
2. Identify if a posts expresses a need
   - Create a dataset with posts labelled with 1 and 0:
     -  1: indicates that there is a need expressed in the post 
     -  0: indicates that there is no need expressed in the post 
   - Create training set and a test set
   - Train a classifier on the labelled dataset
3. Identify the need in a post

### Identify needs in thread summaries

1. Retrieve conversations from forums
   - Parse the conversations into threads and create new datasets
2. Identify best summarization technique
   - Generate summaries of threads with multiple extractive summarization algorithms
   - Evaluate summaries with ROUGE metric
3. Identify optimal summary length for threads
   - Generate multiple summaries of different length
   - Evaluate summaries with ROUGE metric
4. Identify if a thread summary expresses a need.
   - Create a dataset with summaries labelled with 1 and 0:
     -  1: indicates that there is a need expressed in the summary
     -  0: indicates that there is no need expressed in the summary
   - Create training set and a test set
   - Train a classifier on the labelled dataset.
5. Identify the need in a thread summary.


## Project Setup 

1. Open an Anaconda Prompt
2. Navigate to the repository root: `.../jh-summer19/`
3. In the repository root run the command: `conda env create -f environment.yml`
4. In the Anaconda Prompt activate the newly created virtual environment with the command `activate rfut_env`
5. Navigate to the project folder `.../jh-summer19/project/`
6. Select the desired script to run in *app.py*: `.../jh-summer19/project/rfut/app.py`
7. In the Anaconda Prompt run the command `python -m rfut`


## Repository Structure

- **conferences2019 Folder**: Contains all the notes and workshops from the conferences I attempted during my internship.
- **Exercises Folder**: Contains all the the proof of concepts developed. 
- **journal Folder**: Contains a detailed journal of the research process.
- **papers Folder**: Contains relevant papers and summaries of those papers.
- **plan**: Contains the project plan. 
- **project**: Contains the final _Software Requirements from Unstructured Text_ project's code

## Author

- Jérémie Huppé - Polytechnique Montréal - [jeremie.huppe@polymtl.ca](mailto:jeremie.huppe@polymtl.ca)
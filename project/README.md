# Software Requirements from Unstructured Text

## Project Setup 

1. Open an Anaconda Prompt
2. Navigate to the repository root: `.../jh-summer19/`
3. In the repository root run the command: `conda env create -f environment.yml`
4. In the Anaconda Prompt activate the newly created virtual environment with the command `activate rfut_env`
5. Navigate to the project folder `.../jh-summer19/project/`
6. Select the desired script to run in *app.py*: `.../jh-summer19/project/rfut/app.py`
7. In the Anaconda Prompt run the command `python -m rfut`

## Project Structure

- **common**: Contains files used in all the project.
- **data_output**: Contains all the datasets outputted from the scripts.
- **graphs**: Contains all the graphs generated to represent the datasets.
- **notebooks**: Contains jupyter notebooks with statistics and representations of the datasets.
- **objects**: Contains python objects used in the scripts. 
- **scripts**: Contains all the scripts developed to retrieve, parse and analyse the datasets.

_The project's structure has been inspired from [this article](https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6.)_



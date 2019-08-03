# Based on:
# - https://gist.github.com/danemacaulay/c8e3194b63570de1cf88f431ade32107
# - https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f
# - https://www.datacamp.com/community/tutorials/random-forests-classifier-python
# - https://medium.com/@tenzin_ngodup/simple-text-classification-using-random-forest-fe230be1e857
# - https://stackoverflow.com/questions/30653642/combining-bag-of-words-and-other-features-in-one-model-using-sklearn-and-pandas
# Imblearn Under-sampling: 
#   - https://imbalanced-learn.readthedocs.io/en/stable/under_sampling.html
#   - https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets#t72
#   - https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.under_sampling.RandomUnderSampler.html


# Imports
import csv
import os
import re
import pandas as pd
from rfut.common.constants import PROJECT_PATH, DATA_OUTPUT_PATH
from sklearn.model_selection import train_test_split
#Import scikit-learn dataset library
from sklearn import datasets
#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import scipy as sp
from imblearn.under_sampling import RandomUnderSampler

# Results: 

# With only bow feature and n_estimators=10: Accuracy = 0.795705725699068

# Balance 0 and 1 
# 10-fold
# precision / recall / f-score
# feature selection: PCA mrmr

def run():
    #Load dataset
    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "mturk", "submission_mturk_no2", "results", "dataset_for_classifier.csv"]
    input_file = os.path.join("", *file_path)
    df_data = pd.read_csv(input_file)

    

    # Init objects
    rus = RandomUnderSampler(return_indices=True)
    vectorizer = CountVectorizer(min_df=1)
    nb_estimators = 10

    # Features
    selected_features = df_data[[
        #"core_nlp_clause_tag", 
        #"nb_alnum_characters", 
        #"nb_alnum_characters", 
        #"nb_words", 
        "is_question_num",
        "has_annotations_num",
        #"sentence_number",
        #"subforum_number",
    ]]

    # For one feature
    # X = vectorizer.fit_transform(df_data["sentence"].values)

    # For multiple features
    X = sp.sparse.hstack((vectorizer.fit_transform(df_data["sentence"].values), selected_features.values), format="csr")

    X_columns = selected_features.columns.tolist()

    # Labels
    y = df_data["expresses_a_need_final"].values

    # Resample to have the same number of sentences that express a need and sentences that don't
    # X_resampled, y_resampled = rus.fit_resample(X, y)

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test

    # Create a Gaussian Classifier 
    clf = RandomForestClassifier(n_estimators=nb_estimators)
    
    # Train the model using the training sets
    clf.fit(X_train, y_train)

    # Get prediction
    y_pred = clf.predict(X_test)

    # Get accuracy score
    accuracy_score = metrics.accuracy_score(y_test, y_pred)

    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:", accuracy_score)


    # Export prediction 
    df_test_results = pd.DataFrame()
    df_test_results["y_test"] = y_test
    df_test_results["y_pred"] = y_pred

    feature_names_string = "_".join(X_columns)
    feature_names_string = "_bow_" + feature_names_string + "_" 

    # Write output file
    filename = "classifier_random_forest_" + feature_names_string + "_prediction_example_" + str(round(accuracy_score, 4)) + "_accuracy.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH,  "mturk", "submission_mturk_no2", "results", "classifier_results", filename]
    output_file = os.path.join("", *output_path)
    df_test_results.to_csv(output_file, sep=",", encoding="utf-8", index=False)


    #feature_imp = pd.Series(clf.feature_importances_,index=iris.feature_names).sort_values(ascending=False)

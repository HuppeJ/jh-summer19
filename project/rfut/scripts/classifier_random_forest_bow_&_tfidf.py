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
# - https://stackoverflow.com/questions/47464067/how-to-predict-labels-using-cross-validation-kfold-with-sklearn

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
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict, KFold, cross_val_score, cross_validate
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score
import scipy as sp
from imblearn.under_sampling import RandomUnderSampler


# Results: 

# With only bow feature and n_estimators=10: Accuracy = 0.795705725699068

# Balance 0 and 1 
# 10-fold
# precision / recall / f-score
# feature selection: PCA mrmr

def run():
    #####################################
    # Load dataset
    #####################################

    file_path = [PROJECT_PATH, DATA_OUTPUT_PATH, "mturk", "submission_mturk_no2", "results", "dataset_for_classifier.csv"]
    input_file = os.path.join("", *file_path)
    df_data = pd.read_csv(input_file)

    
    #####################################
    # Init objects
    #####################################
    rus = RandomUnderSampler(random_state=42)

    # vectorizer = CountVectorizer(min_df=1)
    vectorizer = TfidfVectorizer()
    
    nb_estimators = 10
    simple_prediction = False


    #####################################
    # Features
    #####################################

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
    #X = vectorizer.fit_transform(df_data["sentence"].values)

    # For multiple features
    X = sp.sparse.hstack((vectorizer.fit_transform(df_data["sentence"].values), selected_features.values), format="csr")

    X_columns = selected_features.columns.tolist()

    # Labels
    y = df_data["expresses_a_need_final"].values

    print("X.shape: ", X.shape)
    print("y.shape: ", y.shape)


    #####################################
    # Resampling
    #####################################

    # Resample to have the same number of sentences that express a need and sentences that don"t
    X_resampled, y_resampled = rus.fit_resample(X, y)


    print("X_resampled.shape: ", X_resampled.shape)
    print("y_resampled.shape: ", y_resampled.shape)
 

    #####################################
    # Create training set and test set
    #####################################

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test

    print("X_train.shape: ", X_train.shape)
    print("y_train.shape: ", y_train.shape)

    print("X_test.shape: ", X_test.shape)
    print("y_test.shape: ", y_test.shape)
 

    #####################################
    # Create Classifier 
    #####################################

    clf = RandomForestClassifier(n_estimators=nb_estimators)
    
    # **Train the model using the training sets**
    # clf.fit(X_train, y_train)

    # **Get Prediction**

    ## Simple prediction with no cross-validation
    # simple_prediction = True
    # y_pred = clf.predict(X_test)

    ## **Get accuracy score**
    # accuracy_score = metrics.accuracy_score(y_test, y_pred)
    # print("Accuracy:", accuracy_score)


    ## **Gey Prediction with k-fold cross-validation**
    nb_of_folds = 10
    kfold = KFold(n_splits=nb_of_folds)
    y_pred = cross_val_predict(clf, X_resampled, y_resampled, cv=kfold)
    print("y_pred.shape: ", y_pred.shape)

    ## **Get scoring**

    #coring = {"accuracy" : make_scorer(accuracy_score), 
    #           "precision" : make_scorer(precision_score),
    #           "recall" : make_scorer(recall_score), 
    #           "f1_score" : make_scorer(f1_score)}

    scoring = {"accuracy": "accuracy",
               "precision": "precision",
               "recall": "recall",
               "f1" : "f1"
           }

    results = cross_validate(estimator=clf, X=X_resampled, y=y_resampled, cv=kfold, scoring=scoring)
    print (list(results.keys()))
    print("Model scores: ")
    print("accuracy: ", np.mean(results["test_accuracy"]), " ± ", np.std(results["test_accuracy"]))
    print("precision: ", np.mean(results["test_precision"]), " ± ", np.std(results["test_precision"]))
    print("recall: ", np.mean(results["test_recall"]), " ± ", np.std(results["test_recall"]))
    print("f1: ", np.mean(results["test_f1"]), " ± ", np.std(results["test_f1"]))

    accuracy_score = np.mean(results["test_accuracy"])

    # Create scores dataframe to write in csv file the scores
    df_scores = pd.DataFrame()

    df_scores["score"] = ""
    df_scores["mean"] = 0
    df_scores["std"] = 0

    df_scores.loc[len(df_scores)] = ["accuracy", np.mean(results["test_accuracy"]), np.std(results["test_accuracy"])]
    df_scores.loc[len(df_scores)] = ["precision", np.mean(results["test_precision"]), np.std(results["test_precision"])]
    df_scores.loc[len(df_scores)] = ["recall", np.mean(results["test_recall"]), np.std(results["test_recall"])]
    df_scores.loc[len(df_scores)] = ["test_f1", np.mean(results["test_f1"]), np.std(results["test_f1"])]


    # Export prediction 
    df_test_results = pd.DataFrame()
    if simple_prediction:
        df_test_results["y_test"] = y_test
    else:
        df_test_results["y_resampled"] = y_resampled
    df_test_results["y_pred"] = y_pred


    feature_names_string = "_".join(X_columns)
    # TODO: Change name of vectorizer (bow vs tfidf)
    feature_names_string = "_tfidf_" + feature_names_string + "_" 

    # Write output file
    filename = "classifier_random_forest_" + feature_names_string + "prediction_example_" + str(round(accuracy_score, 4)) + ".csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH,  "mturk", "submission_mturk_no2", "results", "classifier_results", filename]
    output_file = os.path.join("", *output_path)
    df_test_results.to_csv(output_file, sep=",", encoding="utf-8", index=False)

    filename = "classifier_random_forest_" + feature_names_string + "prediction_example_" + str(round(accuracy_score, 4)) + "_scores.csv"
    output_path = [PROJECT_PATH, DATA_OUTPUT_PATH,  "mturk", "submission_mturk_no2", "results", "classifier_results", filename]
    output_file = os.path.join("", *output_path)
    df_scores.to_csv(output_file, sep=",", encoding="utf-8", index=False)

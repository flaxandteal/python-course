#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test learning algorithms on the classic Iris dataset.

@author: Phil Weir <phil.weir@flaxandteal.co.uk>
@license: MIT
"""

import os
import numpy as np
import pandas

from sklearn import svm

from sklearn import datasets
from pandas.plotting import scatter_matrix

def run():
    # Why is this if-statement here? Why don't we just use lines 21-22?
    if not os.path.exists('iris.data'):
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        df = pandas.read_csv(url, header=None)
        df.to_csv('iris.data', header=False, index=False)
    
    df = pandas.read_csv('./iris.data', header=None)
    
    # When you are happy with what this looks like, remove it!
    print(df)

    # Why is this important?
    reordering = np.random.permutation(df.index)
    df = df.reindex(reordering)
    
    # This is the set of inputs
    X_training = df.iloc[:-30, :-1]
    # This is the known classifiers
    y_training_target = df.iloc[:-30, -1]
    
    # This set we will use for testing the model
    X_testing = df.iloc[-30:, :-1]
    # We will measure our predictions against these
    y_testing_target = df.iloc[-30:, -1]
    
    # Make a model
    classifier = svm.SVC(kernel='linear', C=1).fit(X_training, y_training_target)
    
    # Evaluate it
    score = classifier.score(X_testing, y_testing_target)
    print(score)
    
    # What type of flower is an iris with:
    #   Sepal length: 4.7cm
    #   Sepal width: 3.4cm
    #   Petal length: 1.1cm
    #   Petal width: 0.2cm
    # ?
    samples = [
        [4.7, 3.4, 1.1, 0.2]
    ]
    print(classifier.predict(samples))
    
    # TASKS
    #------
    # 0 - What, in words, is each slicing operation doing?
    #
    # 1 - Download the CSV and open it from the same folder as script (still with read_csv)
    
    # 2 - Add plots of sepal length, sepal width, petal length and petal width using Pandas'
    #      - scatter_matrix (hint: create a dataframe with those four columns)
    #      - RadViz (familiar looking dataset on the Pandas manual page!)
    
    # 3 - Switch to using "test_train_split" instead of using "-30" and slicing
    
    # 4 - Instead of using "score", use "cross_val_score": http://scikit-learn.org/stable/modules/cross_validation.html#cross-validation

if __name__ == "__main__":
    run()

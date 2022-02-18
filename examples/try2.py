# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:27:36 2021

@author: Lenovo
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss, accuracy_score
from gama import GamaClassifier
import openml

if __name__ == "__main__":
#    X, y = load_breast_cancer(return_X_y=True)
    dataset = openml.datasets.get_dataset(1596)
    X, y, categorical_indicator, attribute_names = dataset.get_data(
            dataset_format='dataframe', target=dataset.default_target_attribute
            )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, random_state=0
    )

    automl = GamaClassifier(max_total_time=180, store="nothing", n_jobs=1)
    print("Starting `fit` which will take roughly 3 minutes.")
    automl.fit(X_train, y_train)

    label_predictions = automl.predict(X_test)
    probability_predictions = automl.predict_proba(X_test)

    print("accuracy:", accuracy_score(y_test, label_predictions))
    print("log loss:", log_loss(y_test, probability_predictions))
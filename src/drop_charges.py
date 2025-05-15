from data_csv import data
import pandas as pd
import numpy as np
from custom_pipeline import DropFeatureSelector
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer, MinMaxScaler, StandardScaler, PolynomialFeatures, Binarizer, KBinsDiscretizer, OrdinalEncoder
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.base import BaseEstimator, TransformerMixin
from data_csv import drop_dup, readcsv
import os

def train_test_creation(data):
    X= data.drop(['charges'], axis=1)
    y=data['charges']
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, train_size=0.85, random_state=42, stratify=X['smoker'])
    return X_train, X_test, y_train, y_test

if os.path.isfile('dataset.csv'):
    data = drop_dup(readcsv('dataset.csv'))

    X_train, X_test, y_train, y_test = train_test_creation(data)

    preprocessor = make_pipeline(DropFeatureSelector(),make_column_transformer((StandardScaler(), ['children','age']),
                                                        (OrdinalEncoder(), ['smoker', 'sex']), (OneHotEncoder(),['region',"BMI_cat"])), PolynomialFeatures(2))

    #Linear Regression

    model = make_pipeline(preprocessor, LinearRegression())

    # print(model.get_params())

    param_grid = {
        'pipeline__polynomialfeatures__degree': [1,2,3]
    }

    grid_search = GridSearchCV(
        model,
        param_grid,
        cv=5,
        scoring='r2'
    )

    grid_search.fit(X_train, y_train)
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer, MinMaxScaler, StandardScaler, PolynomialFeatures, Binarizer, KBinsDiscretizer, OrdinalEncoder
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.base import BaseEstimator, TransformerMixin


class DropFeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y = None):
        return self
    
    def get_feature_names_out(self, feature_names_out):
        return feature_names_out
    
    def fit_transform(self, X, y = None, **fit_params):
        return super().fit_transform(X, y, **fit_params)
    
    def transform(self, X):
        X_cop= X.copy()
        bins = [0,18,25,30,35,40,50,1000]
        labels=['sous poids','poids normal','surpoids','obésité modérée','obésité sévère','obésité morbide','obésité massive']
        X_cop['BMI_cat']=pd.cut(X_cop['bmi'], bins=bins, labels=labels, right=False)
        X_cop= X_cop.drop(['bmi'], axis=1)
        return X_cop

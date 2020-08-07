# -*- coding: utf-8 -*-
"""
@author: @mikegallimore
"""

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
import pickle
import parameters


###
### LOAD & SHAPE THE DATA
###

# set the location of the file with the seed data
shots_training_seasons = parameters.shots_training_seasons

# create a dataframe of the seed data; duplicate it and drop unneeded columns
shots_train_df = pd.read_csv(shots_training_seasons)
shots_df = shots_train_df.copy()

if shots_training_seasons == parameters.shots_train or shots_training_seasons == parameters.shots_train_small:
    shots_df = shots_df.drop(columns=parameters.drop_columns)


###
### GRADIENT BOOSTING
###

# set the independent variables
continuous_variables = parameters.continuous_variables
boolean_variables = parameters.boolean_variables
independent_variables = continuous_variables + boolean_variables
x = shots_df[independent_variables]

# set the dependent variable
y = shots_df['IS_GOAL']

# create the classifier
clf = GradientBoostingClassifier(n_estimators=60, learning_rate=0.1, max_depth=9, max_features=7, min_samples_split=400, min_samples_leaf=70, subsample=0.8, random_state=42, verbose=10)

# create hyperparameter options
param_grid = {}

# create grid search
cv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring='neg_log_loss', cv=10)

# fit grid search
cv.fit(x, y)

print("\nGradient Boosting Classifier:\n", cv)

# save model
pickle.dump(cv, open("pickle_gb.pkl", 'wb'))
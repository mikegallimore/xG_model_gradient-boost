# -*- coding: utf-8 -*-
"""
@author: @mikegallimore
"""

import pandas as pd
import matplotlib as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
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


# define the different stages
baseline = 'baseline'
stage_1 = 'stage_1'
stage_2 = 'stage_2'
stage_3 = 'stage_3'
stage_4 = 'stage_4'
stage_5 = 'stage_5'

# indicate whether to run the baseline or a particular stage
run = stage_5


### BASELINE
if run == baseline:
    # create the classifier
    clf = GradientBoostingClassifier(learning_rate=0.1, max_depth=3, random_state=42, verbose=10)

    # fit baseline model
    clf.fit(x, y)

    # gauge feature importance
    predictors=list(x)
    feat_imp = pd.Series(clf.feature_importances_, predictors).sort_values(ascending=False)
    feat_imp.plot(kind='bar', title='Importance of Features')
    plt.ylabel('Feature Importance Score')


### STAGE 1
if run == stage_1:
    # create the classifier
    clf = GradientBoostingClassifier(learning_rate=.1, max_depth=8, max_features='sqrt', min_samples_split=500, min_samples_leaf=50, subsample=0.8, random_state=42, verbose=10)
    
    # create hyperparameter options
    param_grid = {'n_estimators':range(20,81,10)}
    
    # create grid search
    cv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring='roc_auc', cv=5)
    
    # fit grid search
    cv.fit(x, y)
    
    print("\nGradient Boosting Classifier:\n", cv)
    
    print(cv.cv_results_, cv.best_params_, cv.best_score_)


### STAGE 2
if run == stage_2:
    # create the classifier
    clf = GradientBoostingClassifier(learning_rate=.1, max_features='sqrt', n_estimators=80, subsample=0.8, random_state=42, verbose=10)
    
    # create hyperparameter options
    param_grid = {'max_depth':range(5,16,2), 'min_samples_split':range(200,1001,200)}
    
    # create grid search
    cv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring='roc_auc', cv=5)
    
    # fit grid search
    cv.fit(x, y)
    
    print("\nGradient Boosting Classifier:\n", cv)
    
    print(cv.cv_results_, cv.best_params_, cv.best_score_)
    
    
### STAGE 3
if run == stage_3:
    # create the classifier
    clf = GradientBoostingClassifier(learning_rate=.1, max_depth=9, max_features='sqrt', min_samples_split=400, n_estimators=60, subsample=0.8, random_state=42, verbose=10)
    
    # create hyperparameter options
    param_grid = {'min_samples_leaf':range(30,71,10)}
    
    # create grid search
    cv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring='roc_auc', cv=5)
    
    # fit grid search
    cv.fit(x, y)
    
    print("\nGradient Boosting Classifier:\n", cv)
    
    print(cv.cv_results_, cv.best_params_, cv.best_score_)


### STAGE 4
if run == stage_4:
    # create the classifier
    clf = GradientBoostingClassifier(learning_rate=.1, max_depth=9, min_samples_split=400, min_samples_leaf=70, n_estimators=60, subsample=0.8, random_state=42, verbose=10)
    
    # create hyperparameter options
    param_grid = {'max_features':range(7,20,2)}
    
    # create grid search
    cv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring='roc_auc', cv=5)
    
    # fit grid search
    cv.fit(x, y)
    
    print("\nGradient Boosting Classifier:\n", cv)
    
    print(cv.cv_results_, cv.best_params_, cv.best_score_)
    

### STAGE 5
if run == stage_5:
    # create the classifier
    clf = GradientBoostingClassifier(learning_rate=.1, max_depth=9, max_features=7, min_samples_split=400, min_samples_leaf=70, n_estimators=60, random_state=42, verbose=10)
    
    # create hyperparameter options
    param_grid = {'subsample':[0.6,0.7,0.8,0.9,1.0]}
    
    # create grid search
    cv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring='roc_auc', cv=5)
    
    # fit grid search
    cv.fit(x, y)
    
    print("\nGradient Boosting Classifier:\n", cv)
    
    print(cv.cv_results_, cv.best_params_, cv.best_score_)

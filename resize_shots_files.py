# -*- coding: utf-8 -*-
"""
@author: @mikegallimore
"""

import pandas as pd


###
### TRAINING SHOTS
###

# set the location of the file with the seed data
shots_training_seasons = 'shots_train.csv'

# create a dataframe of the seed data
shots_train_df = pd.read_csv(shots_training_seasons)

# reduce the dataframe to 3 seasons of shots
shots_train_df = shots_train_df[(shots_train_df['SEASON'] > 20132014)]

# save the dataframe to a distinct file
shots_train_df.to_csv('shots_train_small.csv', index=False)


###
### TESTING SHOTS
###

# set the location of the file with the seed data
shots_testing_seasons = 'shots_test.csv'

# create a dataframe of the seed data
shots_testing_df = pd.read_csv(shots_testing_seasons)

# reduce the dataframe to 1 season of shots
shots_testing_df = shots_testing_df[(shots_testing_df['SEASON'] == 20182019)]

# save the dataframe to a distinct file
shots_testing_df.to_csv('shots_test_small.csv', index=False)
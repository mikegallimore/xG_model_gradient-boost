# -*- coding: utf-8 -*-
"""
@author: @mikegallimore
"""

# identify the different versions of training shot data; choose which version to use
shots_train = 'shots_train.csv'
shots_train_resampled = 'shots_train_resampled.csv'

shots_train_small = 'shots_train_small.csv'
shots_train_small_resampled = 'shots_train_small_resampled.csv'

shots_training_seasons = shots_train_small

# identify the different versions of training shot data; choose which version to use
shots_test = 'shots_test.csv'
shots_test_small = 'shots_test_small.csv'

shots_test_seasons = shots_test_small

# trim the dataframe
drop_columns = ['SEASON', 'GAME_ID', 'HOME', 'AWAY', 'PERIOD', 'SECONDS_LAST_EVENT', 'HOME_GOALS', 'AWAY_GOALS', 'HOME_SITUATION', 'AWAY_SITUATION', 'HOME_SCOREDIFF', 'AWAY_SCOREDIFF', 'HOME_STRENGTH', 'AWAY_STRENGTH', 'HOME_STATE', 'AWAY_STATE', 'EVENT', 'EVENT_TYPE', 'EVENT_DETAIL', 'HOME_ZONE', 'AWAY_ZONE', 'TEAM', 'X_1', 'Y_1', 'SHOOTER_NO', 'SHOOTER_POS', 'LAST_EVENT', 'LAST_EVENT_TYPE', 'LAST_EVENT_TEAM', 'LAST_EVENT_X_1', 'LAST_EVENT_Y_1', 'X_ADJ', 'Y_ADJ', 'ANGLE', 'LAST_EVENT_X_ADJ', 'LAST_EVENT_Y_ADJ', 'LAST_EVENT_ANGLE', 'LAST_EVENT_ANGLE_ABS', 'LAST_EVENT_DISTANCE', 'CHANGE_IN_ANGLE', 'IS_TEAM_HOME', 'IS_ON_NET']

# select the features
continuous_variables = ['SECONDS_GONE', 'X_ABS', 'Y_ABS', 'ANGLE_ABS', 'DISTANCE', 'DISTANCE_LAST_EVENT', 'SPEED_LAST_EVENT', 'SPEED_CHANGE_IN_ANGLE']
boolean_variables = ['IS_SHOOTER_POS_F', 'IS_REBOUND', 'IS_LAST_EVENT_TEAM_SHOT', 'IS_LAST_EVENT_OPP_SHOT', 'IS_LAST_EVENT_TEAM_FACEOFF', 'IS_LAST_EVENT_OPP_FACEOFF', 'IS_LAST_EVENT_TEAM_GIVEAWAY', 'IS_LAST_EVENT_OPP_GIVEAWAY', 'IS_LAST_EVENT_TEAM_TAKEAWAY', 'IS_LAST_EVENT_OPP_TAKEAWAY', 'IS_LAST_EVENT_OPP_HIT', 'IS_LAST_EVENT_TEAM_HIT', 'IS_TEAM_NET_EMPTY', 'IS_OPP_NET_EMPTY', 'IS_TEAM_UP_3_OR_MORE', 'IS_TEAM_UP_2', 'IS_TEAM_UP_1', 'IS_TEAM_TIED', 'IS_TEAM_DOWN_1', 'IS_TEAM_DOWN_2', 'IS_TEAM_DOWN_3_OR_MORE', 'IS_TEAM_5v5', 'IS_TEAM_4v4', 'IS_TEAM_3v3', 'IS_TEAM_5v4', 'IS_TEAM_5v3', 'IS_TEAM_4v3', 'IS_TEAM_4v5', 'IS_TEAM_3v5', 'IS_TEAM_3v4']

###
### SIMPLE
###

# trim the dataframe
simple_drop_columns = ['SEASON', 'GAME_ID', 'HOME', 'AWAY', 'PERIOD', 'SECONDS_LAST_EVENT', 'HOME_GOALS', 'AWAY_GOALS', 'HOME_SITUATION', 'AWAY_SITUATION', 'HOME_SCOREDIFF', 'AWAY_SCOREDIFF', 'HOME_STRENGTH', 'AWAY_STRENGTH', 'HOME_STATE', 'AWAY_STATE', 'EVENT', 'EVENT_TYPE', 'EVENT_DETAIL', 'HOME_ZONE', 'AWAY_ZONE', 'X_1', 'Y_1', 'SHOOTER_NO', 'SHOOTER_POS', 'LAST_EVENT', 'LAST_EVENT_TYPE', 'LAST_EVENT_TEAM', 'LAST_EVENT_Y_1', 'X_ADJ', 'Y_ADJ', 'LAST_EVENT_X_1', 'ANGLE', 'LAST_EVENT_X_ADJ', 'LAST_EVENT_Y_ADJ', 'LAST_EVENT_ANGLE', 'LAST_EVENT_ANGLE_ABS', 'LAST_EVENT_DISTANCE', 'CHANGE_IN_ANGLE', 'IS_TEAM_HOME', 'IS_ON_NET']
# select the features
simple_continuous_variables = ['ANGLE_ABS', 'DISTANCE', 'DISTANCE_LAST_EVENT', 'SPEED_LAST_EVENT', 'SPEED_CHANGE_IN_ANGLE']
simple_boolean_variables = ['IS_SHOOTER_POS_F', 'IS_REBOUND', 'IS_LAST_EVENT_TEAM_SHOT', 'IS_LAST_EVENT_TEAM_TAKEAWAY', 'IS_LAST_EVENT_OPP_GIVEAWAY']
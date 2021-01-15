import pandas
import json
import requests
import time
from sklearn.metrics import plot_confusion_matrix,roc_curve, confusion_matrix, plot_roc_curve 
import matplotlib.pyplot as plt
import seaborn as sns


    
def get_match_data(num_pulls, api_key) :
    """Pulls match data from OpenDota API, returns Pandas dataframe.
    
    Keyword Arguments:
    num_pulls -- integer number of API calls, pulls 100 matches at a time
    api_key -- API key to use for OpenDota API calls.
    
    Libraries needed: Pandas, json, requests, time
    """

    df = pandas.DataFrame()
    
    for x in range(num_pulls) :
        match_batch = requests.get('https://api.opendota.com/api/publicMatches?api_key={}'.format(api_key))
        df = df.append(pandas.DataFrame(match_batch.json()))
        time.sleep(0.07)
    
    df = df.drop_duplicates(subset = ['match_id'])
    return df

def add_hero_cols(df, column_name) :
    """Builds and appends a sparse data table at the end of a dataframe of Dota 2 Matches.
    
    Keyword Arguments:
    df -- Pandas Dataframe containing match data
    column_name -- the column of the team you are wishing to append
    
    Libraries needed: Pandas, json, requests, time
    """
    heroes = requests.get('https://api.opendota.com/api/constants/heroes')
    heroes = heroes.json()
    
    temp_df = df[column_name].str.split(pat = ',')
    hero_dict = {}
    
    for hero in heroes :
        heroes['{}'.format(hero)]['localized_name'].replace(' ', '_')
        hero_dict['{}_{}'.format( heroes['{}'.format(hero)]['localized_name'], column_name)] = []
    
    for team in temp_df :
        for hero in heroes :
            if hero in team :
                hero_dict['{}_{}'.format(heroes['{}'.format(hero)]['localized_name'], column_name)].append(1)
            else :
                hero_dict['{}_{}'.format(heroes['{}'.format(hero)]['localized_name'], column_name)].append(0)
    
    for hero in hero_dict :
        df[hero] = hero_dict[hero]
        
    df.drop(['{}'.format(column_name)], axis=1, inplace=True)
    
    return df

def plot_conf_matrix(title, y_pred, y_test):
    """Function to plot confusion matrix for the model
    Takes in 3 params; no return values
    title: a string for the model name
    y_pred: the predicted y values for the set
    y_test: the true y values for the set"""
        
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, cmap=plt.cm.copper, 
        xticklabels= ['Pred Radiant Win', 'Pred Dire Win'], 
        yticklabels=['True Radiant Win', 'True Dire Win'],
        fmt='d')
    plt.title("{} \n Confusion Matrix".format(title), fontsize=14)
    

def plot_roc(cm,X_train, y_train,X_test, y_test):
    """Function to plot ROC curve for the model
    Takes in 5 params; no return values
    cm: an estimator model object
    X_train: the features for the training set
    y_train: the true y values for the training set
    X_test: the features for the test set
    y_test: the true y values for the test set"""
    
    fig, axes = plt.subplots(1,2, figsize = (10,5), sharey = 'row')
    plot_roc_curve(cm, X_train, y_train, ax=axes[0])
    axes[0].plot([0, 1], [0, 1], color='red', lw=2, linestyle='--')
    axes[0].set_title("ROC Curve for Traning")
    
    plot_roc_curve(cm, X_test, y_test, ax=axes[1])
    axes[1].plot([0, 1], [0, 1], color='red', lw=2, linestyle='--')
    axes[1].set_title("ROC Curve for Testing")
    
    plt.show()
    

def metric_report(name, y, y_pred):
    """Function to print metrics for model performance
    Takes in 3 params; no return values
    name: a string for the model name
    y: the true y values for the set
    y_pred: the predicted y values for the set"""
    
    n_errors = (y_pred != y).sum()
    print("{} Number of Errors: {}".format(name,n_errors))
    print("Accuracy Score :")
    print(accuracy_score(y,y_pred))
    print("Classification Report :")
    print(classification_report(y,y_pred))
    
def get_test_match(match_id):
    match = requests.get('https://api.opendota.com/api/matches/{}'.format(match_id))
    match = match.json()
    
    match_dict = {'avg_mmr' : 0.25, 'radiant_team' : match['radiant_team'], 'dire_team' : match['dire_team']}
    
    df = pd.DataFrame(match_dict)
    df = add_hero_cols(df, 'radiant_team')
    df = add_hero_cols(df, 'dire_team')
    
    return df
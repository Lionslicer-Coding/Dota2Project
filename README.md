# Dota2Project
Capstone project for projecting Dota 2 match results

## Repository Contents

* README.md - This file, an overview of the project.
* capstonepresentation.pptx - A powerpoint presentation intended for a non-technical audience
* data_pull.ipynb - A short notebook used to document the process used to obtain the data used
* index.ipynb - The primary notebook housing data exploration and modeling
* match_data.csv - CZV containing basic information for ~32,000 Dota 2 matches
* project_funcs.py -  python file containing all functions used in our project
* sparse_table.csv - the sparse table generated for our models, intended for use in deployment of the model


## Introduction

For the better part of two decades, online multiplayer video games have been accruing massive player bases and forming competitive environments within them. These games span many different genres, and range from simple enough for children to complex enough to require thousands of hours of playtime to develop high level skills.

One such game is Dota 2, created by Valve Software. Launched in 2012, this game has maintained a strong following all the way to the present day, where there are at least 400,000 players online at any point in time. Given the stability of the player base, it's not surprising that it also enjoys a strong competitive scene, creating myriad opportunities for individuals to generate income from the game. It has also generated an appetite for strong predictive tools that allow for more confident analysis and betting predictions.

This project seeks to develop a strong predictive model for win probabilities of two teams, using only what is known prior to the start of a match.

## Model Conclusions

In this repository, we develop two separate models. The first is a Logistic Regression model, that scores well with an AUC of .86 on our training set and .84 on testing. Following that we used a Random Forest Classifier that scored a little better with an AUC of .91 on our training set and .90 on our testing set. Through the use of GridsearchCV we found a combination of parameters that boosted this performance to near perfect.

## Future Work

While our model did perform very well, there is much work left to be done. First, more thorough exploration of our data set could bring up valuable insights into why matches seem to be fairly predictable. Exploring what factors our models found to be most important is also vital to gaining a better understanding of what good team compositions look like. Another thing we wanted to try but could not get to in time was different sets of data, for example ensuring that some number of every unique team composition was included, or that skill brackets and heroes saw equal representation.

An end goal of ours is to be able to simulate full drafts, in order to provide insight on what heroes to pick and when. For example a team with the 9th pick would be able to see what heroes provide the largest boost to their win probabilities, or perhaps would see early in the draft who they should ban. These pieces of information, if used in practice, could help guide teams to better strategies and overall performace in competitive matches.
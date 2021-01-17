# Predicting migration using satellite imagery

## Introduction

In India, 
1. The data driven governance regime depends to a great extent on administrative data collected by government departments.
2. This data is used to monitor the efficacy of schemes and policies to shape routine everyday administration.
3. Research on migration India has suffered due to lack of consistent and robust data. It belies regional and spatial disparity. Migration is motivated by the need to secure a sustainable  and  economically stable livelihood and happens from areas of poor development towards highly urbanized areas. Hence, it influences development.

## Aim and Objectives

1. Use geospatial and census data analysis to enable novel data intensive approach to analyse and measure human development.
2. Predict and track migration patterns and their relationship with other socioeconomic variables
3. Study how technology could monitor economic development and analyse as well as predict trends relating to the growth of a country.

## Proposed Methods

### Dataset

1. Census Dataset(Ground Truth) (Check out MigrationGroundTruth.xlsx in the Dataset Folder)
2. Processed Satellite Images- 635 districts (Check out Preprocessing of Landsat7 Images Folder)

### Step 1: Data Preprocessing from census tables
### Step 2: Image Preprocessing from Satellite Data an Feature Extraction (Find features in the dataset folder)
### Step 3: Developing Machine Learning Framework (_Prediction.ipynb_)

## Results 

1. To offer an alternative to the task of the census, we try to use satellite imagery as its proxy. We compared several machine learning models and observed the Extreme Gradient Boosting or   XGBoost classifier , performed the best and gave us accuracies and f1-scores, ranging from    63%-85%.

## Conlusion

We have established that satellite imagery could indeed be used to predict socioeconomic growth and migration patterns of a country
 



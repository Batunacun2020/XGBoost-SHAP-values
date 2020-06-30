# XGBoost-SHAP-values： Prediction of grassland degradation
## Table of contents
### Background
This project aims to using argificial intelligence methods to simulating and predicting land use change.
### Install
#Please use Ananconda as basis environment for Python3.X
#Anaconda is a free and open-source distribution of the Python and R 
#programming languages for scientific computing (data science, machine 
#learning applications)
#for installation look at: https://www.anaconda.com/products/individual
#and install the open source version for your operation system
#========================================================================
#Please install the following packages using a conda virtual enviroment 
#========================================================================
#conda create a new virtual environment
conda create --name XGB
conda activate XGB
#install packages
conda install -c conda-forege xgboost
conda install -c conda-forge shap 
conda install -c conda-forge imbalanced-learn
conda install -c conda-forge ipython
conda install -c conda-forge matplotlib
conda install -c conda-forge pandas
### Data and output introduction
The present example of machine learning modelling was created on the basis of spatial data from Inner Mongolia (China). Firstly, a model (lr) was developed on the basis of logistic regression.  This model achieves only a low accuracy and serves as a benchmark. The second model xgb was created using XGBoost. It achieved a very high accuracy both in training and, more importantly, in test data excluded from training. 

The data has an unbalanced distribution for class 0 (no degradation) and class 1 (degradation) of about 10:1 To change this, artificial values were added using a "RandomOverSampler" from the Python package "imblearn".

Furthermore, the SHAP library was used for the statistical analysis of xgb in the methodology presented here. The SHAP allows a detailed analysis of single decisions, the dependencies of two inputs up to the overall analysis of the feature_importance (shap.summary_plot). This was used to determine the four most important influencing variables of the model.

This example software is part of my research work in Germany at Zalf Müncheberg and is aimed at stimulating the study of the methodology of machine learning.

##Data description
disdens: distance to dense grass
dismode: distance to moderately dense grass
dissparse: distance to sparse grass
sheep: sheep density
disunused: distance to unused land
prec: precipitation
disforest: distance to forest
gdp: GDP density
urban: distance to urban
dem: DEM
slope: slope
mine: distance to mine
temp: temperature
discrop: distance to cropland
desertPolicy: policy setting, dummy variable
road: distance to road
water: distance to  water
pop: population density
rural: distance to rural area
aspect: aspect


##Model output:

========================= Oversampling ============================
items before over sampling: [(0.0, 18190), (1.0, 1810)]
items after over sampling: [(0.0, 18190), (1.0, 18190)]
====================== Logistic Regression ========================
Testing score     : 0.6880726303514909
Training score    : 0.6938951341593501
Testing score1    : 0.6880726303514909
Testing precision : 0.6802241793434748
Testing recall    : 0.7084723148765844
kappa             : 0.3761745858219654
F1 score          : 0.694061
ROC AUC           : 0.749781
area under PR     : 0.761540
============================= XGBoost =============================
Testing score     : 0.9789272030651341
Training score    : 0.9809222942479692
Testing score1    : 0.9789272030651341
Testing precision : 0.9665312753858651
Testing recall    : 0.9921614409606404
kappa             : 0.9578556504852656
F1 score          : 0.979179
ROC AUC           : 0.997841
area under PR     : 0.997592

============================== SHAP ===============================

![shap](shape2.png)


##Happy hacking
### Maintainer
@Batunacun2020
### Contributing
@Ralf Wieland @Batunacun

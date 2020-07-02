# XGBoost-SHAP-values： Prediction of grassland degradation

## Background
This project aims to simulating and predicting grassland degradation by using Machine Learning method-XGBoost.
This project has been published on Geoscientific Model Development, please check the link to download it: https://gmd.copernicus.org/preprints/gmd-2020-59/#discussion
## Install
Please check the install text. 
## Data and output introduction
### Model selection
The present example of machine learning modelling was created on the basis of spatial data from Inner Mongolia (China). Firstly, a model (Logistic regression) was developed on the basis of logistic regression.  This model achieves only a low accuracy and serves as a benchmark. The second non-linear (black box model) model was created using XGBoost. It achieved a very high accuracy both in training and simulating process, more importantly, in test data excluded from training. 
### Imbalance issue
The data has an unbalanced distribution for class 0 (no degradation) and class 1 (degradation) of about 10:1 To change this, artificial values were added using a "RandomOverSampler" from the Python package "imblearn".
Over-sampling method refers Artificial points are added to the minority class of an imbalanced sampling set, making it equal to the majority class and resulting in equal sized samples.
### Open black box model-SHAP values
Furthermore, the SHAP library was used for the statistical analysis of xgb in the methodology presented here. The SHAP allows a detailed analysis of single decisions, the dependencies of two inputs up to the overall analysis of the feature_importance (shap.summary_plot). This was used to determine the four most important influencing variables of the model.
SHAP values as a statistical method use used in this project to sort the driver’s effects, and break down the prediction into individual feature impacts.

This example software is part of my research work in Germany at Zalf Müncheberg and is aimed at stimulating the study of the methodology of machine learning.

## Data description
#### Data collection and processing
In line with previous studies, A total of 20 (include one policy proxy variable) drivers were used in this project to simulating grassland degradation in Xilingol.
#### Drvier description
Driver name | Description
------------ | -------------
disdens | distance to dense grass  
dismode |distance to moderately dense grass  
dissparse| distance to sparse grass  
sheep|sheep density  
disunused|distance to unused land 
prec|precipitation  
disforest|distance to forest
gdp|GDP density  
urban|distance to urban  
dem|DEM  
slope| slope  
mine|distance to mining area
temp|temperature  
discrop|distance to cropland  
desertPolicy|policy setting, dummy variable  
road|distance to road 
water|distance to  water
pop|population density 
rural|distance to rural area 
aspect|aspect  
## Smpling stratigies and Model validation:
### Smpling stratigies
========================= Oversampling ============================  
Sampling stratiges | sampling size
------------ | -------------
items before over sampling|[(0.0, 18190), (1.0, 1810)]  
items after over sampling|[(0.0, 18190), (1.0, 18190)]  

### Model validation
#### overall classification accuracy
#### precision
#### recall
#### kappa
#### area under PR
====================== Logistic Regression ========================  
validation indicators| results
------------ | -------------
Testing score|0.689
Training score|0.69
Testing score1|0.69
Testing precision|0.68 
Testing recall|0.71   
kappa | 0.38
area under PR|0.76   
  
============================= XGBoost =============================  
validation indicators| results
------------ | -------------
Testing score|0.98
Training score |0.98
Testing score1 |0.97
Testing precision |0.99
Testing recall|0.96
kappa|0.96
area under PR|1.00
============================== SHAP ===============================  
![shap](https://github.com/Batunacun2020/XGBoost-SHAP-values/blob/master/shap2.png)


##Happy hacking
## Maintainer
@Batunacun2020
## Contributing
@Ralf Wieland @Batunacun

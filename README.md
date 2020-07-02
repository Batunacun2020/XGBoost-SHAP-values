# XGBoost-SHAP-values： Prediction of grassland degradation

## Background
This project aims to simulating and predicting grassland degradation by using Machine Learning method-XGBoost.
This project has been published on Geoscientific Model Development, please check the link to download it: https://gmd.copernicus.org/preprints/gmd-2020-59/#discussion
## Install
Please check the install text. 
## Data and output introduction
The present example of machine learning modelling was created on the basis of spatial data from Inner Mongolia (China). Firstly, a model (lr) was developed on the basis of logistic regression.  This model achieves only a low accuracy and serves as a benchmark. The second model xgb was created using XGBoost. It achieved a very high accuracy both in training and, more importantly, in test data excluded from training. 

The data has an unbalanced distribution for class 0 (no degradation) and class 1 (degradation) of about 10:1 To change this, artificial values were added using a "RandomOverSampler" from the Python package "imblearn".
Over-sampling method refers Artificial points are added to the minority class of an imbalanced sampling set, making it equal to the majority class and resulting in equal sized samples.

Furthermore, the SHAP library was used for the statistical analysis of xgb in the methodology presented here. The SHAP allows a detailed analysis of single decisions, the dependencies of two inputs up to the overall analysis of the feature_importance (shap.summary_plot). This was used to determine the four most important influencing variables of the model.
SHAP values as a statistical method use used in this project to sort the driver’s effects, and break down the prediction into individual feature impacts.

This example software is part of my research work in Germany at Zalf Müncheberg and is aimed at stimulating the study of the methodology of machine learning.

##Data description
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
------------ | -------------

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
## Maintainer
@Batunacun2020
## Contributing
@Ralf Wieland @Batunacun

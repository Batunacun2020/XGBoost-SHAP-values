# XGBoost-SHAP-values： Prediction of grassland degradation

## Background
This project aims to simulating and predicting grassland degradation by using Machine Learning method-XGBoost.
SHAP values was used to "crack the black model", XGBoost. SHAP values were useful for analysing the complex relationship between the different drivers of grassland degradation. 
### Objectives
From 2000 to 2015, about 10.2% of the total area has experienced grassland degradation. We are primarily interested in learning whether ML models can achieve a better predictive quality than linear methods, in addition to improving our understanding of how grassland degrades in Xilingol. The objects in this project as following:  
(1) Can machine learning models achieve a better predictive quality than linear methods?  
(2) How can we open the nonlinear relationships of the black box model? 
### Related publication
This project has been published on "Geoscientific Model Development", please check the link to download it: https://gmd.copernicus.org/preprints/gmd-2020-59/#discussion
## Install
Please check the install.txt. 
## Data collection
In line with previous studies, A total of 20 (include one policy proxy variable) drivers were used in this project to simulating grassland degradation in Xilingol.
The data used in this project please check "dataImbalance.csv"
### Drvier description
For example: disdens is the abbreviation of distance to dense grassland, it is euclidean distance that calculated by ArcGIS.
Disdens is a proxy drivers, that could stand for the existing dense grassland effects and the comprehensitive environment of the dense grassland.
Driver name | Description|Driver name | Description          
------------ | --------------|----------- | -------------
disdens | distance to dense grass|                slope| slope  
dismode |distance to moderately dense grass|      mine|distance to mining area
dissparse| distance to sparse grass|              temp|temperature
sheep|sheep density |                          discrop|distance to cropland 
disunused|distance to unused land|                desertPolicy|policy setting, dummy variable 
prec|precipitation|                               road|distance to road 
disforest|distance to forest|                     water|distance to  water
gdp|GDP density|                                 pop|population density 
urban|distance to urban|                          rural|distance to rural area 
dem|DEM|                                         aspect|aspect  

## Model building and selection
The present example of machine learning modelling was created on the basis of spatial data from Inner Mongolia (China). we use logistic regression as a benchmark model to compare linear and non-linear methods in the simulation of grassland degradation. This model achieves only a low accuracy. The second non-linear (black box model) model was created using XGBoost. It achieved a very high accuracy with four different samplling strategies(see follow section), in both training and simulating process. In this project, due to the limitation of the dataset, we post the model training process. The high accuracy model produced by training process could be used in simulation process.
<p align="center">
  <img src="https://github.com/Batunacun2020/XGBoost-SHAP-values/blob/master/Model%20structure.png" height=70% width=70%>
</p>
## Imbalance issue
The data has an unbalanced distribution for class 0 (no degradation) and class 1 (degradation) of about 10:1 To change this, artificial values were added using a "RandomOverSampler" from the Python package "imblearn".
Over-sampling method refers Artificial points are added to the minority class of an imbalanced sampling set, making it equal to the majority class and resulting in equal sized samples.
### Smplling stratigies
Data are often distributed unevenly among different classes. Such imbalanced class distribution generally induces a bias. Canonical ML algorithms assume that data is roughly balanced in different classes. In real situations, however, the data is usually skewed, and smaller classes often carry more important information and knowledge than larger ones. It is therefore important to develop learning from imbalanced data to build real-world models. To ensure a highly accurate GD model, we introduced four different sampling methods in this study(following figure).
<p align="center">
  <img src="https://github.com/Batunacun2020/XGBoost-SHAP-values/blob/master/Four%20sampling%20strategies%20used%20in%20this%20project.png" height=70% width=70%>
</p>

========================= Oversampling ============================  
Sampling stratiges | sampling size
------------ | -------------
items before over sampling|[(0.0, 18190), (1.0, 1810)]  
items after over sampling|[(0.0, 18190), (1.0, 18190)]  
## Model validation
### Overall classification accuracy (OCA)
OCA is the correct prediction of NGD and other pixels in the whole region. This indicator was used to evaluate the accuracy of the model.
### precision 
Precision is the proportion of correctly predicted positive examples (refers to NGD in this study) in all predicted positive examples.
### Recall 
Recall is the proportion of correctly predicted positive examples in all observed positive examples (the observed NGD)
### Kappa
Kappa is a popular indicator used to measure the proportion of agreement between observed and simulated data, especially to measure the degree of spatial matching. 
### The precision-recall curve (PR curve)
PR curve provides more information about the model’s performance than, for instance, the Receiver Operator Characteristic curve (ROC curve), when applied to skewed data. The PR curve shows the trade-off of precision and recall, and provides a model-wide evaluation.
### area under PR: The area under the PR curve (AUC-PR) 
AUC-PR is likewise effective in the classification of model comparisons. 
====================== LG and XGBoost valdation ========================  
validation indicators|Logistic Regression validation|XGBoost validation
------------ | -------------| -------------
Testing score|0.69|0.98
Training score|0.69|0.98
Testing score1|0.69|0.97
Testing precision|0.68|0.99
Testing recall|0.71|0.96
kappa | 0.38|0.96
area under PR|0.76| 1.00
 
## Open black box model-SHAP values
Furthermore, the SHAP library was used for the statistical analysis of xgb in the methodology presented here. The SHAP allows a detailed analysis of single decisions, the dependencies of two inputs up to the overall analysis of the feature_importance (shap.summary_plot). This was used to determine the four most important influencing variables of the model.
SHAP values as a statistical method use used in this project to sort the driver’s effects, and break down the prediction into individual feature impacts.

This example software is part of my research work in Germany at Zalf Müncheberg and is aimed at stimulating the study of the methodology of machine learning.
<p align="center">
  <img src="https://github.com/Batunacun2020/XGBoost-SHAP-values/blob/master/Decomposed%20SHAP%20values.png"  height=80% width=80% title="SHAP values">
</p>

## Model results

### Drivers selection
The SHAP values plot combines feature importance (drivers are ordered along the y-axis) and driver effects (SHAP values on the x-axis), which describe the probability of NGD having occurred. Positive SHAP values refer to a higher probability of NGD. The gradient colour represents the feature value from high (red) to low (blue). As the figure shows, disdense was the primary driver for NGD in the study region. The relationship between disdense and NGD is non-linear, which can be seen from the SHAP values being both positive and negative. 

### Drivers interpretation
============================== SHAP ===============================  
<p align="center">
  <img src="https://github.com/Batunacun2020/XGBoost-SHAP-values/blob/master/SHAPvaluesGitHub.png" height=60% width=60% title="SHAP values">
</p>


## Maintainer
@Batunacun2020
## Contributing
@Ralf Wieland @Batunacun2020

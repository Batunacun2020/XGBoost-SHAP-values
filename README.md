# XGBoost-SHAP-values：Prediction of grassland degradation

## Background
This project aims at simulating and predicting grassland degradation by using Machine Learning (ML) method, XGBoost.
SHAP values was used to "crack the black model", XGBoost. SHAP values were useful for analysing the complex relationship between different drivers of grassland degradation. 
### Objectives
Xilingol, located in Inner Mongolia, China, is typical region for research on serious grassland degradation and its drivers. 
From 2000 to 2015, about 10.2% of the total area in Xilingol has experienced grassland degradation (newly added grassland degradation, NGD). We are primarily interested in evaluating whether ML models can achieve a better predictive quality than generalized linear methods, in addition to improving our understanding of how grassland degradation occurs in Xilingol. Therefore, the goal of this project is to answer the following research questions:    
(1) Can machine learning models achieve a better predictive quality than linear methods?    
(2) How can we open the nonlinear relationships of the black box model?   
Based on these questions, a set of twenty drivers were analysed using XGBoost, involving four alternative sampling strategies, and SHAP to interpret the results of the purely data-driven approach. 
### Related publication
This project has been published on the journal of "Geoscientific Model Development", please check the link to download it: https://gmd.copernicus.org/preprints/gmd-2020-59/#discuSHAP.
## Install
Please check the install.txt. 
## Data collection
In line with previous studies, a total of 20  drivers (including one policy proxy variable) were used in this project to simulate grassland degradation in Xilingol.
Please check the data file (data.csv) for the data used in this project.
### Drvier description
For example: disdens is the Euclidean distance to dense grassland, calculated by ArcGIS.  
Disdens is a proxy driver, which represents the effects of dense grassland and its comprehensive environment.  
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

## Model selection and validation
### Model selection 
In a bid to create a robust model to simulating grassland degradation, two different models were used, XGBoost (non-linear model) and Logistic regression (generalized linear model). Logistic regression was used as a benchmark in this study. Results indicated that XGBoost outperformed logistic regression models in both training and simulation processes. Due to dataset limitations, we post the model training process only. The high accuracy model produced by training process could be used in simulation process. We organized the grassland degradation issue as a binary classification task by using ML model. The model building process was presented in the following figure.

<p align="center">
  <img src="https://github.com/Batunacun2020/XGBoost-SHAP-values/blob/master/image/Model%20structure.png" height=450% width=45% alt="Model building process">
</p>

### Model validation
In this project, a robust model was selected using overall classification accuracy, precision, recall and the kappa index. Accuracy, precision and recall were calculated based on a confusion matrix (CM) (He and Garcia, 2009).  
The following table indicates that XGBoost outperformed logistic regression models.  
**OCA**: is the correct prediction of NGD and other pixels in the whole region. This indicator was used to evaluate the accuracy of the model.    
**Precision**: refers to the proportion of correctly predicted positive examples in all predicted positive examples.      
**Recall**: refers to the proportion of correctly predicted positive examples in all observed positive examples (the observed NGD).      
**Kappa**: refers to a popular indicator used to measure the proportion of agreement between observed and simulated data, especially to measure the degree of spatial matching.      
**The precision-recall curve (PR curve)**: PR curves provide more information about  model’s performance than other methods, such as Receiver Operating Characteristic curve (ROC curve), when applied to skewed data. The PR curve shows the trade-off of precision and recall, and provides a model-wide evaluation.      
**area under PR, The area under the PR curve (AUC-PR)**: AUC-PR is likewise effective in the classification of model comparisons.     
**F1 score**: The F1 score can be interpreted as a weighted average of the precision and recall, where an F1 score reaches its best value at 1 and worst score at 0.    
**ROC AUC**: Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores. ROC curve is a graphical plot that illustrates the diagnostic ability of a binary classifier system based on a discrimination threshold (https://scikit-learn.org/0.21/modules/generated/sklearn.metrics.roc_auc_score.html).    
**F1 score and ROC AUC were not used in our publication, but we listed these methods here as it can be useful for other projects.**

====================== LG and XGBoost valdation ========================  
validation indicators|Logistic Regression validation|XGBoost validation
------------ | -------------| -------------
Testing score|0.69|0.98
Training score|0.69|0.98
Testing score1|0.69|0.97
Testing precision|0.68|0.99
Testing recall|0.71|0.96
F1 score|0.69| 0.98
ROC AUC|0.75| 1.00
kappa | 0.38|0.96
area under PR|0.76| 1.00
## Imbalance issue
About 10.2% of the total area was degraded between 2000 and 2015. As a binary classification issue, the data has an unbalanced distribution for class 0 (non degradation, 90% of the total area) and class 1 (degradation, 10% of total area). In real situations, the data is usually skewed, and smaller classes often carry more important information and knowledge than larger ones. It is therefore important to develop learning from imbalanced data to build real-world models. 
For machine learning methodology, the unevenly distributed data led to overfitting or loss of important information. In a bid to avoid bias, different sampling strategies should be used. The sampling method generally includes balanced and imbalanced sampling strategies. In this study, we tested various balanced sampling strategies to identify the most suitable one. The following list briefly describes each sampling method.
We used four different sampling methods in this study.    
**Over-sampling**: Artificial points are added to the minority class of an imbalanced sampling set, making it equal to the majority class and resulting in equal sample sizes.      
**Under-sampling**: Points are removed from a majority class of an imbalanced sampling set, making it equal to the minority class and resulting in equal sample sizes.    
**Imbalanced-sampling**: Random data sampling, but with the same share of the sampled class, resulting in unequal sample sizes.        
**Balanced-sampling**: Random data sampling, resulting in equal sample sizes.    
Over-sampling method performed slightly better than the other three sampling methods.   
 
<p align="center">
  <img src="https://github.com/Batunacun2020/XGBoost-SHAP-values/blob/master/image/Four%20sampling%20strategies%20used%20in%20this%20project.png" height=50% width=50% alt="Smpling strategites">
</p>

## Open black box model-SHAP values
SHAP (SHapley Additive exPlanations) is a novel approach to improve our understanding of the complexity of predictive model results and to explore relationships between individual variables for the predicted case (Lundberg and Lee, 2017).
The general idea of introducing SHAP values as a further tool to analyse XGBoost ranking is to provide a method to evaluate the ranking with respect to causal relationships.  
The following figure shows the decomposed SHAP values for the individual prediction of an example pixel.
Disdens was the dominant driver for grassland degradation at this pixel.


This example software is part of my research work in Germany at Zalf Müncheberg and is aimed at stimulating the study of the methodology of machine learning.
<p align="center">
  <img src="https://github.com/Batunacun2020/XGBoost-SHAP-values/blob/master/image/Decomposed%20SHAP%20values.png"  height=80% width=80% title="SHAP values" alt="Decomposed SHAP values of each point">
</p>

## Model results
### Drivers selection
The SHAP values plot combines feature importance (drivers are ordered along the y-axis) and driver effects (SHAP values on the x-axis), which describe the probability of NGD having occurred. Positive SHAP values refer to a higher probability of NGD. The gradient color represents the feature value from high (red) to low (blue). As the figure shows, disdense was the primary driver for NGD in the study region. The relationship between disdense and NGD is non-linear, which can be seen from the SHAP values being both positive and negative. 
### Drivers interpretation
The following figure shows that driver effects include both linear-dominated relationships, such as sheep, GDP and others, and non-linear-dominated relations, such as disdense, dismode and others. 
In addition, the figure shows that the most important drivers for NGD are the changes of distance to dense, moderately dense and sparse grassland, followed by sheep density and the distance to unused land.

<p align="center">
  <img src="https://github.com/Batunacun2020/XGBoost-SHAP-values/blob/master/image/SHAPvalues.png" height=60% width=60% title="SHAP values" alt="SHAP values">
</p>


## Maintainer
@Batunacun2020
## Contributing
@Ralf Wieland (https://github.com/Ralf3)   @Batunacun2020  
This example software is part of my research work in Germany at Zalf Müncheberg and is aimed at stimulating the study of the methodology of machine learning.
## Reference
1,Batunacun, Wieland R, Lakes T, Nendel C. 2020. Using SHAP to interpret XGBoost predictions of grassland degradation in Xilingol, China. Geoscientific Model Development Discussions 1–28. DOI: https://doi.org/10.5194/gmd-2020-59  
2,He H, Garcia EA. 2009. Learning from Imbalanced Data. IEEE Transactions on Knowledge and Data Engineering 21: 1263–1284. DOI: 10.1109/TKDE.2008.239  
3,Lundberg S. 2019. A unified approach to explain the output of any machine learning model.: slundberg/shap. Jupyter Notebook. 


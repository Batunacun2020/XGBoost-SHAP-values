"""
Machine learning example for landuse change modeling in Inner Mongolia

Steps:
1.) Read the data using pandas 
2.) change the imbalance data to a balanced data by RandomOverSampler
3.) Use a logistic regression as benchmark
4.) Use Xgboost 
5.) Make a model evaluation
6.) Open the blackbox of the XGBoost using the SHAP library

Batunacun 24.06.2020 GPLv3
"""

import pandas as pd
import numpy as np
import pylab as plt
from xgboost import plot_importance
from xgboost import plot_tree
from xgboost import XGBClassifier
import shap
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, precision_score
from sklearn.model_selection import train_test_split 
from random import sample
from collections import Counter
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.metrics import precision_recall_curve
from imblearn.over_sampling import RandomOverSampler

#=============CHANGE LD data===================
# adapt this path according your file structure
path='../data/'
df=pd.read_csv(path+'data.csv', sep=';')

# original order, do not move
inputs=['water','desertPolicy','gdp','road','slope','dem','urban','aspect',
        'sheep','mine','disforest','temp','rural','discrop','pop','prec',
        'disunused','dismode','disdens','dissparse']
         
# prepare data from sample data for machine learning
def gen_X(inp):
    """ 
    uses inp to select the data from df
    """
    global df  # df sample data
    X=np.zeros((df.shape[0],len(inp))) # store the training data from sample 
    k=0 # count the names
    for name in inp: 
        X[:,k]=df[name].values #sampling dataset
        k+=1
    return X # return the sample point drivers

#generate Y data
def gen_Y(sel):
    global df # df, sample data
    Y=np.zeros((df.shape[0]))
    Y[:]=df[sel].values # df include all sample data
    return Y

# evaluate the trained models
def score(model,Xtrain,ytrain,Xtest,ytest):
    """ uses the model to calculate a set of scores """
    print('Testing score     :',model.score(Xtest,Ytest))
    # accuracy_score
    print('Training score    :',model.score(Xtrain,Ytrain))
    Ym=model.predict(Xtest)
    print('Testing score1    :',accuracy_score(Ytest,Ym))
    print('Testing precision :', precision_score(Ytest,Ym))
    print('Testing recall    :', recall_score(Ytest,Ym))
    print('kappa             :',cohen_kappa_score(Ytest,Ym))
    print('F1 score          : %f' % f1_score(Ytest,Ym))
    # ROC AUC
    Yp=model.predict_proba(Xtest)
    probs = Yp[:, 1]# keep probabilities for the positive outcome only
    print('ROC AUC           : %f' % roc_auc_score(Ytest, probs))
    #print auc of precision recall curve
    precision, recall, thresholds = precision_recall_curve(Ytest, probs)
    # calculate precision-recall AUC
    print('area under PR     : %f' % auc(recall, precision))
    
#==========CHANGE different period=======
name='gdnew'
#name='ldlrChange' # alternattive training fit
x=gen_X(inputs)
y=gen_Y(name)# 'ldlr7500' is one filed in df, 

print('========================= Oversampling ============================')
# over sample quickly, increase value 1
print('items before over sampling:',sorted(Counter(y).items()))
ros = RandomOverSampler(random_state=0)
X, Y = ros.fit_resample(x, y)
print('items after over sampling:',sorted(Counter(Y).items()))

# split train and test data
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.33)
# train the logistic regression
lg = LogisticRegression(C=0.1,penalty='l2',max_iter=5000,
                           solver="lbfgs",multi_class='multinomial', 
                           random_state=0,)

lg.fit(Xtrain,Ytrain)

# score the model
print('====================== Logistic Regression ========================')
score(lg,Xtrain,Ytrain,Xtest,Ytest)

# the parameter after tunning 
basicparameter={'base_score':0.5,
                'booster':'gbtree',
                'objective':'binary:logistic',
                'scale_pos_weight':1,
                'max_delta_step':5,
                'n_jobs':1,
                'random_state':0, 
                'max_depth':5,
                'min_child_weight':3,
                'n_estimators':300,                
                'subsample':1.0,#0.9,
                'colsample_bytree':0.5,
                'reg_lambda':10,
                'reg_alpha':0.1,
                'learning_rate':0.01,
                'gamma':0.1}                

xgb=XGBClassifier(**basicparameter)
# xgb=XGBClassifier() # apply the default parameters
xgb.fit(Xtrain,Ytrain)

#  score the model
print('============================= XGBoost =============================')
score(xgb,Xtrain,Ytrain,Xtest,Ytest)

print('============================== SHAP ===============================')
explainer = shap.TreeExplainer(xgb)   # define the explainer
shap_values = explainer.shap_values(X)  # use all data for analysis
def gen_data(inputs,X):
    """ creates a data Frame with inputs and X for statistics with shap """
    df1=pd.DataFrame()
    for i,name in enumerate(inputs):
        df1[name]=X[:,i]
    return df1
df1=gen_data(inputs,X)

shap.summary_plot(shap_values, df1)
# shap.summary_plot(shap_values, df1, plot_type="bar")

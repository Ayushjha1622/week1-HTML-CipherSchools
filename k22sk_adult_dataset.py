# -*- coding: utf-8 -*-
"""K22SK_adult_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x0XxWPWv2ZHD1emQ8FpHoMO0vvBeYGNU
"""

import pandas as pd

dataset=pd.read_csv('/content/adult.csv', header=None, na_values=' ?')

dataset.shape

dataset.head()

dataset.columns=['age', 'workclass','wgt', 'edu','edu_num', 'marital_status',
                 'occ', 'relation','race', 'sex', 'gain','loss', 'hpw', 'country', 'income']

dataset.head()

dataset.isnull().sum()

from sklearn.impute import SimpleImputer
si=SimpleImputer(strategy='most_frequent')
dataset1=si.fit_transform(dataset)
print(pd.DataFrame(dataset1).isnull().sum())

dataset1=pd.DataFrame(dataset1)
dataset1.columns=['age', 'workclass','wgt', 'edu','edu_num', 'marital_status',
                 'occ', 'relation','race', 'sex', 'gain','loss', 'hpw', 'country', 'income']
print(dataset1.head())

cols=['workclass','edu','marital_status','occ', 'relation', 'race', 'sex','country','income']
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in cols:
  dataset1[i]=le.fit_transform(dataset1[i])
print(dataset1.head())

target=dataset1['income']
input=dataset1.drop(columns=['income'])
input.shape

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(input, target, test_size=0.25)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
xtrain_sc=sc.fit_transform(x_train)
xtest_sc=sc.transform(x_test)
y_train.unique()

(y_train==0).count()
y_train.shape
(y_train==0).sum()
(y_train==1).sum()

from sklearn.linear_model import Perceptron
P=Perceptron()
P.fit(x_train,y_train)
train_pred=P.predict(x_train)
test_pred=P.predict(x_test)

from sklearn.metrics import accuracy_score
print("Training Accuracy: ",accuracy_score(train_pred,y_train))
print("Testing Accuracy: ", accuracy_score(test_pred, y_test))


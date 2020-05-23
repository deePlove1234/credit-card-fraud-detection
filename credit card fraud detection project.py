#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import numpy
import pandas
import matplotlib
import seaborn
import scipy
import sklearn
print('python:{}'.format(sys.version))
print('Numpy:{}'.format(numpy.__version__))
print('Pandas:{}'.format(pandas.__version__))
print('Matplotlib:{}'.format(matplotlib.__version__))
print('seaborn:{}'.format(seaborn.__version__))
print('Scipy:{}'.format(scipy.__version__))
print('Sklearn:{}'.format(sklearn.__version__))


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as  sns


# In[3]:


data= pd.read_csv('C:\\Users\\Deepanshi\\Downloads\\creditcard.csv')
data


# In[4]:


print(data.columns)


# In[5]:


print(data.shape)


# In[6]:


print(data.describe)


# In[7]:


data.mean


# In[8]:


data=data.sample(frac=1,random_state=2)
print(data.shape)


# In[9]:


data.hist(figsize=(20,20))
plt.show()


# In[10]:


Fraud=data[data['Class']==1]
Valid=data[data['Class']==0]
outlier_fraction=len(Fraud)/float(len(Valid))
print('Fraud Cases:{}'.format(len(Fraud)))
print('Valid Cases:{}'.format(len(Valid)))


# In[11]:


cormat=data.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(cormat,vmax= .8,square=True)
plt.show() ##corelation matrix.....light + ,dark- corelations


# In[12]:


columns=data.columns.tolist()
columns=[c for c in columns if c not in ["Class"]]
target="Class"
X=data[columns]
Y=data[target]
print(X.shape)
print(Y.shape)


# In[13]:


from sklearn.metrics import classification_report,accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

state=1

classifiers={
    "Isolation Forest":IsolationForest(max_samples=len(X),
                      contamination = outlier_fraction, random_state=state),
     "Local Outlier Factor":LocalOutlierFactor(n_neighbors=20,
    contamination = outlier_fraction)
    
}


# In[14]:


n_outliers=len(Fraud)
for i,(clf_name,clf) in  enumerate(classifiers.items()):
    
        if clf_name =="Local Outlier Factor":
            y_pred = clf.fit_predict(X)
            scores_pred=clf.negative_outlier_factor_
        else:
            clf.fit(X)
            scores_pred=clf.decision_function(X)
            y_pred=clf.predict(X)
            
            y_pred[y_pred==1]=0
            y_pred[y_pred==-1]=1
            n_errors=(y_pred != Y).sum()
            
            print('{}: {}'.format(clf_name,n_errors))
            print(accuracy_score(Y,y_pred))
            print(classification_report(Y,y_pred))


# In[ ]:





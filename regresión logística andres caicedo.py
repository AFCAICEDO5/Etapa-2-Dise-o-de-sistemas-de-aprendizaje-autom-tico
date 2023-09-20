#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sb
get_ipython().run_line_magic('matplotlib', 'inline')


# In[37]:


data = pd.read_csv(filepath_or_buffer = "/Users/felipe.caicedo/Documents/archive/diabetes2.csv")
data.head(10)


# In[41]:


data[['BMI','Outcome']].head()


# In[43]:


#grafica de puntos
data[['BMI','Outcome']].plot.scatter(x='BMI',y='Outcome')


# In[48]:


# pintar funcion logistica
#pruebas de parametros
w = 0.09
b = -3.6
#puntos de la recta
x = np.linspace(0,data['BMI'].max(),100)
y = 1/(1+np.exp(-(w*x+b)))


# In[49]:


# grafica de la recta
data.plot.scatter(x='BMI',y='Outcome')
plt.plot(x,y, color='black')
plt.ylim(0,data['Outcome'].max()*1.1)
plt.scatter(x,y, color='#A9E2F3')
# plt.grid()
plt.xlabel("indice de masa corporal")
plt.ylabel("diabetis 1:Posotivo 0:Negativo")
plt.show()


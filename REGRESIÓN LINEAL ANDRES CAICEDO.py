#!/usr/bin/env python
# coding: utf-8

# In[139]:


import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
import sklearn
import matplotlib.pylab  as  ptr 
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from tabulate import tabulate
import matplotlib.pyplot  as  plt 



# In[140]:


Rlineal = pd.read_csv(filepath_or_buffer = "/Users/felipe.caicedo/Documents/archive/data.csv")


# In[73]:


Rlineal.head(5)


# In[94]:


print(Rlineal.metro)


# In[96]:


Rlineal.columns


# In[107]:


Rlineal[['metro','precio']].head()


# In[145]:


Rlineal.plot.scatter(x='metro',y='precio')


# In[143]:


fig = plt.figure(figsize = (14,14))
plt.scatter(Rlineal['metro'],Rlineal['precio'])
plt.plot(Rlineal['metro'],Rlineal['precio'],)
plt.xlabel('metro')
plt.ylabel('precio')
plt.grid()


#!/usr/bin/env python
# coding: utf-8

# # Introduction to Pandas
# **Pandas** is an open-source Python library used for data manipulation, cleaning, analysis, and visualization.
# It provides tools to work with structured data like tables from CSV, Excel, SQL, etc.
# 
# The name *'Pandas'* comes from **'Panel Data'** — a term used in econometrics.

# ##  Why Use Pandas?
# - Load data from files and databases
# - Clean, filter, sort, and transform data
# - Handle missing data easily
# - Perform grouping and aggregation
# - Analyze time series
# - Merge or join datasets

# ##  Core Data Structures in Pandas

# ### 1. `Series` - 1D labeled array

# In[5]:


import pandas as pd
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)


# ### 2. `DataFrame` - 2D table made of Series

# In[8]:


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
df = pd.DataFrame(data)
print(df)


# ##  Common Operations in Pandas

# In[10]:


#  View data
df.head()
df.tail()
df.shape
df.info()
df.describe()


# In[12]:


# Access data
df['Name']
df.loc[0]
df.iloc[0]


# In[13]:


# Filter data
df[df['Age'] > 25]


# In[15]:


# Handle missing data
df.dropna()
df.fillna(0)


# In[16]:


# Group and aggregate
df.groupby('City')['Age'].mean()


# In[32]:


# Merge DataFrames
# pd.merge(df1, df2, on='ID')


# ##  Pandas with Visualization

# In[21]:


import matplotlib.pyplot as plt
df['Age'].plot(kind='hist')
plt.show()


# ##  When to Use Pandas?
# - You have structured/tabular data
# - You need to clean or explore datasets
# - You want to do quick data analysis
# - You're preparing data for machine learning

# ##  Summary Table
# | Feature              | Series                  | DataFrame                |
# |----------------------|--------------------------|--------------------------|
# | Dimensions           | 1D                       | 2D                       |
# | Structure            | Labeled array            | Table of labeled columns |
# | Indexing             | One axis (rows)          | Two axes (rows + columns)|
# | Real-world analogy   | Single column in Excel   | Full Excel sheet         |

# In[ ]:





# In[ ]:





# In[ ]:





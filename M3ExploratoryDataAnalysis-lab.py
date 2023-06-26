#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2023-01-01">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Exploratory Data Analysis Lab**
# 

# Estimated time needed: **30** minutes
# 

# In this module you get to work with the cleaned dataset from the previous module.
# 
# In this assignment you will perform the task of exploratory data analysis.
# You will find out the distribution of data, presence of outliers and also determine the correlation between different columns in the dataset.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# -   Identify the distribution of data in the dataset.
# 
# -   Identify outliers in the dataset.
# 
# -   Remove outliers from the dataset.
# 
# -   Identify correlation between features in the dataset.
# 

# * * *
# 

# ## Hands on Lab
# 

# Import the pandas module.
# 

# In[1]:


import pandas as pd


# Load the dataset into a dataframe.
# 

# In[2]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")


# ## Distribution
# 

# ### Determine how the data is distributed
# 

# The column `ConvertedComp` contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01.
# 
# This assumes 12 working months and 50 working weeks.
# 

# Plot the distribution curve for the column `ConvertedComp`.
# 

# In[4]:


# your code goes here
import seaborn as sns
sns.displot(df['ConvertedComp'], kde = True)


# Plot the histogram for the column `ConvertedComp`.
# 

# In[5]:


# your code goes here
import matplotlib as mpl
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.hist(df['ConvertedComp'])


# What is the median of the column `ConvertedComp`?
# 

# In[6]:


# your code goes here
df['ConvertedComp'].dropna(axis=0,inplace=True)
print("ConvertedComp Median:", df['ConvertedComp'].median())


# How many responders identified themselves only as a **Man**?
# 

# In[7]:


# your code goes here
df['Gender'].value_counts()


# Find out the  median ConvertedComp of responders identified themselves only as a **Woman**?
# 

# In[8]:


# your code goes here
df_woman=df[df['Gender']=='Woman']
print("Woman Median:", df_woman['ConvertedComp'].median())


# Give the five number summary for the column `Age`?
# 

# **Double click here for hint**.
# 
# <!--
# min,q1,median,q3,max of a column are its five number summary.
# -->
# 

# In[9]:


# your code goes here
df['Age'].describe()


# Plot a histogram of the column `Age`.
# 

# In[10]:


# your code goes here
plt.hist(df['Age'])


# ## Outliers
# 

# ### Finding outliers
# 

# Find out if outliers exist in the column `ConvertedComp` using a box plot?
# 

# In[11]:


# your code goes here
df_cv = pd.DataFrame(data=df['ConvertedComp'])
df_cv.plot(kind='box', figsize=(8,6))
plt.show()


# Find out the Inter Quartile Range for the column `ConvertedComp`.
# 

# In[12]:


# your code goes here
df['ConvertedComp'].dropna(axis=0,inplace=True)
Q1,Q3=df['ConvertedComp'].quantile(.25),df['ConvertedComp'].quantile(.75)
IQR=Q3 - Q1
print('The Inter Quartile Range for ConvertedComp:', IQR)


# Find out the upper and lower bounds.
# 

# In[13]:


# your code goes here
upper=Q3+(IQR*1.5)
lower=Q1-(IQR*1.5)

print('Upper Bound:', upper)
print('Lower Bound:', lower)


# Identify how many outliers are there in the `ConvertedComp` column.
# 

# In[14]:


# your code goes here
(df['ConvertedComp']<lower) | (df['ConvertedComp']>upper)


# Create a new dataframe by removing the outliers from the `ConvertedComp` column.
# 

# In[15]:


# your code goes here
df2 = df['ConvertedComp'].clip(upper, lower)
df2.describe()


# ## Correlation
# 

# ### Finding correlation
# 

# Find the correlation between `Age` and all other numerical columns.
# 

# In[16]:


# your code goes here
df.corr()


# ## Authors
# 

# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

#  Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2023-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 

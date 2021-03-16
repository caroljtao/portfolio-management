#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tabula
import pandas as pd
from tabula.io import read_pdf
from tabula.io import convert_into


# In[2]:


file_path = 'C:/Users/Caroline Tao/Desktop/lulu20151101.pdf'


# In[4]:


df = read_pdf(file_path,pages="all")


# In[9]:


convert_into(df, "test.csv", output_format="csv", stream=True)


# In[10]:


convert_into(df, "test.csv", output_format="csv", stream=True)


#!/usr/bin/env python
# coding: utf-8

# In[8]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series,DataFrame

url = 'https://www.nirfindia.org/2023/ManagementRanking.html'


result = requests.get(url)
c = result.content

soup = BeautifulSoup(c, 'html.parser')

table = soup.find('table',{'class':'table table-condensed dataTable no-footer dtr-inline'})
table = soup.find_all('table')[0]
df=pd.read_html(str(table))[0]
df


# In[10]:


df.to_csv(r'C:\Users\Akanksha Sharma\Desktop\NIRF_RANKING.csv', index=False )


# In[ ]:





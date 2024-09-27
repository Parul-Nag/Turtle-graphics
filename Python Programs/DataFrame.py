# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:10:10 2024

@author: ITM-USER
"""

import pandas as pd
Name_dict={'Name' : ['Parul','Priya','Kashish','Yamini'],
      'Surname' : ['Nag','Sen', 'Mishra','Rajput'],
      'City' : ['Raipur','Nagpur','Jaipur','Bhilai'],
      'Marks' : [80,55.5,90,75.8]}

b=pd.DataFrame(Name_dict)
'''
#indexing through number
print(b.iloc[1,2])

#indexing through name
print(b.loc[1,'Surname'])
print(b.loc[3,'Marks'])
'''
#printing first 2 columns of DataFrame
'''
print(b.iloc[[0,1,2,3],0])

print(b.iloc[:,0])
'''

#printing first 2 rows of DataFrame
print(b.iloc[[0,1],:])

#printing last 2 columns data of first 2 rows through numbers
print(b.iloc[[0,1],[2,3]])
#printing last 2 columns data of first 2 rows through names
print(b.loc[[0,1],['City','Marks']])

#Creating new columns in DataFrame
b['College']=['ITM','Kalinga','MATS','Rungta']

#Creating new column Percentage from existing column
b['Percentage']=b['Marks']/100

#Creating new column Add from existing column
b['Add']=b['Marks']+b['Percentage']

#Sorting on the basis of column
update=b.sort_values('Percentage',ascending=False).reset_index(drop=True)
print(b.loc[[0,1,2],'Name'])




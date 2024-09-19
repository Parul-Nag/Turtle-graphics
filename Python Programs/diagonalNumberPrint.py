# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:37:38 2024

@author: ITM-USER
"""

num=[
     [1,2,3],
     [2,3,4],
     [3,4,5]
     ]

for i in range(3):
    for j in range(3):
        if (i==j):
            print(num[i][j])
        j +=1
    i +=1
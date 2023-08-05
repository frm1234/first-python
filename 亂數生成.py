# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:25:13 2023

@author: user
"""

import random

day = list(range(1,32))

celsius = []
for _ in range(31):
    celsius.append(round(random.uniform(25,45),ndigits= 2))
    
print (celsius)

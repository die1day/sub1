# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 07:18:30 2022

@author: Jeff
"""
import numpy as np

def cal(x, y):
    if x != 0 and y != 0:
        return np.log(x) * np.exp(y) * 999 - np.log(y)
    elif x > 100:
        return 0
    else:
        return -333
    

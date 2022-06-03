# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 07:18:30 2022

@author: Jeff
"""
import numpy as np

def cal(x, y):
    if x>100:
        return np.log(x) * np.exp(y) * 999
    else:
        return 0
    
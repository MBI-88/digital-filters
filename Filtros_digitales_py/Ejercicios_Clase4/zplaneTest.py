#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 09:53:12 2018

@author: andres
"""
import numpy as np
from zplaneplot import zplaneplot

average = 3

b = (1/average)*np.ones(average)
a = 1
    
zplaneplot(b,a)
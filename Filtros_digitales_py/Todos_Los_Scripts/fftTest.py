#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 11:39:04 2018

@author: andresdido
"""
from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from mpldatacursor import datacursor


plt.close('all')

# Number of samplepoints
N = 1024
# sample frequency
Fs=1024

t = np.linspace(0.0, N/Fs-1/Fs, N)
y = np.sin(50 * 2.0*np.pi*t) + 0.5*np.sin(80.0 * 2.0*np.pi*t)
spectrum_abs = (2/N)*np.abs(scipy.fftpack.fft(y))
frequency = np.linspace(0.0, Fs/2, N/2)

half_spectrum_abs=spectrum_abs[:N//2]

fig, ax = plt.subplots()
ax.stem(frequency, half_spectrum_abs)
plt.show()

datacursor(ax,draggable='True')
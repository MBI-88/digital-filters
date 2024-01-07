#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 17:06:11 2018

@author: andresdido
"""
from scipy.fftpack import fft
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


N = 1024
Fs = 40000

average = 11

t = np.linspace(0, N/Fs, N, endpoint='False')

a1 = 1
a2 = 1
an = 0.2
bias = 3
f1 = 750
f2 = 1250
f3 = 3850
ph1 = 0
ph2 = np.pi/2
ph3 = np.pi/2

x = bias + a1*np.sin(2*np.pi*f1*t+ph1) \
+ a2*np.sin(2*np.pi*f2*t + ph2)
 #    + 0.18*np.cos(2*np.pi*3.85*t)
xn = x + np.random.randn(len(t)) * an


#%%
a=np.array([1])
b=(1/average)*(np.ones((average)))

#y=signal.lfilter(b,a,xn)
y = signal.convolve(b,xn) 

y = y[0:-(average-1)] # Convolution trim
#%%

plt.figure(0)
plt.plot(t, xn, 'b', alpha=0.75,label='noisy')
#plt.plot(t, z, 'r--', t, z2, 'r', t, y, 'k')
plt.legend(loc='best')
plt.grid(True)
plt.show()


plt.plot(t, y, 'r', alpha=0.75,label='filtered')
#plt.plot(t, z, 'r--', t, z2, 'r', t, y, 'k')
plt.legend(loc='best')
plt.grid(True)
plt.show()

#%%

extendedKernel = np.append(b,np.zeros(100*len(b)))
spectrum_abs = (2/len(b))*np.abs(fft(extendedKernel))
half_spectrum_abs=spectrum_abs[:len(spectrum_abs)//2]

normalized_frec=np.linspace(0,np.pi,len(half_spectrum_abs),endpoint=False)

plt.figure(1)
plt.plot(normalized_frec,half_spectrum_abs, 'r', alpha=0.75,
         label='Frequency response')
#plt.plot(t, z, 'r--', t, z2, 'r', t, y, 'k')
plt.legend(loc='best')
plt.grid(True)
plt.show()
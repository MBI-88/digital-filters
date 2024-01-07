#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:29:05 2018

@author: root
"""

# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi, linspace
from scipy import signal
from mpldatacursor import datacursor


t = arange(0.0, 1.0, 0.01)

fig = figure(1)

ax1=fig.add_subplot(1,1,1)
graph=ax1.plot(t, sin(2*pi*t))
ax1.grid(True)
ax1.set_ylim((-2, 2))
ax1.set_ylabel('1 Hz')
ax1.set_title('A sine wave or two')
markers_on = [12, 17, 25, 50]
ax1.plot(t, sin(2*pi*t), '-gD', markevery=markers_on)
datacursor(graph)

fig = figure(19)

ax1=fig.add_subplot(1,1,1)
graph=ax1.plot(t, sin(2*pi*t))
ax1.grid(True)
ax1.set_ylim((-2, 2))
ax1.set_ylabel('1 Hz')
ax1.set_title('A sine wave or two')
markers_on = [12, 17, 25, 50]
ax1.plot(t, sin(2*pi*t), '-gD', markevery=markers_on)
datacursor(graph)

show()
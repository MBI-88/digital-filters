#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

x = bias + a1*np.sin(2*np.pi*f1*t+ph1) + a2*np.sin(2*np.pi*f2*t + ph2)
 #    + 0.18*np.cos(2*np.pi*3.85*t)
xn = x + np.random.randn(len(t)) * an

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


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline, title, grid, figure
from collections import defaultdict
from scipy.signal import tf2zpk

def zplaneplot(b, a, filename=None):
    """Plot the complex z-plane given zeros and poles.
    """
    
        # Get the poles and zeros
    z, p, k = tf2zpk(b, a)

    if np.empty(p): # In case of FIR systems poles must be forced to 0
        p = np.zeros(len(z))

    # Create zero-pole plot
    figure#(figsize=(16, 9))
    #subplot(2, 2, 1)
    
    # get a figure/plot
    ax = plt.subplot(1, 1, 1)
    # TODO: should just inherit whatever subplot it's called in?

    # Add unit circle and zero axes    
    unit_circle = patches.Circle((0,0), radius=1, fill=False,
                                 color='black', ls='solid', alpha=0.1)
    ax.add_patch(unit_circle)
    axvline(0, color='0.7')
    axhline(0, color='0.7')
    
    # Plot the poles and set marker properties
    poles = plt.plot(p.real, p.imag, 'x', markersize=9, alpha=0.5)
    
    # Plot the zeros and set marker properties
    zeros = plt.plot(z.real, z.imag,  'o', markersize=9, 
             color='none', alpha=0.5,
             markeredgecolor=poles[0].get_color(), # same color as poles
             )

    # Scale axes to fit
    r = 1.5 * np.amax(np.concatenate((abs(z), abs(p), [1])))
    plt.axis('scaled')
    plt.axis([-r, r, -r, r])
#    ticks = [-1, -.5, .5, 1]
#    plt.xticks(ticks)
#    plt.yticks(ticks)

    """
    If there are multiple poles or zeros at the same point, put a 
    superscript next to them.
    TODO: can this be made to self-update when zoomed?
    """
    # Finding duplicates by same pixel coordinates (hacky for now):
    poles_xy = ax.transData.transform(np.vstack(poles[0].get_data()).T)
    zeros_xy = ax.transData.transform(np.vstack(zeros[0].get_data()).T)    

    # dict keys should be ints for matching, but coords should be floats for 
    # keeping location of text accurate while zooming

    # TODO make less hacky, reduce duplication of code
    d = defaultdict(int)
    coords = defaultdict(tuple)
    for xy in poles_xy:
        key = tuple(np.rint(xy).astype('int'))
        d[key] += 1
        coords[key] = xy
    for key, value in d.items():
        if value > 1:
            x, y = ax.transData.inverted().transform(coords[key])
            plt.text(x, y, 
                        r' ${}^{' + str(value) + '}$',
                        fontsize=13,
                        )

    d = defaultdict(int)
    coords = defaultdict(tuple)
    for xy in zeros_xy:
        key = tuple(np.rint(xy).astype('int'))
        d[key] += 1
        coords[key] = xy
    for key, value in d.items():
        if value > 1:
            x, y = ax.transData.inverted().transform(coords[key])
            plt.text(x, y, 
                        r' ${}^{' + str(value) + '}$',
                        fontsize=13,
                        )
            
    grid(True, color='0.9', linestyle='-', which='both', axis='both')
    
    title('Poles and zeros')
    
    # Display zeros, poles and gain
    print(str(len(z)) + " zeros: " + str(z))
    print(str(len(p)) + " poles: " + str(p))
    print("gain: " + str(k))
    

    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)
        print('Pole-zero plot saved to ' + str(filename))

average = 3

b = (1/average)*np.ones(average)
a = 1
    
zplaneplot(b,a)


# In[7]:


# Filtor iir
import scipy.signal as sg
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

# para listar las variables que hay en el archivo
#io.whosmat('ecg.mat')
mat_struct = sio.loadmat('ecg.mat')

ecg_one_lead = np.transpose(mat_struct['ecg_lead'])
samp_frec = 1000 # Hz
nyq_frec = samp_frec / 2



# filter design

ws1 = 1 #Hz
wp1 = 3 #Hz
wp2 = 15 #Hz
ws2 = 35 #Hz

#filter_type = 'butter'
#filter_type = 'ellip'
filter_type = 'cheby1'

bp_sos = sg.iirdesign(wp=np.array([wp1, wp2]) / nyq_frec, ws=np.array([ws1, ws2]) / nyq_frec, gpass=0.5, gstop=40., analog=False, ftype=filter_type, output='sos')

w, h = sg.sosfreqz(bp_sos)

plt.figure(2)

plt.title('Digital filter frequency response')
plt.plot(w, 20*np.log10(np.abs(h)))
plt.title('Digital filter frequency response')
plt.ylabel('Amplitude Response [dB]')
plt.xlabel('Frequency (rad/sample)')
plt.grid()
plt.show()


ecg_filtered = sg.sosfiltfilt(bp_sos, ecg_one_lead)

#%matplotlib inline 
#%matplotlib qt5

plt.figure(1)
plt.plot(np.transpose(ecg_one_lead), 'b', np.transpose(ecg_filtered), 'r')
plt.show()


# In[10]:


from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi, linspace
from scipy import signal

t = arange(0.0, 1.0, 0.01)

fig = figure(1)

ax1 = fig.add_subplot(311)
ax1.plot(t, sin(2*pi*t))
ax1.grid(True)
ax1.set_ylim((-2, 2))
ax1.set_ylabel('1 Hz')
ax1.set_title('A sine wave or two')

for label in ax1.get_xticklabels():
    label.set_color('r')

ax2 = fig.add_subplot(312)
ax2.stem(t, sin(2*2*pi*t))
ax2.grid(True)
ax2.set_ylim((-2, 2))
l = ax2.set_xlabel('Hi mom')
l.set_color('g')
l.set_fontsize('large')

ax2 = fig.add_subplot(313)
ax2.plot(t, sin(0.5*2*pi*t))
ax2.grid(True)
ax2.set_ylim((-2, 2))
l = ax2.set_xlabel('Hi mom')
l.set_color('g')
l.set_fontsize('large')
t = linspace(0, 1, 500, endpoint=False)
ax2.plot(t, signal.square(2 * pi * 5 * t))
ax2.set_ylim((-2, 2))

show()


# In[ ]:





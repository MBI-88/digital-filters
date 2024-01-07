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

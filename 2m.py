__author__ = 'student'
import numpy as np
x=int(input())
y = (np.log((np.e**(1/(np.sin(x)+1)))/(5/4+(x**(-15)))))/(np.log(1+x**2))
print(y)


import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.plot(x,(x*x-x-6))
plt.grid(True)
plt.show()

x = np.arange(-10, 10.01, 0.01)
a=np.log((x**2+1)*((np.e)**(-abs(x)/10)))
b=np.log(1+(np.tan(1/(1+(np.sin(x))**2))))
plt.plot(x,a/b)
plt.grid(True)
plt.show()


import math
import pylab
from matplotlib import mlab

tmin = -20.0
tmax = 20.0

dt = 0.1
tlist = mlab.frange (tmin, tmax, dt)
pylab.ion()

for a in range (5):
      ylist = [math.cos(2*t) for t in tlist]
      xlist=[math.sin(t + a) for t in tlist]
      pylab.clf()
      pylab.plot (xlist, ylist)
      pylab.draw()
      pylab.pause(0.03)
pylab.close()

pylab.ioff()
x = np.arange(-10, 10.01, 0.01)
s = input()
plt.plot(x, eval(s))
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
x1 = np.arange(0, 10.01, 0.01)
v, p = np.polyfit(x, y, deg=2, cov=True)
p_f = np.poly1d(v)
plt.plot(x1, p_f(x1))
plt.grid(True)
plt.show()


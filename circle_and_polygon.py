
import matplotlib.pyplot as plt
import numpy as np
import math
fig = plt.figure(figsize=(8, 8))

plt.grid(True)
ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

def cir(r):
    theta = np.arange(0, 2 * np.pi, np.pi/100)
    x0 = r*np.cos(theta)
    y0 = r*np.sin(theta)
    plt.plot(x0, y0,color='r')

def dbx(n,r):
    o=[0,-r]
    N=2/n*math.pi
    x=[o[0]*math.cos(N/2)-o[1]*math.sin(N/2)]
    y=[o[0]*math.sin(N/2)+o[1]*math.cos(N/2)]
    for i in range(n):
        n_x=x[-1]*math.cos(N)-y[-1]*math.sin(N)
        n_y=x[-1]*math.sin(N)+y[-1]*math.cos(N)
        x.append(n_x)
        y.append(n_y)    
        plt.plot(x, y,color='r')

r = 1
n=12
for i in range(n):
    cir(r)
    r=r/math.cos(1/(i+3)*math.pi)
    dbx(i+3, r)
plt.ylim([-r, r])
plt.xlim([-r, r])
plt.show()

import matplotlib.pyplot as plt
import sympy
from sympy.abc import x, y
import numpy as np
import inspect


def cylinder_stream_function(U=1, R=1):
    r = sympy.sqrt(x**2 + y**2)
    theta = sympy.atan2(y, x)
    si = U * (r - R**2 / r) * sympy.sin(theta)
    #print(si)
    return si

def velocity_field(psi):
    u = sympy.lambdify((x, y), psi.diff(y), 'numpy')
    v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')
    
    return u, v

def plot_streamlines(ax, u, v, xlim=(-1, 1), ylim=(-1, 1)):
    x0, x1 = xlim
    y0, y1 = ylim
    Y, X =  np.ogrid[y0:y1:100j, x0:x1:100j]
    U=(psi.diff(y))
    V= -(psi.diff(x))
    stag = sympy.solve([U,V],[x,y])
    for xp,yp in stag:
        try:
            plt.scatter(xp,yp,color='red',marker='o',)
        except TypeError:
            continue
    ax.streamplot(X, Y, u(X, Y), v(X, Y), color='cornflowerblue')
   
    

def format_axes(ax):
    ax.set_aspect('equal')
    ax.figure.subplots_adjust(bottom=0, top=1, left=0, right=1)

    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    ax.axis('off')
    

psi = cylinder_stream_function()
u, v = velocity_field(psi)
xlim = ylim = (-3, 3)
fig, ax = plt.subplots(figsize=(4, 4))
plot_streamlines(ax, u, v, xlim, ylim)
c = plt.Circle((0, 0), radius=1, facecolor='none', fill=False)
ax.add_patch(c)
#stagPoint = sympy.solve((u,v),[x,y])
#for xp, yp in stagPoint:
 #   print(xp,yp)
plt.show()
format_axes(ax)

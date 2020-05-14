import matplotlib.pyplot as plt
import sympy
from sympy.abc import x, y
import numpy as np


def cylinder_stream_function(U=1, R=1):                             #Stream Function
    r = sympy.sqrt(x**2 + y**2)                                     #converts x,y in terms of r,θ 
    theta = sympy.atan2(y, x)
    si = U * (r - R**2 / r) * sympy.sin(theta)
    #print(si)
    return si

def velocity_field(psi):                                            #Velocity Field
    u = sympy.lambdify((x, y), psi.diff(y), 'numpy')                #Differentiates psi w.r.t.y for u and converts it to numpy function for calculation 
    v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')                #Differentiates psi w.r.t.x for -v and converts it to numpy function for calculation
    
    return u, v

def plot_streamlines(ax, u, v, xlim=(-1, 1), ylim=(-1, 1)):         #Plots streamlines and stagnation points
    x0, x1 = xlim
    y0, y1 = ylim
    Y, X =  np.ogrid[y0:y1:100j, x0:x1:100j]
    U=(psi.diff(y))
    V= -(psi.diff(x))
    stag = sympy.solve([U,V],[x,y])                                 #solves u,v and returns x,y for u=v=0 stagnation pt
    for xp,yp in stag:
        try:                                                        #Try block as the solution of stagnation pt contains imginary values
            plt.scatter(xp,yp,color='red',marker='o',)              #plots real values and if imaginary values raises TypeError
        except TypeError:                                           #this block catches the error 
            continue
    ax.streamplot(X, Y, u(X, Y), v(X, Y), color='cornflowerblue')   #plots stream lines 
   
    

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
c = plt.Circle((0, 0), radius=1, facecolor='none', fill=False)      #creates a circular 2D cylinder for better visualisation 
ax.add_patch(c)
plt.show()
format_axes(ax)

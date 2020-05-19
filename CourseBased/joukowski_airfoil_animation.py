import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegWriter


def Joukowski_transformation(z, lam, alpha):			 #Joukowski transformation
    return z+(np.exp(-1j*2*alpha)*lam**2)/z


def circle(C, R):
    t = np.linspace(0,2*np.pi, 200)
    return C+R*np.exp(1j*t)



def deg2radians(deg):
    return deg*np.pi/180



plt.rcParams['figure.figsize'] = 6,6


def streamlines(alpha=0, beta=5, V_inf=1, R=1, ratio=1.2):
    #ratio=R/lam
    alpha = deg2radians(alpha)							# angle of attack
    beta = deg2radians(beta)							# -beta is the argument of the complex no (Joukovski parameter - circle center)
    if ratio <= 1: 										#R/lam must be >1
        raise ValueError('R/lambda must be >1')
    lam = R/ratio       								#lam is the parameter of the Joukowski transformation

    center_c = lam - R*np.exp(-1j*beta)					# Center of the circle
    x = np.arange(-3,3, 0.1)
    y = np.arange(-3,3, 0.1)
    x,y = np.meshgrid(x,y)
    z = x+1j*y
    z = ma.masked_where(np.absolute(z-center_c)<=R, z)
    Z = z-center_c
    Gamma = -4*np.pi*V_inf*R*np.sin(beta+alpha)			#circulation
    

    # np.log(Z) cannot be calculated correctly due to a numpy bug np.log(MaskedArray);
    #https://github.com/numpy/numpy/issues/8516
    # we perform an elementwise computation
    
    
    U = np.zeros(Z.shape, dtype=np.complex)

    with np.errstate(divide='ignore'):					#avoid warning when evaluates np.log(0+1jy).
                                     					#In this case the arg is arctan(y/0)+cst
        for m in range(Z.shape[0]):
            for n in range(Z.shape[1]):
                #U[m,n]=Gamma*np.log(Z[m,n]/R)/(2*np.pi)# 
                 U[m,n]=Gamma*np.log((Z[m,n]*np.exp(-1j*alpha))/R)/(2*np.pi)
    
    c_flow = V_inf*Z*np.exp(-1j*alpha) + (V_inf*np.exp(1j*alpha)*R**2)/Z - 1j*U 
                                                        #the complex flow

    J = Joukowski_transformation(z, lam, alpha)			#Joukovski transformation of the z-plane minus the disc D(center_c, R)
    Circle = circle(center_c, R)
    Airfoil=Joukowski_transformation(Circle, lam, alpha)# airfoil 
    
    return J, c_flow.imag, Airfoil


J, stream_func, Airfoil=streamlines(alpha=0)
levels = np.arange(-2.8, 3.8, 0.2).tolist()

fig = plt.figure()
ax = fig.add_subplot(111)
cp = ax.contour(J.real, J.imag, stream_func,levels=levels, colors='blue', linewidths=1,
                        linestyles='solid')             # this means that the flow is evaluated at Juc(z) 
                                                       #since c_flow(Z)=C_flow(csi(Z))
ax.plot(Airfoil.real, Airfoil.imag)
ax.set_aspect('equal')
ax.set_facecolor('xkcd:sky blue')


def animate(i):
    ax.clear()
    J, stream_func, Airfoil=streamlines(alpha=i)
    levels = np.arange(-2.8, 3.8, 0.2).tolist()

    cp = ax.contour(J.real, J.imag, stream_func,levels=levels, colors='blue', linewidths=1,
                            linestyles='solid')             # this means that the flow is evaluated at Juc(z) 
                                                           #since c_flow(Z)=C_flow(csi(Z))
    ax.plot(Airfoil.real, Airfoil.imag) 
    return cp
anim = FuncAnimation(fig,animate,np.arange(-15,15),repeat=False)
#anim.save('animation.mp4', writer=FFMpegWriter())         #if file not find error occurs u need ffmpeg in python directory
plt.show()
        

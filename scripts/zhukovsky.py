#!/usr/bin/env python

#IMPORTS---------------------------------------
from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import quad
#----------------------------------------------

#CONFIGS N: number of panels ------------------
N=50
twopi = 2*np.pi
#----------------------------------------------

#CONSTANT a, alpha, beta, uinf
a = 0.75
alphadg = 5
alpha = np.radians(alphadg)
beta=-0.05
Uinf = 1
#----------------------------------------------

#FUNCTIONS-------------------------------------

def Zeta(theta):
  return (np.cos(theta)+beta)+(np.sin(theta)+alpha)*1j;

def Zhukovsky(zeta):
  return zeta+a*pow(zeta,-1)

#----------------------------------------------

#DEFINE theta, zeta, z-------------------------
theta = np.arange(0, twopi, twopi/N)
zeta = Zeta(theta)
z = Zhukovsky(zeta)
x = z.real; y = z.imag
#----------------------------------------------

#INITIAL VISUALIZATION-------------------------

plt.figure()
plt.plot(zeta.real, zeta.imag,'g',label=r'$\zeta(\theta) = \xi + i\eta$')
plt.plot(x, y,'r-o',label=r'$z(\theta) = x + iy$')
plt.plot(beta, alpha, 'g+')
plt.grid()
plt.legend()
plt.axis('scaled')
plt.title('Aerofolio fino')
plt.xlabel(r'$a = {0},\, \alpha = {1} graus, \beta = {2}$'.format(a, alphadg, beta))
plt.plot(0, 0, 'k+', ms=10)
#-----------------------------------------------

#GET COEFFICIENTS INFLUENCE MATRIX AND APPLY KUTTA CONDITION
A = np.mat(np.zeros((N+1,N+1)))
A[N,0]  =  1
A[N,N-1]= -1

for i in range(N):
  A[i,N]=1
  for j in range(N):
    if i==j :
      A[i,i]=0.5
    else:
      integrand = lambda t: np.log(abs((z[i]+z[(i+1)%N])/2-Zhukovsky(Zeta(t))))
      A[i,j] = quad(integrand, theta[j], theta[(j+1)%N])[0]/twopi


b = Uinf*(np.concatenate((y,[0])))
#-----------------------------------------------

#SOLVE LINEAR SYSTEM TO OBTAIN gamma AND Cp-----
sol = np.linalg.solve(A, b)

gamma = sol[0:N]
C = sol[N]

print('C={0}'.format(C))

Cp = 1-pow(gamma,2)/(Uinf**2)
#-----------------------------------------------

#PLOT EVERYTHING, SHOW AND SAVE-----------------

plt.figure()
xn = x - min(x)
plt.plot(xn/max(xn), -Cp, 'b-o', label = r'$-C_p(x)$')
plt.legend()

plt.show()
#---:w

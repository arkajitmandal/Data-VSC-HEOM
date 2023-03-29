import numpy as np
import matplotlib.pyplot as plt

from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

eV = 1.0 / 27.2114
cmn1 = 1.0/219474.63

def Vnew(R, wb= 0.02, Eb = 0.4):
    
    wb = wb * cmn1
    Eb = Eb * cmn1
    a1 = wb*wb/2.0
    a2 = a1*a1/(4*Eb)
    c  = 2.27817 * 1E-8
    V  = -a1*R**2 + a2*R**4  - c * R**3  

    V0 = np.min(V)
    return - V0 + V


# Kinetic energy for electron 
def Te(re):
 N = float(len(re))
 mass = 1.0
 Tij = np.zeros((int(N),int(N)))
 Rmin = float(re[0])
 Rmax = float(re[-1])
 step = float((Rmax-Rmin)/N)
 K = np.pi/step

 for ri in range(int(N)):
  for rj in range(int(N)):
    if ri == rj:  
     Tij[ri,ri] = (0.5/mass)*K**2.0/3.0*(1+(2.0/N**2)) 
    else:    
     Tij[ri,rj] = (0.5/mass)*(2*K**2.0/(N**2.0))*((-1)**(rj-ri)/(np.sin(np.pi*(rj-ri)/N)**2)) 
 return Tij

def HO(R, R0,w):
    return 0.5 * (R-R0)**2 * w**2




width= 5
aspect_ratio= 1.13
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

wb  = 1030 
Eb  = 2730
nR  = 1024
Rmax = 100
R = np.linspace(-Rmax,Rmax, nR)
V = Vnew(R,wb,Eb) 

plt.plot(R,  V/cmn1, c =  "#000000", lw = 3)
plt.ylim(-10, 3500)


Hij = Te(R) + np.diag(V)
Ei, Um   = np.linalg.eigh(Hij)
color = ['#ef5777', '#48dbfb', '#8854d0', '#079992', '#e58e26',"#ff9ff3"]

"""
for i in range(0,1):
    plt.plot(R, Um[:,i]*0 + Ei[i]/cmn1, c =  "#000000")
    plt.plot(R,  (Um[:,i+1] - Um[:,i]) * 2000 + Ei[i]/cmn1, c =  color[i], ls = '-')
    plt.fill_between(R,Ei[i]/cmn1,  (Um[:,i+1] - Um[:,i]) * 2000 + Ei[i]/cmn1, facecolor=color[i], alpha = 0.3)

    plt.plot(R, - (Um[:,i+1] + Um[:,i]) * 2000 + Ei[i]/cmn1, c =  color[i+1], ls = '-')
    plt.fill_between(R,Ei[i]/cmn1, - (Um[:,i+1] + Um[:,i]) * 2000 + Ei[i]/cmn1, facecolor=color[i+1], alpha = 0.3)
"""

for i in range(0,6):
    plt.plot(R, Um[:,i]*0 + Ei[i]/cmn1, c =  "#000000")
    plt.plot(R, - Um[:,i] * 4000 + Ei[i]/cmn1, c =  color[i], ls = '-')
    plt.fill_between(R,Ei[i]/cmn1,  - Um[:,i] * 4000 + Ei[i]/cmn1, facecolor=color[i], alpha = 0.3)

plt.xlim(-100, 100)

 
plt.xlabel("R (a.u.)")
plt.ylabel("Energy (cm$^{-1}$)")
#plt.tight_layout()
plt.savefig('S4a.pdf')  
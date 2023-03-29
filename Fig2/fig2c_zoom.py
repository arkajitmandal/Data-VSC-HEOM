from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

def Vnew(R, wb= 0.02, Eb = 0.4):
    
    wb = wb * cmn1
    Eb = Eb * cmn1
    a1 = wb*wb/2.0
    a2 = a1*a1/(4*Eb)
    V  = -a1*R**2 + a2*R**4

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

eV = 1.0 / 27.2114
cmn1 = 1.0/219474.63
wb  = 1000 
Eb  = 2250
nR  = 1024
Rmax = 100
R = np.linspace(-Rmax,Rmax, nR)
V = Vnew(R,wb,Eb) 


def ĉ(nf):
    a = np.zeros((nf,nf))
    for m in range(1,nf):
        a[m,m-1] = np.sqrt(m)
    return a.T

N = 20
cmn1 = 1.0/219474.63
Hij = Te(R) + np.diag(V)
Ei, Um   = np.linalg.eigh(Hij)

µ = (Um.T @ np.diag(R) @ Um)[:N,:N]
H = np.diag(Ei)[:N,:N]

# Data of the diabatic states
def Ĥ(ωc, χ, H, µ, nf, ns):
    #------------------------
    Iₚ = np.identity(nf)
    Iₘ = np.identity(ns)
    #------ Photonic Part -----------------------
    Hₚ = np.identity(nf)
    Hₚ[np.diag_indices(nf)] = np.arange(nf) * ωc  
    â   = ĉ(nf) 
    #--------------------------------------------
    #       matter ⊗ photon 
    #--------------------------------------------
    Hij   = ꕕ(H, Iₚ)                    # Matter
    Hij  += ꕕ(Iₘ, Hₚ)                   # Photon
    Hij  += ꕕ(µ, (â.T + â)) * χ         # Interaction
    Hij  += ꕕ(µ @ µ, Iₚ) * (χ**2/ωc)    # Dipole Self-Energy
    return Hij 
#--------------------------------------------------------
#ωc = np.arange(0.01, 0.3, 0.0003)/27.2114
ωc = np.arange(0.12, 0.162, 0.0001)/27.2114

Epol = np.zeros((20,len(ωc)))
Ucav = np.zeros((20,len(ωc)))

for i in range(len(ωc)):
    HPF = Ĥ(ωc[i], 0.00125 * ωc[i], H, µ, N, 20)
    Ep, Up  = np.linalg.eigh(HPF)
    Epol[:, i] = Ep[:20] 
    Ucav[:, i] = (Up[1, :20]**2 +  Up[ N + 1, :20]**2 +  Up[ 2 * N + 1, :20]**2)\
                + (Up[2, :20]**2 +  Up[ N + 2, :20]**2 +  Up[ 2 * N + 2, :20]**2)\
                + (Up[3, :20]**2 +  Up[ N + 3, :20]**2)\
                + (Up[4, :20]**2 +  Up[ N + 4, :20]**2)\
                + (Up[5, :20]**2 +  Up[ N + 5, :20]**2)\
                + (Up[6, :20]**2 +  Up[ N + 6, :20]**2)\
                + (Up[ 3 * N + 1, :20]**2)\
                + (Up[ 4 * N + 1, :20]**2)

 

from matplotlib import cm as colm

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# (33%,63%,100%)
colors = [(0, 0, 0), (0.33, 0.64, 1)] # first color is black, last is red
cm = LinearSegmentedColormap.from_list(
        "Custom", colors, N=20)

width= 5
aspect_ratio= 1.13
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)


for i in range(16):
    plt.scatter(ωc /cmn1, Epol[i,:]/cmn1, s = 16.0 , c = cm(Ucav[i, :])) 
 
plt.xlim(1100, 1250)
plt.ylim(1700, 2000)


plt.xlabel(r'${\omega_c}$ (cm$^{-1}$)')
plt.ylabel(r'Energy (cm$^{-1}$)')
 
 
plt.savefig('fig2c_zoom.pdf')  
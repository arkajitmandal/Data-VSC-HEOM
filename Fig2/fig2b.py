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

width= 5
aspect_ratio= 1.13
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

wb  = 1000 
Eb  = 2250
nR  = 1024
Rmax = 100
R = np.linspace(-Rmax,Rmax, nR)
V = Vnew(R,wb,Eb) 


plt.ylim(-10, 3500)


Hij = Te(R) + np.diag(V)
Ei, Um   = np.linalg.eigh(Hij)



# State 1 and 2
val = (R<55)*(R>30)
plt.plot(R[val], R[val]*0 + Ei[0]/cmn1, c =   "#000000")
val = (R<-30)*(R>-55)
plt.plot(R[val], R[val]*0 + Ei[0]/cmn1, c =   "#000000")


# State 3
val = (R<60)*(R>15)
plt.plot(R[val], R[val]*0 + Ei[2]/cmn1, c =   "#000000")
val = (R<-15)*(R>-60)
plt.plot(R[val], R[val]*0 + Ei[2]/cmn1, c =   "#000000")


# State 4
val = (R<60)*(R>12)
plt.plot(R[val], R[val]*0 + Ei[3]/cmn1, c =   "#000000")
val = (R<-12)*(R>-60)
plt.plot(R[val], R[val]*0 + Ei[3]/cmn1, c =   "#000000")


# State 5
val = (R<65)*(R>-65)
plt.plot(R[val], R[val]*0 + Ei[4]/cmn1, c =   "#000000")
val = (R<65)*(R>-65)
plt.plot(R[val], R[val]*0 + Ei[5]/cmn1, c =   "#000000")


plt.plot(R,  V/cmn1, c =  "#000000", lw = 3)
 

wc  = 0.14813/27.2114
Hij = Te(R) + np.diag(V) + np.identity(len(V)) * wc
Ei, Um   = np.linalg.eigh(Hij)
 




plt.plot(R,  V/cmn1 + wc/cmn1, c =  '#54a0ff', lw = 6, alpha = 0.2)
plt.plot(R,  V/cmn1 + wc/cmn1, c =  '#2e86de', lw = 2)

# State 1 and 2
val = (R<55)*(R>30)
plt.plot(R[val], R[val]*0 + Ei[0]/cmn1, c = '#54a0ff', lw = 6, alpha = 0.2)
plt.plot(R[val], R[val]*0 + Ei[0]/cmn1, c = '#2e86de', lw = 2)
val = (R<-30)*(R>-55)
plt.plot(R[val], R[val]*0 + Ei[0]/cmn1, c = '#54a0ff', lw = 6, alpha = 0.2)
plt.plot(R[val], R[val]*0 + Ei[0]/cmn1, c = '#2e86de', lw = 2)

# State 3
val = (R<60)*(R>15)
plt.plot(R[val], R[val]*0 + Ei[2]/cmn1, c = '#54a0ff', lw = 6, alpha = 0.2)
plt.plot(R[val], R[val]*0 + Ei[2]/cmn1, c = '#2e86de', lw = 2)
val = (R<-15)*(R>-60)
plt.plot(R[val], R[val]*0 + Ei[2]/cmn1, c = '#54a0ff', lw = 6, alpha = 0.2)
plt.plot(R[val], R[val]*0 + Ei[2]/cmn1, c = '#2e86de', lw = 2)

# State 4
val = (R<60)*(R>12)
plt.plot(R[val], R[val]*0 + Ei[3]/cmn1, c = '#54a0ff', lw = 6, alpha = 0.2)
plt.plot(R[val], R[val]*0 + Ei[3]/cmn1, c = '#2e86de', lw = 2)
val = (R<-12)*(R>-60)
plt.plot(R[val], R[val]*0 + Ei[3]/cmn1, c = '#54a0ff', lw = 6, alpha = 0.2)
plt.plot(R[val], R[val]*0 + Ei[3]/cmn1, c = '#2e86de', lw = 2)



plt.xlim(-100, 100)
plt.ylim(0, 3000)
plt.xlabel("R (a.u.)")
plt.ylabel("Energy (cm$^{-1}$)")
#plt.tight_layout()
plt.savefig('fig2b.pdf')  
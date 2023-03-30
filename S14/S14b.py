from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 16})

width= 5
aspect_ratio= 1.0
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

color = ['#ef5777', '#feca57' , '#ff9ff3', '#00d2d3', '#e58e26',"#ff9ff3"]

dat0 = np.loadtxt("S14b-0.01.out") 
dat1 = np.loadtxt("S14b-0.015.out") 
dat2 = np.loadtxt("S14b-0.0175.out")
dat3 = np.loadtxt("S14b-0.02.out") 
k0 = 6.898744546653864e-06

plt.plot(dat0[:,0], dat0[:,4]/k0, c= color[0], lw  = 4)


print(np.min(dat0[:,4]/k0))
plt.plot(dat1[:,0], dat1[:,1]/k0, c= color[1], lw  = 4)
print(np.min(dat1[:,1]/k0))
plt.plot(dat2[:,0], dat2[:,1]/k0, c= color[2], lw  = 4)
print(np.min(dat2[:,1]/k0))
plt.plot(dat3[:,0], dat3[:,1]/k0, c= color[3], lw  = 4)
print(np.min(dat3[:,1]/k0))


plt.ylim(0.4,1.0)
plt.xlim(500,2000)

plt.savefig('S14b.pdf') 
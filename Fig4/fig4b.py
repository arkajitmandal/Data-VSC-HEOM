from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})


 
width= 4.6
aspect_ratio= 1.05
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)



dat05 = np.loadtxt("fig4b-05.out")
dat025 = np.loadtxt("fig4b-025.out")
dat0125 = np.loadtxt("fig4b-0125.out")


plt.plot(np.arange(0,3000), np.arange(0,3000)* 0 +1, lw = 4, c = 'black')

plt.plot(dat05[:,0], dat05[:,4]/dat05[0,4], c = '#ff6b6b' , lw = 4, solid_capstyle='round')
plt.plot(dat025[:,0], dat025[:,4]/dat025[0,4], c = '#feca57', lw = 4, solid_capstyle='round')
plt.plot(dat0125[:,0], dat0125[:,4]/dat0125[0,4], c = '#00d2d3', lw = 4, solid_capstyle='round')

plt.xlim(650,1900)

plt.savefig('fig4b.pdf') 
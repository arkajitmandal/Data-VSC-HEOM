from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

width= 4.6
aspect_ratio= 0.7
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)
 
dat2  = np.loadtxt("fig5a-rate-QM.out")

plt.plot(dat2[:,0], dat2[:,4]/dat2[0,4], c = '#ff6b6b' , lw = 4, solid_capstyle='round')

 
plt.plot(np.arange(0,3000), np.arange(0,3000)* 0 +1, lw = 4, c = 'black')

 
dat = np.loadtxt("fig5a-rate-CM.out")
plt.plot(dat[1:,0]*8066, dat[1:,1]/dat[0,1], 'o-', lw = 4, c = '#00d2d3')


plt.xlim(700,2000)
plt.ylim(0.67,1.53)
plt.savefig('fig5a.pdf') 
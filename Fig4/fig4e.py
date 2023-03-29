from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

 
width= 4.6
aspect_ratio= 1.05
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

dat05 = np.loadtxt("fig4e-05.out")
#dat025 = np.loadtxt("./structured/r_scan/light_matter_interaction_scan/rates_r_scan_c_5e-7_taum_100_tauc_1000_0.0025.out")
dat0125 = np.loadtxt("fig4e-0125.out")
dat025 = np.loadtxt("fig4e-025.out")


plt.plot(np.arange(0,3000), np.arange(0,3000)* 0 +1, lw = 4, c = 'black')

plt.plot(dat05[:,0], dat05[:,4]/dat05[0,4], c = '#ff6b6b' , lw = 4, solid_capstyle='round')
plt.plot(dat025[:,0], dat025[:,4]/dat025[0,4], c = '#feca57', lw = 4, solid_capstyle='round')
plt.plot(dat0125[:,0], dat0125[:,4]/dat0125[0,4], c = '#00d2d3', lw = 4, solid_capstyle='round')

plt.xlim(650,1900)
plt.savefig('fig4e.pdf') 
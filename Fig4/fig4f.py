from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

width= 4.6
aspect_ratio= 1.0
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

width= 4.6
aspect_ratio= 1.05
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)


dat5E7 = np.loadtxt("fig4f-5E-7.out")
dat2E6 = np.loadtxt("fig4f-2E-6.out")
dat5E6 = np.loadtxt("fig4f-5E-6.out")
#dat0125 = np.loadtxt("./structured/r_scan/light_matter_interaction_scan/rates_r_scan_c_5e-7_taum_100_tauc_1000_0.00125.out")




plt.plot(dat5E7[:,0], dat5E7[:,4]/dat5E7[0,4], c = '#ff6b6b' , lw = 4, solid_capstyle='round')
plt.plot(dat5E6[:,0], dat5E6[:,4]/dat5E6[0,4], c = '#00d2d3', lw = 4, solid_capstyle='round')
plt.plot(dat2E6[:,0], dat2E6[:,4]/dat2E6[0,4], c = '#feca57', lw = 4, solid_capstyle='round')

plt.plot(np.arange(0,3000), np.arange(0,3000)* 0 +1, lw = 4, c = 'black')
plt.xlim(650,1900)

plt.savefig('fig4f.pdf') 
from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

 
width= 4.6
aspect_ratio= 1.0
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)


dat1 = np.loadtxt("S12b-0.025.out")
dat2 = np.loadtxt("S12b-0.05.out")
dat3 = np.loadtxt("S12b-0.075.out")
dat4 = np.loadtxt("S12b-0.1.out")
#dat0125 = np.loadtxt("./structured/r_scan/light_matter_interaction_scan/rates_r_scan_c_5e-7_taum_100_tauc_1000_0.00125.out")


plt.plot(dat1[:,0], dat1[:,2]/dat1[0,1] , c = '#ff6b6b' , lw = 4, solid_capstyle='round')
plt.plot(dat2[:,0], dat2[:,2]/dat2[0,1] , c = '#feca57', lw = 4, solid_capstyle='round')
plt.plot(dat3[:,0], dat3[:,2]/dat3[0,1] , c = '#54a0ff', lw = 4, solid_capstyle='round')
plt.plot(dat4[:,0], dat4[:,2]/dat4[0,1] , c = '#00d2d3', lw = 4, solid_capstyle='round')


plt.plot(np.arange(0,3000), np.arange(0,3000)* 0 +1, lw = 4, c = 'black')
plt.xlim(650,1900)


#plt.ylim(0.65,1.35)
plt.savefig('S12b.pdf') 
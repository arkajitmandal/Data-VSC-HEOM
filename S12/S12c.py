from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 20})
width= 4.6
aspect_ratio= 1.0
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

 
dat3 = np.loadtxt("S12c-QM.out")
 
#dat0125 = np.loadtxt("./structured/r_scan/light_matter_interaction_scan/rates_r_scan_c_5e-7_taum_100_tauc_1000_0.00125.out")


 
plt.plot(dat3[:,0], dat3[:,2]/dat3[0,1] , c = '#54a0ff', lw = 4, solid_capstyle='round')
 




plt.plot(np.arange(0,3000), np.arange(0,3000)* 0 +1, lw = 4, c = 'black')
plt.xlim(650,1900)


#plt.ylim(0.65,1.35)



gledat = np.loadtxt("S12c-CM.out")
plt.plot(gledat[:,0] * 8066,gledat[:,1]/0.12, c = '#05dba8', lw = 5.0)

plt.savefig('S12c.pdf') 
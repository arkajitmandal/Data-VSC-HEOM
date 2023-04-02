import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})


cmn1 = 1.0/219474.63
width= 5
aspect_ratio= 1.05
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

dat = np.loadtxt("S13a.out")

plt.ylim(2e-8,5e-6)
plt.xlim(0,2500)
plt.semilogy(dat[:,0], dat[:,1]+ dat[:,2], label = "Total", c = '#ff6b6b', lw = 6.5)
plt.semilogy(dat[:,0],dat[:,1] , label = "Bath", c = "black", lw = 3.6, ls = '--')
plt.semilogy([1180, 1180], [1e-8, 5e-6], '--', c = 'blue', lw = 1)



plt.ylabel("$J(\omega)$")
plt.xlabel("$\omega$ (cm$^{-1}$)")
  
plt.savefig('S13a.pdf')  
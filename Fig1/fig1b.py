from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})


cmn1 = 1.0/219474.63
width= 5
aspect_ratio= 1.05
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

dat = np.loadtxt("fig1b.out")

plt.ylim(0,0.0000006)
plt.xlim(0,2000)
plt.plot(dat[:,0], dat[:,1]+ dat[:,2], 'k', label = "Total", c = '#ff6b6b', lw = 6.5)
plt.plot(dat[:,0],dat[:,1] , 'r', label = "Bath", c = "black", lw = 3.6, ls = '--')


plt.ylabel("$J(\omega)$")
plt.xlabel("$\omega$ (cm$^{-1}$)")
  
plt.savefig('fig1b.pdf')  
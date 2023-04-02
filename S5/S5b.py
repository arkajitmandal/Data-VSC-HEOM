from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

width= 4.6
aspect_ratio= 1.0
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)


dat  = np.loadtxt("S5b.out")
plt.plot(dat[:,0], dat[:,2]/ dat[0,2], c  = '#ff6b6b', lw = 4)
plt.plot(dat[:,0], dat[:,1]*0 + 1,c  = 'black', lw = 4)

plt.xlim(650,1850)
plt.ylim(0.9,1.2)
plt.savefig('S5b.pdf')  
import numpy as np
import matplotlib.pyplot as plt

from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

width= 5
aspect_ratio= 1.075
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

dat  = np.loadtxt("S4b-200.out")
plt.plot(dat[:,0], dat[:,1], c  = '#ff6b6b', lw = 4)


dat  = np.loadtxt("S4b-1000.out")

plt.plot(dat[:,0], dat[:,1], c  = '#ff9f43', lw = 4)
plt.plot(dat[:,0], dat[:,1]*0 + dat[-1,1],c  = 'black', lw = 4)

plt.xlim(500,2000)


plt.savefig('S4b.pdf')  
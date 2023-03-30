from matplotlib import cm as colm
from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})


width= 5
aspect_ratio= 1.05
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

color = ['#ef5777', '#48dbfb', '#8854d0', '#079992', '#e58e26',"#ff9ff3"]

def plot_curve(filename, label, scalefactor, c = 'black'):
    data = np.genfromtxt(filename)
    plt.plot(data[:, 0], data[:, 1]/scalefactor, label = label, c = c, lw = 5)
 

plt.xlim(750, 2000)
plt.xlabel(r'$\omega_c$ $(\mathrm{cm}^{-1})$')
plt.ylabel(r'$\kappa /\kappa_0$')

gledat = np.loadtxt("S11f-CM.out")
plt.plot(gledat[:,0] * 8066,gledat[:,1]/0.0835, c = '#05dba8', lw = 5.0)
plot_curve(f"S11f-QM.out", r'$\eta=1.25\times10^{-3}$', 1.277283572197006e-07, c ='#54a0ff')
 

plt.plot([750, 2000], [1, 1], 'k', lw = 3, label='no cavity')
plt.ylim(0.95,1.45)

plt.savefig('S11f.pdf')
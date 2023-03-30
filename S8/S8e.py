from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})


width= 5
aspect_ratio= 1.075
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

color = ['#ef5777', '#48dbfb', '#8854d0', '#079992', '#e58e26',"#ff9ff3"]

def plot_curve(filename, label, scalefactor, c = 'black'):
    data = np.genfromtxt(filename)
    plt.plot(data[:, 0], data[:, 1]/scalefactor, label = label, c = c, lw = 2.5)
 
 
plt.xlim(500, 2000)
plt.xlabel(r'$\omega_c$ $(\mathrm{cm}^{-1})$')
plt.ylabel(r'$\kappa /\kappa_0$')


dat = np.loadtxt(f"S8e-0.005.out") 
plt.plot(dat[:,0]* 8066, dat[:,1]/0.075, c= '#184E77', lw = 2.5)

dat = np.loadtxt(f"S8e-0.0025.out") 
plt.plot(dat[:,0]* 8066, dat[:,1]/0.075, c= '#168AAD', lw = 2.5)

dat = np.loadtxt(f"S8e-0.00125.out") 
plt.plot(dat[:,0]* 8066, dat[:,1]/0.075, c= '#52B69A', lw = 2.5)

dat = np.loadtxt(f"S8e-0.000625.out") 
plt.plot(dat[:,0]* 8066, dat[:,1]/0.075, c= '#99D98C', lw = 2.5)

dat = np.loadtxt(f"S8e-0.0003125.out") 
plt.plot(dat[:,0]* 8066, dat[:,1]/0.075, c = '#D9ED92', lw = 2.5)

plt.plot([500, 2000], [1, 1], 'k', lw = 3, label='no cavity')



plt.ylim(0.94,2.35)
plt.savefig('S8e.pdf')  
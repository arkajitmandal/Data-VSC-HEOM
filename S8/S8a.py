from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

width= 5
aspect_ratio= 1.12
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

color = ['#ef5777', '#48dbfb', '#8854d0', '#079992', '#e58e26',"#ff9ff3"]

def plot_curve(filename, label, scalefactor, c = 'black', lw = 2.5):
    data = np.genfromtxt(filename)
    idmax = np.argmin(np.abs(data[:, 0] - 1183))
    plt.plot(data[:, 0], data[:, 4]/scalefactor, label = label, c = c, lw = lw)

data_no_cav = np.genfromtxt(f"S8d-nocav.out")
plt.xlim(500, 2000)
plt.xlabel(r'$\omega_c$ $(\mathrm{cm}^{-1})$')
plt.ylabel(r'$\kappa /\kappa_0$')
 
 
plot_curve(f"S8a-lifetime-100.out", r'100', data_no_cav[0, 4], c ='#F6DA62')
plot_curve(f"S8a-lifetime-200.out", r'200', data_no_cav[0, 4], c = '#F4B757')
plot_curve(f"S8a-lifetime-500.out", r'500', data_no_cav[0, 4], c = '#F3734C')
plot_curve(f"S8a-lifetime-1000.out", r'1000', data_no_cav[0, 4], '#F13D36')
plot_curve(f"S8a-lifetime-2000.out", r'2000', data_no_cav[0, 4], c = '#B62203')
 
plot_curve("S8a-lifetime-infty.out", r'infinity', data_no_cav[0, 4], c = '#48dbfb',  lw = 3)
 

plt.ylim(0.9, 1.85)
plt.savefig('S8a.pdf')
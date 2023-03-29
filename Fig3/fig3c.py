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

def plot_curve(filename, scalefactor, c = 'black'):
    data = np.genfromtxt(filename)
    plt.plot(data[:, 0], data[:, 4]/scalefactor, c = c, lw = 2.5)


plt.xlim(500, 2000)
plt.xlabel(r'$\omega_c$ $(\mathrm{cm}^{-1})$')
plt.ylabel(r'$\kappa /\kappa_0$')
 
data_no_cav = np.genfromtxt(f"fig3c-nocav-0.02.out")
plot_curve(f"fig3c-cav-0.02.out", data_no_cav[0, 4], '#ef5777') 

data_no_cav = np.genfromtxt(f"fig3c-nocav-0.1.out")
plot_curve(f"fig3c-cav-0.1.out", data_no_cav[0, 4], '#ffb854')

 
data_no_cav = np.genfromtxt(f"fig3c-nocav-0.5.out")
plot_curve(f"fig3c-cav-0.5.out", data_no_cav[0, 4], '#b5ee8b')

 
data_no_cav = np.genfromtxt(f"fig3c-nocav-1.5.out")
plot_curve(f"fig3c-cav-1.5.out", data_no_cav[0, 4], '#00e1dd')


 
#plt.legend()
#plt.plot([500, 2000], [1, 1], 'k', lw = 3, label='no cavity')



plt.ylim(0.885,1.35)
plt.savefig('fig3c.pdf')
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

def plot_curve(filename, label, scalefactor, c = 'black'):
    data = np.genfromtxt(filename)
    plt.plot(data[:, 0], data[:, 4]/scalefactor, label = label, c = c, lw = 2.5)
    idx = np.argmin(np.abs(data[:, 0] - 1193.0))
    #print (data[idx, 4]/scalefactor)
    
    
    
 
data_no_cav = np.genfromtxt("fig3a_nocav.out")
plt.xlim(500, 2000)
plt.xlabel(r'$\omega_c$ $(\mathrm{cm}^{-1})$')
plt.ylabel(r'$\kappa /\kappa_0$')



plot_curve("fig3a-eta_0.005.out", r'$\eta=5\times10^{-3}$', data_no_cav[0, 4], '#184E77')
plot_curve("fig3a-eta_0.0025.out", r'$\eta=2.5\times10^{-3}$', data_no_cav[0, 4], c ='#168AAD')
plot_curve("fig3a-eta_0.00125.out", r'$\eta=1.25\times10^{-3}$', data_no_cav[0, 4], c = '#52B69A')
plot_curve("fig3a-eta_0.000625.out", r'$\eta=6.25\times10^{-4}$', data_no_cav[0, 4], c = '#99D98C')
plot_curve("fig3a-eta_0.0003125.out", r'$\eta=3.125\times10^{-4}$', data_no_cav[0, 4], c = '#D9ED92')
#plt.legend()
plt.plot([500, 2000], [1, 1], 'k', lw = 3, label='no cavity')



plt.ylim(0.94,1.35)
 
plt.savefig('fig3a.pdf')
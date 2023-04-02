import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

eV = 1.0 / 27.2114
cmn1 = 1.0/219474.63



width= 5
aspect_ratio= 1.12
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

color = ['#ef5777', '#48dbfb', '#8854d0', '#079992', '#e58e26',"#ff9ff3"]

def plot_curve(filename, label, scalefactor, c = 'black'):
    data = np.genfromtxt(filename)
    plt.plot(data[:, 0], data[:, 2]/scalefactor, label = label, c = c, lw = 2.5)
fold = "."

data_no_cav = np.genfromtxt(f"S10b_1000_no_cavity.out")
plt.xlim(500, 2000)
plt.xlabel(r'$\omega_c$ $(\mathrm{cm}^{-1})$')
plt.ylabel(r'$\kappa /\kappa_0$')



plot_curve(f"{fold}/S10b_0.005.out", r'$\eta_c=5\times10^{-3}$', data_no_cav[0, 4], '#184E77')
plot_curve(f"{fold}/S10b_0.0025.out", r'$2.5\times10^{-3}$', data_no_cav[0, 4], c ='#168AAD')
plot_curve(f"{fold}/S10b_0.00125.out", r'$1.25\times10^{-3}$', data_no_cav[0, 4], c = '#52B69A')
#plt.legend()
plt.plot([500, 2000], [1, 1], 'k', lw = 3, label='no cavity')



plt.ylim(0.94,1.3)
 
plt.savefig('S10b.pdf')
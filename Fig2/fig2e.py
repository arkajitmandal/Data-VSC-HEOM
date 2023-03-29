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
    plt.plot(data[:, 0], data[:, 4]/scalefactor, label = label, c = c, lw = 5)
fold = "./cavity_scan/model_1000/alpha_0.1/cavity_loss/eta_dependence"

data_no_cav = np.genfromtxt(f"fig2d_rates_1000_no_cavity.out")
plt.xlim(500, 2000)
plt.xlabel(r'$\omega_c$ $(\mathrm{cm}^{-1})$')
plt.ylabel(r'$\kappa /\kappa_0$')

gledat = np.loadtxt("fig2e_classical.txt")
plt.plot(gledat[:,0] * 8066,gledat[:,1]/0.076, c = '#05dba8', lw = 5.0)

#plot_curve(f"{fold}/rates_1000_eta_0.005_lifetime_1000.out", r'$\eta=5\times10^{-3}$', data_no_cav[0, 4], '#B9B4FF')
plot_curve(f"fig2d_rates_1000_eta_0.00125_lifetime_100.out", r'$\eta=2.5\times10^{-3}$', data_no_cav[0, 4], c ='#54a0ff')
#plot_curve(f"{fold}/rates_1000_eta_0.00125_lifetime_1000.out", r'$\eta=1.25\times10^{-3}$', data_no_cav[0, 4], c = '#ffb854')
#plot_curve(f"{fold}/rates_1000_eta_0.000625_lifetime_1000.out", r'$\eta=6.25\times10^{-4}$', data_no_cav[0, 4], c = '#05dba8')
#plot_curve(f"{fold}/rates_1000_eta_0.0003125_lifetime_1000.out", r'$\eta=3.125\times10^{-4}$', data_no_cav[0, 4], c = '#009ce6')
#plt.legend()


plt.plot([500, 2000], [1, 1], 'k', lw = 3, label='no cavity')




plt.ylim(0.85,2.0)

plt.savefig('fig2e.pdf')
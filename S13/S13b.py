import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})


width= 5
aspect_ratio= 1.05
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

color = ['#ef5777', '#48dbfb', '#8854d0', '#079992', '#e58e26',"#ff9ff3"]

def plot_curve(filename, label, scalefactor, c = 'black', colind=4, style='-'):
    data = np.genfromtxt(filename)
    plt.plot(data[:, 0], data[:, colind]/scalefactor, label = label, c = c, lw = 5, ls = style)
fold = "./"

data_no_cav = np.genfromtxt(f"S13b_rates_1000_no_cavity.out")
plt.xlim(750, 2000)
plt.xlabel(r'$\omega_c$ $(\mathrm{cm}^{-1})$')
plt.ylabel(r'$\kappa /\kappa_0$')

fold = "./"

#plot_curve(f"{fold}/rates_1000_eta_0.005_lifetime_1000.out", r'$\eta=5\times10^{-3}$', data_no_cav[0, 4], '#B9B4FF')
plot_curve(f"S13b_rates_off_resonant", r'$\omega_Q=1800$ cm$^{-1}$', data_no_cav[0, 4], colind=2, c ='r')
plot_curve(f"S13b_rates_unstructured", r'Unstructured', data_no_cav[0, 4], colind=2, c ='black', style = '--')


plt.plot([750, 2000], [1, 1], 'k', lw = 3, label='no cavity')


plt.savefig('S13b.pdf')
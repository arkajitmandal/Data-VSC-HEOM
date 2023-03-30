from matplotlib import cm as colm
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
    plt.plot(data[:, 0], data[:, 1]/scalefactor, label = label, c = c, lw = lw)

#fold = "./cavity_scan/model_1000/alpha_0.1/cavity_loss/eta_dependence"
#data_no_cav = np.genfromtxt(f"{fold}/rates_1000_no_cavity.out")
plt.xlim(750, 2000)
plt.xlabel(r'$\omega_c$ $(\mathrm{cm}^{-1})$')
plt.ylabel(r'$\kappa /\kappa_0$')


plot_curve(f"S11e-100.out", r'$\tau_c=100$ fs', 1.277283572197006e-07, c ='#F6DA62')
plot_curve(f"S11e-200.out", r'$\tau_c=200$ fs', 1.277283572197006e-07, c = '#F4B757')
plot_curve(f"S11e-500.out", r'$\tau_c=500$ fs', 1.277283572197006e-07, c = '#F3734C')
plot_curve(f"S11e-1000.out", r'$\tau_c=1000$ fs', 1.277283572197006e-07, '#F13D36')
plot_curve(f"S11e-2000.out", r'$\tau_c=2000$ fs', 1.277283572197006e-07, c = '#B62203')

 
#plt.legend()
plt.plot([500, 2000], [1, 1], 'k', lw = 3, label='no cavity')


plt.ylim(0.95,1.45)
 
plt.savefig('S11e.pdf')
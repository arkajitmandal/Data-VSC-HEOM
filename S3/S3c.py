import numpy as np
import matplotlib.pyplot as plt

from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16}) 
width= 4.6
aspect_ratio= 1.1
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)



def plot_curve(filename, label, scalefactor):
    data = np.genfromtxt(filename)
    plt.plot(data[:, 0], data[:, 3]/scalefactor, label = label, c = '#ef5777', lw = 6)
    #plt.plot(data[:, 0], data[:, 4]/scalefactor, label = label)

data_no_cav = np.genfromtxt("S3c-nocav.out")
plt.xlim(400, 1500)
plt.xlabel(r'$\omega_c$ $(\mathrm{cm}^{-1})$')
plt.ylabel(r'$\kappa /\kappa_0$')

plt.plot([400, 2500], [1, 1], 'k', lw = 3, label='no cavity')
plot_curve("S3c-cav.out", r'$\eta=5\times10^{-3}$', data_no_cav[0, 4])
plt.ylim(0.4, 1.05)
plt.savefig('S3c.pdf') 
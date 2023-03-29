import numpy as np
import matplotlib.pyplot as plt

from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})


width= 4.6
aspect_ratio= 1.0
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)


data = np.genfromtxt('S2b.out')
eta = data[:, 0]
k = data[:, 3]
plt.xlim([0, eta[-1]])

k0 = k#/ktst

plt.plot(eta, k0, c =  '#ef5777', lw = 6)

plt.xlabel(r'$\frac{\eta}{\omega_b}$')
plt.ylabel(r'$\kappa$')
plt.xlim(-0.0,1.5)
plt.savefig('S2b.pdf') 
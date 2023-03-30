from matplotlib import cm as colm
from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

width= 4.6
aspect_ratio= 1.0
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)


data = np.genfromtxt(f'S11d.out')
eta = data[:, 0]
k = data[:, 1]
plt.xlim([0, eta[-1]])
 
k0 = k#/ktstt
etainterp = np.arange(eta[0], eta[-1], 0.0001)
K0interp = np.interp(etainterp,eta,k0)

def color(eta):
    def s(x,x0, b):
        #b = 50.0
        return 1/(1 + np.exp(-b * (x-x0)))
    return (1- (s(eta,0.04, 30.0) + s(eta, 1.75, 10.0))/2) *0.75 + 0.25

plt.scatter(etainterp, K0interp * 1E6, c = colm.viridis(color(etainterp)), s = 23)

plt.xlabel(r'$\frac{\eta}{\omega_b}$')
plt.ylabel(r'$\kappa$')
plt.xlim(0.0,0.5)
plt.savefig('S11d.pdf')  
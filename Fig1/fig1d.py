from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

from matplotlib import cm as colm
cmn1 = 1.0/219474.63
Eb  = 2250
wb  = 1000 
width= 4.6
aspect_ratio= 1.05
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)


data = np.genfromtxt('./fig1d.out')
eta = data[:, 0]
k = data[:, 4]
plt.xlim([0, eta[-1]])
#plt.ylim([0, np.amax(k)*1.1])

wbau = wb*cmn1  
Ebau = Eb*cmn1  
w0 = np.sqrt(2.0)*wbau  #frequency in per atomic units of time

w0pfs = w0 * 41.3413733352

#datapgh = np.genfromtxt("pgh_results_"+str(wb)+".out")
ktst = w0pfs/(2*np.pi) * np.exp(-1052.8*(Ebau) )

k0 = k #/ktst
etainterp = np.arange(eta[0], eta[-1], 0.00000001)
K0interp = np.interp(etainterp,eta,k0)

def color(eta):

    def s(x,x0, b):
        #b = 50.0
        return 1/(1 + np.exp(-b * (x-x0)))

    return (1- (1 + s(etainterp, 0.000003, 4000000))/2) *0.75 + 0.25



plt.scatter(etainterp, K0interp * 1E6, c = colm.viridis(color(etainterp)), s = 23)

 
plt.xlabel(r'$C_{Q}$ ($\times$10$^-5$ a.u.)')
plt.ylabel(r'$\kappa$')
#plt.xlim(-0.05,2.5)
plt.savefig('fig1d.pdf')  
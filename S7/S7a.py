from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

data_no_cav = np.genfromtxt("S7a_rates_1000_no_cavity.out")

width= 5
aspect_ratio= 1.06
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)
def plot_curve(filename, label, scalefactor, c = 'black'):
    data = np.genfromtxt(filename)
    plt.plot(data[:, 0], data[:, 4]/scalefactor, label = label, c = c, lw = 5)
    
def plot_spectrum(fname, skip=1, c = 'black', ls = '-'):
    data = np.genfromtxt(fname, skip_header=skip)[:10000, :]
    ct = np.vectorize(complex)(data[...,1], data[...,2])
    yf = np.fft.hfft(ct)
    N = data.shape[0]
    T = (data[1, 0]-data[0, 0])*41.341374575751
    freq = np.fft.fftfreq(2*N-2, d=T)*219474.63*2*np.pi
    #fig, ax = plt.subplots()

    Iw = np.flip(yf)*freq*(1.0-np.exp(-1052*np.abs(freq)/219474.63))
    
    #plt.ylim([0, 60])
    plt.plot(np.sort(freq), Iw[np.argsort(freq)]/7.6E4 + 1 , c = c, lw = 3.5, ls = ls)
    if c !=True:
        plt.fill_between(np.sort(freq),np.sort(freq) * 0,  Iw[np.argsort(freq)]/7.6E4 + 1, facecolor=c, alpha = 0.5)



#fold = "./cavity_scan/model_1000/alpha_0.1/cavity_loss/loss_dependence_0.00125/"
plot_curve(f"S7a_rates_1000_eta_0.00125_lifetime_100.out", r'$\eta=2.5\times10^{-3}$', data_no_cav[0, 4], c ='#54a0ff')
 

 
plot_spectrum(f"S7a_spectra.out", 2, '#ff9f43')
  
plt.xlim([500, 2000])
plt.ylim([1.0, 2])

plt.xlabel(r'$\omega$ ($cm^{-1}$)')
plt.ylabel(r'$\alpha (\omega)$ (Arb. Units)')

 
plt.savefig('S7a.pdf')
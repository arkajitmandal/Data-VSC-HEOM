
import numpy as np
import matplotlib.pyplot as plt

from numpy import kron as ꕕ
from matplotlib import cm as colm
plt.rcParams.update({'font.size': 16})



def plot_spectrum(fname, skip=2, c = '#000000'):
    data = np.genfromtxt(fname, skip_header=skip)[:10000, :]
    ct = np.vectorize(complex)(data[...,1], data[...,2])
    yf = np.fft.hfft(ct)
    N = data.shape[0]
    T = (data[1, 0]-data[0, 0])*41.341374575751
    freq = np.fft.fftfreq(2*N-2, d=T)*219474.63*2*np.pi
    #fig, ax = plt.subplots()
    plt.xlim([500, 2500])
    #plt.ylim([0, 60])
    I1 = np.flip(yf)*freq*freq
    I2 = np.flip(yf)*freq*(1.0-np.exp(-1052*np.abs(freq)/219474.63))
    plt.plot(freq, I1/np.max(I1), c =  c, lw = 4)#*(1.0-np.exp(-1052*np.abs(freq)/219474.63)))
    #plt.plot(freq,  I2/np.max(I2))


width= 5
aspect_ratio= 1.075
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)


plot_spectrum("S1b-IR-Q-2E-6.out", 2, '#ff6b6b')
plot_spectrum("S1b-IR-Q-5E-6.out", 2, '#feca57')
plot_spectrum("S1b-IR-Q-5E-7.out", 2, '#00d2d3')
#plot_spectrum("./structured/ir_spectrum/out_ir_spectator_Q_2e-6")
plt.xlim(650,1900)
 
plt.savefig('S1b.pdf') 
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pylab as pl
import scipy.optimize
import glob
#plt.rcParams.update({'font.size': 20})
def monoExp(x, m, t):
    return -np.abs(t) * x + m

def get_rate(fname, L, rate0, skip = 1, color = 'k'):
    try:
        data = np.genfromtxt(fname, skip_header=skip)
        d2 = data[:, 1]
        t = data[:, 0]
        N = d2.shape[0]*4//5

        p0 = (0.5, 0.1) # start with values near those we expect
        params, cv = scipy.optimize.curve_fit(monoExp, t[N:], np.log(d2[N:]-0.5), p0)
        m, k = params

        beta = 1052.8
        Eb = 0.3/ 27.2114

        assert(d2.shape[0] > 100)
        w0 = (0.2/27.2114)*41.341374575751
        #ktst = w0*np.exp(-beta*Eb)/(2*np.pi)

        #if(d2.shape[0] < 100):
        #    print(fname)
        diff = np.diff(d2)/(t[1]-t[0])
        kappa = -diff/(d2[1:] + (d2[1:]-1))
        N = 1000
        #while(N > d2.shape[0]): 
        #    N = N//2
        kappas = np.convolve(kappa, np.ones(N)/N, mode='valid')
        print(L, m, np.abs(k), kappa[-1], kappas[-1])
        plt.semilogx(t[1:], kappa/rate0, label=str(L), color=color)
        #plt.plot(t[:-N], kappas, '--', label=str(L))#, c=plt.cm.viridis(L/3e-6))#str(L))
        #plt.plot(t, d2-0.5, label=str(L))
        #plt.plot(t, np.exp(monoExp(t, m, k)))
    except: 
        print(fname)
        return None


#filenames = ["out_c", "out", "out_2", "out_3", "out_g", "out_f", "out_25_12"]#["mol_1e-8_4_3.out", "mol_1e-7_15_8.out", "mol_2e-7_15_8.out", "mol_5e-7_20_8.out"]
#filenames = ["out_25_12", "out_30_20", "out_mol_b", "out_4_4_pade"]
#filenames = sorted(glob.glob("model_500/eta_0.005_new/lifetime_1000/run_*.out"), key = lambda x : float(x.split("_")[-2]))
#filenames = sorted(glob.glob("../model_scan/model_1000/friction_scan/run_1.5_*.out"), key = lambda x : float(x.split("_")[-2]))
#filenames = sorted(glob.glob("eta_0.00125_N_24_100ps/K_3/run_*_15.out"), key = lambda x : float(x.split("_")[-2]))

#filenames = sorted(glob.glob("model_1000/additional_loss/eta_0.00125_lifetime_500/run_*.out"), key = lambda x : float(x.split("_")[-2]))
#filenames = sorted(glob.glob("model_1000_alpha_0.02/additional/eta_0.000625/run_*.out"), key = lambda x : float(x.split("_")[-2]))
#filenames = sorted(glob.glob("*550*"))
#filenames = sorted(glob.glob("model_1000/newer_N_16/K_4/run_*.out"))
#filenames = filenames + sorted(glob.glob("run_2e-06*.out"), key = lambda x : float(x.split("_")[1].split(".out")[0]))
#print(filenames)

width= 4
aspect_ratio= 1.12
fig_size = (width, width / aspect_ratio)

data0 = np.genfromtxt("rates_1000_no_cavity.out")
rates0 = data0[2]

plt.figure(1, figsize=fig_size, constrained_layout=True)
get_rate("panel_a/run_670_perfect.out", r"$670$ cm$^{-1}$", rates0, color='#54a0ff')
get_rate("panel_a/run_2500_perfect.out", r"$2500$ cm$^{-1}$", rates0, color='#ef5777')
get_rate("panel_a/run_1195_perfect.out", r"$1195$ cm$^{-1}$", rates0, color='k')

plt.xlim([200, 100000])
plt.ylim([0.5, 3])
plt.xlabel("$t$ (fs)")
plt.ylabel("$\kappa(t; \omega_c)/\kappa_0$ ")
plt.legend()
plt.savefig('S9a.pdf')  


plt.figure(2, figsize=fig_size, constrained_layout=True)
data = np.genfromtxt("panel_b/rates.out")

n=15
colors = pl.cm.afmhot(np.linspace(0,1,n))
ts = ["0.5 ps", "1 ps", "2 ps", "5 ps", "10 ps", "20 ps", "50 ps", "100 ps"]
for i in range(7):
    plt.plot(data[:, 0], data[:, i+1]/rates0, label=ts[i], color=colors[10-(i+1)])
plt.plot(data[:, 0], data[:, 8]/rates0, label=ts[7], color=colors[0], linewidth=2)
plt.xlabel(r"$\omega_c$ (cm$^{-1}$)")
plt.ylabel(r"$\langle\kappa(\omega_c; t)\rangle/\kappa_0$ ")
plt.xlim([500, 2000])
plt.legend()
plt.savefig('S9b.pdf')  

plt.figure(3, figsize=fig_size, constrained_layout=True)
get_rate("panel_c/run_1195_perfect.out", r"$\tau_c = \infty$", rates0, color='k')
get_rate("panel_c/run_1195_2000.out", r"$2000$ fs", rates0, color='#B62203')
get_rate("panel_c/run_1195_1000.out", r"$1000$ fs", rates0, color='#F13D36')
get_rate("panel_c/run_1195_500.out", r"$500$ fs", rates0, color='#F3734C')
get_rate("panel_c/run_1195_200.out", r"$200$ fs", rates0, color='#F4B757')
get_rate("panel_c/run_1195_100.out", r"$100$ fs", rates0, color='#F6DA62')
plt.xlim([200, 20000])
plt.ylim([0.5, 3])
plt.xlabel("$t$ (fs)")
plt.ylabel("$\kappa(t; \omega_c)/\kappa_0$ ")
plt.legend()
plt.savefig('S9c.pdf')  

#plt.show()

#for files in filenames:
#    #print(files)
#    #print(files)
#    freq = float(files.split("_")[-2])
#    #if(freq < 2200 and freq > 1500) or freq < 100:
#    #if(freq < 1000):# and freq > 1200) or freq < 800
#    if(freq >  450):
#        get_rate(files, freq)

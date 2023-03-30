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

 
gledat = np.loadtxt("S8b-100.out")
plt.plot(gledat[:,0] * 8066,gledat[:,1]/0.076, c = '#F6DA62', lw = 5.0, label = '100 fs')
idmax =  4
print (gledat[idmax,1]/0.076,  2*gledat[idmax,2]/0.076)

gledat = np.loadtxt("S8b-200.out")
plt.plot(gledat[:,0] * 8066,gledat[:,1]/0.076, c = '#F4B757', lw = 5.0, label = '200 fs')
idmax =  4
print (gledat[idmax,1]/0.076,  2*gledat[idmax,2]/0.076)


gledat = np.loadtxt("S8b-500.out")
plt.plot(gledat[:,0] * 8066,gledat[:,1]/0.076, c = '#F3734C', lw = 5.0, label = '500 fs')
idmax =  4
print (gledat[idmax,1]/0.076,  2*gledat[idmax,2]/0.076)


gledat = np.loadtxt("S8b-1000.out")
plt.plot(gledat[:,0] * 8066,gledat[:,1]/0.076, c = '#F13D36', lw = 5.0, label = '1000 fs')
idmax =  4
print (gledat[idmax,1]/0.076,  2*gledat[idmax,2]/0.076)


gledat = np.loadtxt("S8b-2000.out")
plt.plot(gledat[:,0] * 8066,gledat[:,1]/0.076, c =  '#B62203', lw = 5.0, label = '2000 fs')
#plt.fill_between(gledat[:,0] * 8066, (gledat[:,1] + 2*gledat[:,2])/0.076,  (gledat[:,1] - 2*gledat[:,2])/0.076, facecolor='#B62203', alpha = 0.3)

idmax =  4
print (gledat[idmax,1]/0.076,  2*gledat[idmax,2]/0.076)
# '#48dbfb'


print (gledat[idmax,0] * 8066)

gledat = np.loadtxt("S8b-infty.out")
plt.plot(gledat[:,0] * 8066,gledat[:,1]/0.076, c = '#48dbfb', lw = 5.0, label = '$\infty$')
idmax =  4
print (gledat[idmax,1]/0.076,  2*gledat[idmax,2]/0.076)


plt.legend()
plt.ylim(0.9, 1.85)
plt.xlim(500, 2000)

plt.savefig('S8b.pdf')
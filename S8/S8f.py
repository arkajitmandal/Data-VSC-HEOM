from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})


width= 5
aspect_ratio= 1.075
fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)


# η = np.array([0.005, 0.0025, 0.00125, 0.000625, 0.0003125])
# kC = np.array([2.1384329605762313, 1.6421717090510257, 1.3171031231626027, 1.1128803723879521, 1.0402863439971488])
# kQ = np.array([1.283247683855546, 1.269535314715419, 1.248771495418419, 1.1839934663698433, 1.0897211468474446])
# δkcl = np.array([0.023691622065771658, 0.025585613283695942, 0.02723666617604276, 0.027949108479794958, 0.030996693120968873])
dat = np.loadtxt("S8f.out") 
η,kC, kQ, δkcl = dat[:,0], dat[:,1], dat[:,2], dat[:,3]


plt.plot(η, kC, 'o-', c  = '#48dbfb', lw = 4)
plt.plot(η, kQ, 'o-', c  = '#ff6b6b', lw = 4)
plt.plot(η, kC + δkcl, '--', c = '#48dbfb', lw = 2)
plt.plot(η, kC - δkcl, '--', c = '#48dbfb', lw = 2)

plt.fill_between(η, kC - δkcl, kC + δkcl , facecolor='#48dbfb', alpha = 0.3)
plt.savefig('S8f.pdf')  
from numpy import kron as ꕕ
from matplotlib import cm as colm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})


width= 5
aspect_ratio= 1.12

fig_size = (width, width / aspect_ratio)
plt.figure(figsize=fig_size, constrained_layout=True)

# tc = np.array([100,200,500,1000,2000,3000])
# kc = np.array([1.7783970418889945,1.70207583460516,1.4271663880155567,1.2513389414385352,1.137849029906495,1]) 
# kcl = np.array([1.3529958090309375, 1.3100733753272227, 1.2831103085259967, 1.2997728189104631, 1.2780362431056613, 1.2566919738970657])
# δkcl = np.array([0.02856101844684924, 0.027819690926555767, 0.027525925453380874, 0.02687828898951588, 0.02769336754099387, 0.027062192378360096])



dat = np.loadtxt("S8c.out")
tc, kc, kcl, δkcl = dat[:,0], dat[:,1], dat[:,2], dat[:,3]

plt.plot(tc, kc, 'o-', c  = '#ff6b6b', lw = 4)
plt.plot(tc, kcl, 'o-', c = '#48dbfb', lw = 4)
plt.plot(tc, kcl + δkcl, '--', c = '#48dbfb', lw = 2)
plt.plot(tc, kcl - δkcl, '--', c = '#48dbfb', lw = 2)
plt.fill_between(tc, kcl - δkcl, kcl + δkcl , facecolor='#48dbfb', alpha = 0.3)

plt.xlim(50,3100)

plt.savefig('S8c.pdf') 
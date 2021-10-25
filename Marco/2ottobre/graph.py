# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:53:24 2021

@author: mrmar
"""
import numpy as np
from matplotlib import pyplot as plt

tt = np.linspace(1/(6*np.pi),1/(np.pi),1000)


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.plot(tt, np.sin(1/tt), ls = '-', label='$\gamma$')
#plt.plot(tt,0*tt, color = 'black')
plt.plot(np.array([1/np.pi,2/(3*np.pi)]),np.array([0,-1]),'r', lw = 1, label = '$\lambda$')
plt.plot(np.array([2/(3*np.pi),1/(2*np.pi)]),np.array([-1,0]),'r', lw = 1)
plt.plot(np.array([1/(2*np.pi),2/(5*np.pi)]),np.array([0,1]),'r', lw = 1)
plt.plot(np.array([2/(5*np.pi),1/(3*np.pi)]),np.array([1,0]),'r', lw = 1)
plt.plot(np.array([2/(7*np.pi),1/(3*np.pi)]),np.array([-1,0]),'r', lw = 1)
plt.plot(np.array([2/(7*np.pi),1/(4*np.pi)]),np.array([-1,0]),'r', lw = 1)
plt.plot(np.array([1/(4*np.pi),2/(9*np.pi)]),np.array([0,1]),'r', lw = 1)
plt.plot(np.array([2/(9*np.pi),1/(5*np.pi)]),np.array([1,0]),'r', lw = 1)
plt.plot(np.array([2/(11*np.pi),1/(5*np.pi)]),np.array([-1,0]),'r', lw = 1)
plt.plot(np.array([2/(11*np.pi),1/(6*np.pi)]),np.array([-1,0]),'r', lw = 1)
plt.grid(alpha =0.7)
plt.axhline(color = 'black', lw=1, zorder =  0)
plt.legend(loc='best')
plt.savefig('img/sin1x.pdf')
plt.show()
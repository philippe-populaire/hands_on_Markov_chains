#!/usr/bin/python

# Hands on Markov Chains example, using Python
# Demystifying Markov Chain one line of code at a time
# Piero Paialunga, Dec 31, 2021
# https://towardsdatascience.com/hands-on-markov-chains-example-using-python-8138bf2bd971

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif' 
plt.rcParams['font.serif'] = 'Ubuntu' 
plt.rcParams['font.monospace'] = 'Ubuntu Mono' 
plt.rcParams['font.size'] = 14 
plt.rcParams['axes.labelsize'] = 12 
plt.rcParams['axes.labelweight'] = 'bold' 
plt.rcParams['axes.titlesize'] = 12 
plt.rcParams['xtick.labelsize'] = 12 
plt.rcParams['ytick.labelsize'] = 12 
plt.rcParams['legend.fontsize'] = 12 
plt.rcParams['figure.titlesize'] = 12 
plt.rcParams['image.cmap'] = 'jet' 
plt.rcParams['image.interpolation'] = 'none' 
plt.rcParams['figure.figsize'] = (12, 10) 
plt.rcParams['axes.grid']=False
plt.rcParams['lines.linewidth'] = 2 
plt.rcParams['lines.markersize'] = 8
colors = ['xkcd:pale orange', 'xkcd:sea blue', 'xkcd:pale red', 'xkcd:sage green', 'xkcd:terra cotta', 'xkcd:dull purple', 'xkcd:teal', 'xkcd: goldenrod', 'xkcd:cadet blue',
'xkcd:scarlet']
#-- custom Markov chain example
trans_matrix=[
[0.2,0.5,0.3,0,0],
[0,0.5,0.5,0,0],
[0,0,0,1.0,0],
[0,0,0,0,1],
[0,0,0,0.5,0.5]
]
#- evolution of p(n)(2,2):
def t(N):
    step = np.arange(1,N+1,1)
    y = []
    for s in step:
        v = 0.5**s
        y.append(v)
    return y
plt.plot(t(10))
plt.ylabel(r'$t(N-1)$',fontsize=20)
plt.xlabel(r'$N-1$',fontsize=20)
plt.show()
#- 
def prob(N):
    states = np.arange(1,6,1)
    steps = np.arange(1,N+1,1)
    n=1000
    state_collection = []
    for k in range(n):
        start = 2 
        for i in range(N):
            start = np.random.choice(states,p=trans_matrix[start-1])
        if start==2:
            state_collection.append(1)
        else:
            state_collection.append(0)
    state_collection = np.array(state_collection)
    return state_collection.sum()/n
def p(N):
    step = np.arange(1,N+1,1)
    y = []
    for s in step:
        v = prob(s)
        y.append(v)
    return y
p_20 = p(20)
plt.plot(t(20),label=r'Theory, $t(N-1)$')
plt.plot(p_20,'x',label=r'Simulation, $p(N-1)$',color='navy')
plt.ylabel(r'Result',fontsize=20)
plt.xlabel(r'$N-1$',fontsize=20)
plt.legend()
plt.show()
#-
def probEnds(N,start):
    states = np.arange(1,6,1)
    n=1000
    state_collection = []
    for s in states:
        state_collection.append(0)
    for k in range(n): 
        for i in range(N):
            start = np.random.choice(states,p=trans_matrix[start-1])
        state_collection[start-1] = state_collection[start-1] + 1
    state_collection = np.array(state_collection)
    n = state_collection.sum()
    return state_collection/n
for start in np.arange(1,6,1):
    print(f'start = {start}')
    sc = probEnds(2000,start)
    print(f'probEnds = {sc}')

# start = 1
# probEnds = [0.   0.   0.   0.31 0.69]
# start = 2
# probEnds = [0.    0.    0.    0.329 0.671]
# start = 3
# probEnds = [0.    0.    0.    0.342 0.658]
# start = 4
# probEnds = [0.    0.    0.    0.353 0.647]
# start = 5
# probEnds = [0.    0.    0.    0.325 0.675]
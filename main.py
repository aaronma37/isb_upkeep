import numpy as np
import math
import random
from scipy import linalg

crit_chance = .3
hit_chance = .95

crit = crit_chance*hit_chance*hit_chance
# hit = 1-crit-miss
# miss = 1-hit_chance

hit = 1-crit
miss = 0 # 1-hit_chance

max_isb_count = 5

def calculate_stationary(pt):
    evals, evecs = np.linalg.eig(pt.T)
    # print(evecs,"G")
    evec1 = evecs[:,np.isclose(evals, 1)]
    # print(evec1/evec1.sum(),"G")
    evec1 = evec1[:,0]
    revals, revecs = np.linalg.eig(pt)
    revec1 = revecs[:,np.isclose(revals, 1)]
    revec1 = revec1[:,0]
    stationary = evec1 / evec1.sum()
    rstationary = revec1 / revec1.sum()
    return stationary 

def generate_transition_matrix():
    pg = np.ones((max_isb_count,max_isb_count))
    for i in range(max_isb_count):
        for j in range(max_isb_count):
            val = 0
            if i==j:
                val+=miss
            if i==j+1:
                val+= hit
            if i==j and i==0:
                val+=hit
            if j==4:
                val+=crit
            pg[i][j]=val
    return pg

p = generate_transition_matrix()
print('\n----Transition matrix-----       \nCrit chance: ', crit_chance, 'Hit chance: ', hit_chance,"\n")
print(p)
stationary = calculate_stationary(p)
print()
print('----Stationary distribution-----')
print(np.real(stationary))
print()
print('----ISB upkeep-----')
print(np.real(np.sum(stationary[1:])))

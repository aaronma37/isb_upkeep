import numpy as np
import matplotlib.pyplot as plt

import math
import random
from scipy import linalg

num_iters = 10000

crit_chance = .30
hit_chance = .95

crit = crit_chance*hit_chance*hit_chance
miss = 1-hit_chance
hit = 1-crit-miss

max_locks = 50
max_isb_count = 4
t = []
v = []

for num_locks in range(1,max_locks):
    early_miss = 0
    curr_isb_count = 0
    isb_hits = 0
    hits = 0 
    for r in range(num_iters):
        roll = random.random()
        if (roll <= miss):
            continue
        elif (roll <= miss+hit): #hit
            hits+=1
            if (curr_isb_count > 0):
                if early_miss > 0:
                    early_miss -= 1
                else:
                    isb_hits+=1
                curr_isb_count -= 1
        else: #crit
            hits+=1
            if (curr_isb_count > 0):
                if early_miss > 0:
                    early_miss -= 1
                else:
                    isb_hits+=1
            else:
                early_miss = num_locks - 1

            curr_isb_count = max_isb_count
    t.append(num_locks)
    v.append(isb_hits/hits*100)

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.grid()
ax1.set(xlabel='num locks', ylabel='isb uptime %',
       title='isb uptime at max distance crit=30%, hit=95%')
ax1.plot(t[:5], v[:5])


ax2.grid()
ax2.set(xlabel='num locks', ylabel='isb uptime %')
ax2.plot(t, v)
plt.show()

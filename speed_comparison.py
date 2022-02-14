# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 15:16:25 2022

@author: Kyle
"""

import util
import numpy as np
import time
import brute_force_solver

#%timeit util.runWordle("guess", "pecan")

#%timeit util.remove_impossible_words(base_words, "guess", GOG)
with open("words.txt", "r") as fp:
    base_words = fp.read().splitlines()
    
b = np.array([ list(word) for word in base_words ])


"""# All words with a in the first slot
t1 = time.time()
for i in range(100):
    remaining_words = [x for x in base_words if (x[0] == 'a')]
t2 = time.time()

diff1 = t2-t1

print(f"time: {diff1} s")

t1 = time.time()
for i in range(100):
    index = (b[:,0] == 'a')
    remaining_words = b[index]
t2 = time.time()
diff2 = t2 - t1
print(f"time: {diff2} s")

print(f"Fractional Diff: {diff1/diff2}")"""

# All words with a in the first slot
t1 = time.time()
brute_force_solver.get_expected_info('crane', base_words)
t2 = time.time()

diff1 = t2-t1

print(f"time: {diff1} s")

t1 = time.time()
brute_force_solver.get_expected_info_optimized('crane', base_words)
t2 = time.time()
diff2 = t2 - t1
print(f"time: {diff2} s")
print(f"Fractional Diff: {diff1/diff2}")
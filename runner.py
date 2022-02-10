# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:26:51 2022

@author: Kyle
"""
import random
from random_solver import random_solver
import matplotlib.pyplot as plt
import numpy as np

with open("words.txt", "r") as fp:
    base_words = fp.read().splitlines()
random.seed(0)
N = len(base_words)


# Compute for all words
maxGuesses = 6
counts = [0] * (maxGuesses + 1)
for correct_word in base_words:
    guessList = random_solver(correct_word, base_words)
    L = len(guessList)
    if (L <= maxGuesses):
        counts[L-1] += 1
    else:
        counts[maxGuesses] += 1
        
        
# Plot it
plt.figure(figsize=(8, 6), dpi=80)
counts = np.array(counts)
percents = np.array(counts, dtype='float') / np.sum(counts)
plt.bar(["1","2","3","4","5","6","7+"], percents)
plt.ylabel("Percentage")
plt.xlabel("Num Guesses")
plt.title("Random Guesser")
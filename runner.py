# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:26:51 2022

@author: Kyle
"""
import os
os.chdir('A:\\wordle\\WorldeBot')
import random
from tqdm import tqdm
#from random_solver import random_solver
from brute_force_solver import brute_force_solver
import matplotlib.pyplot as plt
import numpy as np
import time

from itertools import repeat
from multiprocessing import Pool, freeze_support



def get_guess_lists(correct_word, base_words):
    #return ['guess1', 'guess2','3','4','5','6','7']
    return brute_force_solver(correct_word, base_words)


def main():
    print("BOOTING UP!")
    with open("words.txt", "r") as fp:
        base_words = fp.read().splitlines()
    random.seed(0)
    N = len(base_words)
    
    with Pool(6) as pool:
        print("IN THE POOL NOW")
        inputs = zip(base_words, repeat(base_words))
        result = pool.starmap(get_guess_lists, \
                              tqdm(inputs,total=N))
        print(result)
    maxGuesses = 6
    counts = [0] * (maxGuesses + 1)
    for guessList in result:
        L = len(guessList)
        if (L <= maxGuesses):
            counts[L-1] += 1
        else:
            counts[maxGuesses] += 1
    plt.figure(figsize=(8, 6), dpi=80)
    counts = np.array(counts)
    print(counts)
    percents = np.array(counts, dtype='float') / np.sum(counts)
    plt.bar(["1","2","3","4","5","6","7+"], percents)
    plt.ylabel("Percentage")
    plt.xlabel("Num Guesses")
    plt.title("Random Guesser")
    plt.show()
        

if __name__=="__main__":
    print("HRGHHH")
    freeze_support()
    main()

"""# Compute for all words
maxGuesses = 6
counts = [0] * (maxGuesses + 1)
for correct_word in base_words:
    guessList = brute_force_solver(correct_word, base_words)
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
plt.title("Random Guesser")"""
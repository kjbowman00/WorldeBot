# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:21:21 2022

@author: Kyle
"""
import random
import util
    
def random_solver(correct_word, base_words):
    """! Solves with random guesses among possible words remaining
    """
    
    count = 0
    remaining_words = base_words
    guess = ""
    guessList = []
    while (guess is not correct_word):
        count += 1

        guess = remaining_words[random.randrange(len(remaining_words))]
        guessList.append(guess)
        GOG = util.runWordle(guess, correct_word)
        remaining_words = util.remove_impossible_words( \
            remaining_words, guess, GOG)
    return guessList

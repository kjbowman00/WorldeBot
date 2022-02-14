# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:52:02 2022

@author: Kyle
"""
import util
import numpy as np

def get_expected_info(guess, remaining_words):
    info_list = []
    for correct_word in remaining_words:
        # simualte if this was the correct word - how much info do we reveal
        GOG = util.runWordle(guess, correct_word)
        remain_simulated = util.remove_impossible_words( \
           remaining_words, guess, GOG)
        
        info_revealed = len(remaining_words) - len(remain_simulated)
        info_list.append(info_revealed)
    return np.mean(info_list)

def get_expected_info_optimized(guess, remaining_words):
    info_list = []
    b = np.array([ list(word) for word in remaining_words ])
    # Get letter counts for all possible words
    all_letter_counts = np.array( \
        [util.letter_counter(word) for word in remaining_words])
    for correct_word in remaining_words:
        # simualte if this was the correct word - how much info do we reveal
        GOG = util.runWordle(guess, correct_word)
        remain_simulated = util.remove_impossible_words_optimized( \
            b, all_letter_counts, guess, GOG)
        # give an info score:
        info_revealed = len(remain_simulated)
        info_list.append(info_revealed)
    return 1 / np.mean(info_list)

def get_best_guess(guessable_words, remaining_words):
    best_expected_info = 0
    best_guess = ""
    phase2 = False
    for guess in guessable_words:
        expected_info = get_expected_info_optimized(
            guess, remaining_words)

        if expected_info > best_expected_info:
            best_guess = guess
            best_expected_info = expected_info
        elif expected_info == best_expected_info:
            #guess within remaining words if score is equal
            if (guess in remaining_words):
                best_guess = guess
                best_expected_info = expected_info
        #print(f"Guess: {guess}, EI: {expected_info}")
            
    return best_guess


def brute_force_solver(correct_word, base_words):
    count = 0
    remaining_words = base_words
    guess = "raise"
    guessList = [guess]
    while (guess != correct_word):
        count += 1
        if (count >= 7):
            guessList.append("FAIL")
            break
        GOG = util.runWordle(guess, correct_word)
        remaining_words = util.remove_impossible_words( \
            remaining_words, guess, GOG)
        #print(remaining_words)
        guess = get_best_guess(base_words, remaining_words)
        guessList.append(guess)
    return guessList



with open("words.txt", "r") as fp:
    base_words = fp.read().splitlines()

#best_guess = get_best_guess(base_words, base_words)
#print(best_guess)
#guessList = brute_force_solver("cynic", base_words)
#print(guessList)


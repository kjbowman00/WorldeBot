# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:52:11 2022

@author: Kyle
"""
from enum import Enum
import numpy as np


def letter_counter(word):
    """! Computes a list of letter counts for a word (length 26 list)
    @param word the word to compute
    @return A list of length 26 with how many occurrences of each letter.
    """
    letter_count = [0] * 26
    for letter in word:
        letter_count[ord(letter) - 97] += 1
    return letter_count




def boolean_index(array):
    """
    Takes a numpy array and isolates all points that are within [0.2,0.4] for
    the first dimension and between [0.4,0.6] for
    the second dimension by creating a boolean index.
    """
    index = (array[:, 0] >= 0.2) & (array[:, 1] >= 0.4) & (array[:, 0] <= 0.4) & (array[:, 1] <= 0.6)

    return array[index]

def remove_impossible_words(remaining_words, guess, GOG):
    """! Removes impossible words given a guess and Green/Orange/Gray sequence
    
    @param remaining_words The list of currently possible words
    @param guess your guessed word (string)
    @param GOG List of colors for each character in the guess
    
    @return an updated list of remaining_words
    """
    # Grab amount of correct letters (green or orange)
    letter_count_current= [0] * 26
    for spot, color in enumerate(GOG):
        guessLetter = guess[spot]
        guessNum = ord(guessLetter) - 97
        if (color == "green"):
            letter_count_current[guessNum] += 1
        elif (color == "orange"):
            letter_count_current[guessNum] += 1

    # Removes words from list without knowing the correct word (given GOG)
    # -----------------------------------------
    # Remove words from list
    # -----------------------------------------
    # if green -> Remove all without that spot
    # if orange -> remove all within that spot and less num of chars of each type
    # if gray -> remove all with those letters
    for spot, color in enumerate(GOG):
        guessLetter = guess[spot]
        guessNum = ord(guessLetter) - 97
        if (color == "green"):
            # all equal in that spot remain
            remaining_words = [x for x in remaining_words if (x[spot] == guessLetter)]
        elif (color == "orange"):
            # all not equal in that spot remain
            remaining_words = [x for x in remaining_words if (x[spot] != guessLetter)]
            # all with correct number of chars remain:
        else: # Gray
            # Gray -> letter doesn't exist or all already found (EE _ _ E, last E could be gray)
            # Remove all words with greater than found number of that letter
            # aka keep all with less than or equal
            remaining_words = [x for x in remaining_words if (letter_counter(x)[guessNum] <= letter_count_current[guessNum])]
                
    return remaining_words # convert back to list

def remove_impossible_words_optimized(b, all_letter_counts, guess, GOG):
    """! Removes impossible words given a guess and Green/Orange/Gray sequence
    
    @param remaining_words The list of currently possible words
    @param guess your guessed word (string)
    @param GOG List of colors for each character in the guess
    
    @return an updated list of remaining_words
    """
    # Grab amount of correct letters (green or orange)
    letter_count_current= [0] * 26
    for spot, color in enumerate(GOG):
        guessLetter = guess[spot]
        guessNum = ord(guessLetter) - 97
        if (color == "green"):
            letter_count_current[guessNum] += 1
        elif (color == "orange"):
            letter_count_current[guessNum] += 1

    # Removes words from list without knowing the correct word (given GOG)
    # -----------------------------------------
    # Remove words from list
    # -----------------------------------------
    # if green -> Remove all without that spot
    # if orange -> remove all within that spot and less num of chars of each type
    # if gray -> remove all with those letters
    index = b[:,0] == b[:,0]
    for spot, color in enumerate(GOG):
        guessLetter = guess[spot]
        guessNum = ord(guessLetter) - 97
        if (color == "green"):
            # all equal in that spot remain
            index = (index) & (b[:,spot] == guessLetter)
            #b = b[index]
            #all_letter_counts = all_letter_counts[index]
        elif (color == "orange"):
            # all not equal in that spot remain
            index = (index) & (b[:,spot] != guessLetter)
            #b = b[index]
            #all_letter_counts = all_letter_counts[index]
            # all with correct number of chars remain:
        else: # Gray
            # Gray -> letter doesn't exist or all already found (EE _ _ E, last E could be gray)
            # Remove all words with greater than found number of that letter
            # aka keep all with less than or equal
            index = (index) & (all_letter_counts[:,guessNum] <= letter_count_current[guessNum])
            #b = b[index]
            #all_letter_counts = all_letter_counts[index]
                
    return b[index]

def runWordle(guess, correct_word):
    """! Simulate wordle by calculating the green/orange/gray for a guess
    
    @param guess the guessed word
    @param correct_word the correct word

    @return A list of colors corresponding to each character in the guess
    """
    # Compute letter count for correct_word
    correct_letter_count = letter_counter(correct_word)
    
    GOG = [None] * len(guess)
    letter_count_current = [0] * 26
    
    # Note:
    # Green must be done before any orange or gray because of triples
    # example: actual: EXXXE, guess: EE _ _ E. If orange/greens go at
    # the same time, then the second E would be marked orange when it should be gray
    for spot, letter in enumerate(guess):
        letterNum = ord(letter) - 97
        if (letter == correct_word[spot]):
            # GREEN
            GOG[spot] = "green"
            letter_count_current[letterNum] += 1
    for spot, letter in enumerate(guess):
        letterNum = ord(letter) - 97
        # Is there already counted letters of this type? are there more to count?
        if (GOG[spot] == "green"):
            continue #ignore this one - already handled above
        elif (letter_count_current[letterNum] < correct_letter_count[letterNum]):
            # ORANGE
            GOG[spot] = "orange"
            letter_count_current[letterNum] += 1
        else:
            GOG[spot] = "gray"
    return GOG
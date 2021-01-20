#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
"""

import random
import play_hand

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"
word_list = play_hand.load_words()


def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    handlen = 0
    for v in hand.values():
        handlen += v

    return handlen


def hand_to_list(hand):
    """
    Helper Function
    transfer current hand to a list, so we can use random.sample()
    """
    ls = []
    for letter in hand.keys():
        # iterate letter key value times
        for j in range(hand[letter]):
            ls = ls + [letter]
    # create a list of letters
    return ls


def choose_word(hand, N=100):
    """
    choose best word for current hand by N simulations,
    then calculate its score
    if can't find a word return none and score=0
    """

    bestscore = 0
    bestword = None

    hand_list = hand_to_list(hand)
    ## we change the hand from a dict to a list in order to use random.sample

    for i in range(1, N):  ##we look for word of different length

        n = calculate_handlen(hand) + 1  ##we calculate the length of the hand to fdefine the length of the word
        k = int(random.uniform(1, n))

        # length_word=random.randrange(1,n,1)
        word_test = random.sample(hand_list, k)  ##we look for a random word of length i
        # word_test is a list
        word = ''.join(word_test)
        # Word is a string

        if play_hand.is_valid_word(word, hand, word_list) == True:
            # word=str, hand=dict
            # n = calculate_handlen(hand) ##we calculate the length of the hand to calculate the score
            score = play_hand.get_word_score(word, n)  # we calculate the score
            if score > bestscore:  # if the score is better than the previous one, we keep it
                bestscore = score
                bestword = word

    return bestword, bestscore


def play_mc_hand(hand, N=100):
    """
    repeat choose best word process,
    find best word and score for currrent hand
    until game ends
    return total score and words found in a list
    """
    handscore = 0  # Score for the hand
    wordls = []  # List of words in order played

    n = calculate_handlen(hand)

    # while choose_word(hand,N) is not (None,0):

    while n > 0:  # as long as we have letters in the hand we keep searching for words

        bestword, bestscore = choose_word(hand, N=100)  # return the bestword and bestscore
        if bestword != None:  # if we found a word
            wordls.append(bestword)  # we upload it in the list
            handscore += bestscore  # and we add it to the toalscore
            hand = ps2.update_hand(hand, bestword)  # we recalculate the new hand to remove the letters used
            n = calculate_handlen(hand)
        else:
            break
    return wordls, handscore


def play_n_mc_hand(hand, N, n):
    """
    Simulated n hands generating N candidate words for each round.
    Return two lists: a nested list of hands(each itself is a list) played and a list of scores.

    """
    # create two empty lists

    mc_hands = []
    mc_scores = []

    for i in range(1, n + 1):
        (wordls, handscore) = play_mc_hand(hand, N=100)
        mc_hands.append(wordls)
        mc_scores.append(handscore)

    return (mc_hands, mc_scores)


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.

    * The user may input a word.
    * When any word is entered (valid or invalid), it uses up letters
      from the hand.
    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # Keep track of the total score
    totalscore = 0

    # As long as there are still letters left in the hand:
    handlen = calculate_handlen(hand)
    while handlen > 0:

        # Display the hand
        play_hand.display_hand(hand)

        # Ask user for input
        word = input('Enter a word: ')
        """
        add choose_word() option when input is "?"
        """
        # If the input is two exclamation points:
        if word == '!!':
            # End the game (break out of the loop)
            break

        elif word == '?':
            # IMPLEMENT ME
            (bestword, bestscore) = choose_word(hand, N=100)
            if bestword == None:
                print("No word could be find in this hand.")
            else:
                print("You could use the word ", bestword, " that is worth ", bestscore)



        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if play_hand.is_valid_word(word, hand, word_list):

                # Tell the user how many points the word earned,
                # and the updated total score
                handscore = play_hand.get_word_score(word, handlen)
                print('You earned {} points.'.format(handscore))
                totalscore += handscore

            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print('Invalid word')

            # update the user's hand by removing the letters of their inputted word
            hand = play_hand.update_hand(hand, word)
            handlen = calculate_handlen(hand)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print('Total score is {}.'.format(totalscore))

    # Return the total score as result of function
    return totalscore


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    # Generate a (reproducible) hand
    word_list = play_hand.load_words()
    random.seed(1)
    hand = play_hand.deal_hand(15)

    # Set the number of MC samples
    N = 100

    # Choose a word from the hand
    print(choose_word(hand, N))

    # Play the hand using MC
    c = play_mc_hand(hand, N)
    print(c)

    # Play n MC hands
    n = 50
    (mc_hands, mc_scores) = play_n_mc_hand(hand, N, n)
    print(mc_hands)
    print(mc_scores)

    # Play the hand manually with help
    play_hand(hand, word_list)





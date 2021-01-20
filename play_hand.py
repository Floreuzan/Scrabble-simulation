# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:27:09 2019

@author: flore
"""

from create_hand import load_words
from create_hand import get_word_score
from create_hand import display_hand
from create_hand import deal_hand
from create_hand import update_hand
from create_hand import is_valid_word
from create_hand import calculate_handlen


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}



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

    total_score = 0  # Keep track of the total score
    n = calculate_handlen(hand)

    print('Current hand :', end='')
    display_hand(hand)  # Display the hand

    while n > 0:  # As long as there are still letters left in the hand:
        score = 0

        word = str(input('Enter word , or "!!" to indicate that you are finished:'))  # Ask user for input

        if word == '!!':  # If the input is two exclamation points:

            print('Total score: ', total_score)
            return (total_score)  # End the game (break out of the loop)

        elif is_valid_word(word, hand, word_list) == False:  # Otherwise (the input is not two exclamation points):
            hand = update_hand(hand, word)

            print('This is not a valid word. Please choose another word.')
            print('Current hand :', end='')
            display_hand(hand)

            # if not (word in word_list):
            # print('This is not a valid word. Please choose another word.')  # Reject invalid word (print a message)

            # else:
            # print('This is not a valid word. Please choose another word.')
            # hand=update_hand(hand,word)

        else:  # If the word is valid:
            score = get_word_score(word, n)
            total_score += score

            print(word, 'earned', score, 'points. Total: ', total_score,
                  'points')  # Tell the user how many points the word earned,
            # and the updated total score

            hand = update_hand(hand, word)  # update the user's hand by removing the letters of their inputted word

            print('Current hand :', end='')
            display_hand(hand)

            n = calculate_handlen(hand)

    print('Ran out of letters. Total sore:', total_score, 'points.')
    return total_score
    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    # Return the total score as result of function


if __name__ == '__main__':
    word_list = load_words()
    hand = deal_hand(15)
    play_hand(hand, word_list)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author:
"""

import random
import play_hand
import monte_carlo_hand

word_list = play_hand.load_words()


def test_mc_player(hand, N=100, seed=1):
    """
    play a hand 3 times, make sure produced same scores.

    """
    random.seed(seed)
    a, b = monte_carlo_hand.play_mc_hand(hand, N=100)

    random.seed(seed)
    c, d = monte_carlo_hand.play_mc_hand(hand, N=100)

    random.seed(seed)
    e, f = monte_carlo_hand.play_mc_hand(hand, N=100)

    if b == d == f:
        return True
    else:
        return False


if __name__ == "__main__":

    # Set the MC seed
    seed = 100

    test_hands = ['helloworld', 'UMasswins', 'statisticscomputing']
    for handword in test_hands:
        hand = play_hand.get_frequency_dict(handword)
        if not test_mc_player(hand, seed=seed):
            print('Reproducibility problem for %s' % handword)

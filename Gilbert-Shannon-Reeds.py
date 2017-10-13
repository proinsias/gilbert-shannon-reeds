# coding: utf-8
import matplotlib
matplotlib.use('nbagg')
import matplotlib.pyplot as plt
import numpy as np
import sklearn.utils
# Note that the functions below have `doctest` examples.
# To test the functions, just run `pytest` in the top level of the repository.
def get_random_number_for_right_deck(n: int, seed: int=None, ) -> int:
    """
    Return the number of cards to split into the right sub-deck.
    :param n: one above the highest number that could be returned by this function.
    :param seed: optional seed for the random number generator to enable deterministic behavior.
    :return: a random integer (between 1 and n-1) that represents the desired number of cards.
    Examples:
    >>> get_random_number_for_right_deck(n=5, seed=0, )
    1
    """
    random = sklearn.utils.check_random_state(seed=seed, )
    return random.randint(low=1, high=n, )
def should_drop_from_right_deck(n_left: int, n_right:int, seed: int=None, ) -> bool:
    """
    Determine whether we should drop a card from the right or left sub-deck.
    Either `n_left` or `n_right` (or both) must be greater than zero.
    :param n_left: the number of cards in the left sub-deck.
    :param n_right: the number of cards in the right sub-deck.
    :param seed: optional seed for the random number generator to enable deterministic behavior.
    :return: True if we should drop a card from the right sub-deck, False otherwise.
    Examples:
    >>> should_drop_from_right_deck(n_left=32, n_right=5, seed=0, )
    True
    >>> should_drop_from_right_deck(n_left=0, n_right=5, )
    True
    >>> should_drop_from_right_deck(n_left=7, n_right=0, )
    False
    >>> should_drop_from_right_deck(n_left=0, n_right=0, )
    Traceback (most recent call last):
    ...
    ValueError: Either `n_left` or `n_right` (or both) must be greater than zero.
    """
    if n_left > 0 and n_right > 0:
        # There are cards left in both sub-decks, so pick a sub-deck at random.
        random = sklearn.utils.check_random_state(seed=seed, )
        num = random.randint(low=0, high=2, )
        boolean = (num == 0)
        return boolean
    elif n_left == 0 and n_right > 0:
        # There are no more cards in the left sub-deck, only the right sub-deck,
        # so we drop from the right sub-deck.
        return True
    elif n_left > 0 and n_right == 0:
        # There are no more cards in the right sub-deck, only the left sub-deck,
        # so we drop from the left sub-deck.
        return False
    else:
        # There are no more cards in either sub-deck.
        raise ValueError ('Either `n_left` or `n_right` (or both) must be greater than zero.')
def shuffle(deck: list, seed: int=None, ) -> list:
    """
    Shuffle the input 'deck', a sequence of integers.
    This implementation uses lists, and so performance may suffer for very large input sequences.
    :param seq: the input sequence of integers.
    :param seed: optional seed for the random number generator to enable deterministic behavior.
    :return: A new deck containing shuffled integers from the input deck.
    Examples:
    >>> shuffle(deck=[0, 7, 3, 8, 4, 9, ], seed=0, )
    [4, 8, 3, 7, 0, 9]
    """
    # First randomly divide the 'deck' into 'left' and 'right' 'sub-decks'.
    n = len(deck)
    number_for_right_deck = get_random_number_for_right_deck(n=n, seed=seed, )
    right_deck = deck[0: number_for_right_deck]
    n_right = len(right_deck)
    left_deck = deck[number_for_right_deck: n]
    n_left = len(left_deck)
    shuffled_deck = []
    while n_left + n_right > 0:
        # There are some cards left in the sub-decks.
        drop_from_right_deck = should_drop_from_right_deck(
            n_left=n_left,
            n_right=n_right,
            seed=seed,
        )
        if drop_from_right_deck is True:
            # Drop from the bottom of right sub-deck onto the shuffled pile.
            shuffled_deck.append(right_deck[-1])
            right_deck = right_deck[0:len(right_deck)-1]
            n_right = len(right_deck)
        else:
            # Drop from the bottom of left sub-deck onto the shuffled pile.
            shuffled_deck.append(left_deck[-1])
            left_deck = left_deck[0:len(left_deck)-1]
            n_left = len(left_deck)
    return shuffled_deck

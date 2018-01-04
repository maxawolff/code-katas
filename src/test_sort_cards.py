"""Test file for sorting deck of cards kata."""

import pytest
from sort_cards import sort_cards


res = [(['A'], ['A']), (['3'], ['3']), (['T'], ['T']),
       (['T', '8', '2', '4', 'Q'], ['2', '4', '8', 'T', 'Q']),
       (['Q', 'K', 'J', '6', '9', '3', '2'],
        ['2', '3', '6', '9', 'J', 'Q', 'K']),
       (['J', '6', '9', '3', '2', '7', 'A', '8'],
        ['A', '2', '3', '6', '7', '8', '9', 'J']),
       (['J', '6', '7', '9', 'J', '7', '3', '2', '7', 'A', '8'],
        ['A', '2', '3', '6', '7', '7', '7', '8', '9', 'J', 'J']),
       (['T', 'A', '8', 'A', 'A', 'A', '2', '4', 'A', 'Q', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A', '2', '4', '8', 'T', 'Q'])]


@pytest.mark.parametrize('deck, sorted_deck', res)
def test_merge_sort(deck, sorted_deck):
    """Test that deck of cards is sorted correctly."""
    assert sort_cards(deck) == sorted_deck

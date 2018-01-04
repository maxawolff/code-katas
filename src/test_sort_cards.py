"""Test file for sorting deck of cards kata."""


def test_merge_sort():
    """Test that merge sort is correctly linked."""
    from sort_cards import sort_deck_of_cards
    sort_deck_of_cards([1, 2, 3, 4, 5, 1])

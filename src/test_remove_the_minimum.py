"""Test module for remove_the_minimum."""

import pytest

test_lists = [([1, 2, 3, 4, 5], [2, 3, 4, 5]),
              ([5, 3, 2, 1, 4], [5, 3, 2, 4]),
              ([1, 2, 3, 1, 1], [2, 3, 1, 1]),
              ([], []),
              ([1, 3, 5, 7, 1], [3, 5, 7, 1]),
              ([4, 3, 2, 3, 2], [4, 3, 3, 2]),
              ([1], []),
              ([1, 2], [2])]


@pytest.mark.parametrize('numbers, result', test_lists)
def test_remove_smallest(numbers, result):
    """Test for the remove_smallest function."""
    from remove_the_minimum import remove_smallest
    assert remove_smallest(numbers) == result

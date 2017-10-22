"""Test module for find_outlier.py."""

import pytest

test_list = [([2, 6, 8, 10, 3], 3),
             ([2, 4, 6, 7, 8], 7),
             ([3, 1, 5, 42, 9, 11], 42),
             ([1, 6, 7], 6),
             ([4, 3, 2, 2, 6, 8], 3)]


@pytest.mark.parametrize('with_outlier, removed', test_list)
def test_find_outlier(with_outlier, removed):
    """Test the find outlier function."""
    from find_outlier import find_outlier
    assert find_outlier(with_outlier) == removed

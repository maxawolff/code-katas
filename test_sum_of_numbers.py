"""Test module for sum_of_numbers.py."""

import pytest

sum_values = [
    (0, 1, 1), (0, -1, -1), (1, 3, 6),
    (2, 2, 2), (1, -1, 0), (1, -3, -5)]


@pytest.mark.parametrize('a, b, value', sum_values)
def test_sum(a, b, value):
    """Test of the get_sum function."""
    from sum_of_numbers import get_sum
    assert get_sum(a, b) == value

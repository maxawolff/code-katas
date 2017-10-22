"""Test module for sum_terms.py."""

import pytest

sum_values = [(1, "1.00"), (2, "1.25"), (3, "1.39")]


@pytest.mark.parametrize('n, sum', sum_values)
def test_series_sum(n, sum):
    """Test of the series sum function."""
    from sum_terms import series_sum
    assert series_sum(n) == sum

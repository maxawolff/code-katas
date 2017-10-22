"""Test module for array_diff.py."""

import pytest

arrays = [([1, 2], [1], [2]),
          ([1, 2, 2], [1], [2, 2]),
          ([1, 2, 2], [2], [1]),
          ([1, 2, 2], [], [1, 2, 2]),
          ([], [1, 2], []),
          ([1, 2, 3], [1], [2, 3]),
          ([], [1, 2, 3, 4, 5], []),
          ([1, 2, 3, 4, 5], [], [1, 2, 3, 4, 5]),
          ([1, 2, 3, 4], [2, 4], [1, 3])]


@pytest.mark.parametrize('a, b, diff', arrays)
def test_array_diff(a, b, diff):
    """Test dat function."""
    from array_diff import array_diff
    assert array_diff(a, b) == diff

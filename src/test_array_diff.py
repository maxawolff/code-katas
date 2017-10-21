"""Test module for array_diff.py."""

import pytest

arrays = [([1, 2], [1], [2]),
          ([1, 2, 2], [1], [2, 2]),
          ([1, 2, 2], [2], [1]),
          ([1, 2, 2], [], [1, 2, 2]),
          ([], [1, 2], [])]


@pytest.mark.parametrize('a, b, diff', arrays)
def test_array_diff(a, b, diff):
    """Test dat function."""
    from array_diff import array_diff
    assert array_diff(a, b) == diff

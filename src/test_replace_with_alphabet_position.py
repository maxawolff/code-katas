"""Test module for replace_with_alphabet_position.py."""

import pytest

test_strings = [
    ("The sunset sets at twelve o' clock.", "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"),
    ("The narwhal bacons at midnight.", "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"),
    ("This is a string", "20 8 9 19 9 19 1 19 20 18 9 14 7"),
    ("Not a fun test to write", "14 15 20 1 6 21 14 20 5 19 20 20 15 23 18 9 20 5"),
    ("Boo", "2 15 15"),
    ("", "")]


@pytest.mark.parametrize('text, result', test_strings)
def test_aplhabet_position(text, result):
    """Test of the alphabet_position function."""
    from replace_with_alphabet_position import alphabet_position
    assert alphabet_position(text) == result

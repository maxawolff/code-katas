"""."""

from string_pyramid import watch_pyramid_from_above, watch_pyramid_from_the_side, count_visible_characters_of_the_pyramid, count_all_characters_of_the_pyramid
import pytest


above = [(None, None), ('', ''), ('*#', '***\n*#*\n***')]


@pytest.mark.parametrize('chars, res', above)
def test_from_above(chars, res):
    """Test dat function."""
    assert watch_pyramid_from_above(chars) == res


def test_from_side():
    """."""
    res = watch_pyramid_from_the_side('aaa')
    pass


def test_num_characters_visible():
    """."""
    pass


def test_num_characters_total():
    """."""
    pass

"""."""

from string_pyramid import watch_pyramid_from_above, watch_pyramid_from_the_side, count_visible_characters_of_the_pyramid, count_all_characters_of_the_pyramid
import pytest


above = [(None, None), ('', ''), ('*#', '***\n*#*\n***'),
         ('abc', 'aaaaa\nabbba\nabcba\nabbba\naaaaa'),
         ('aaa', 'aaaaa\naaaaa\naaaaa\naaaaa\naaaaa'),
         ('54321', '555555555\n544444445\n543333345\n543222345\n543212345\n543222345\n543333345\n544444445\n555555555')]


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

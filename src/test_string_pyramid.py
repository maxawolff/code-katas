"""."""

from string_pyramid import watch_pyramid_from_above, watch_pyramid_from_the_side, count_visible_characters_of_the_pyramid, count_all_characters_of_the_pyramid
import pytest


above = [(None, None), ('', ''), ('*#', '***\n*#*\n***'),
         ('abc', 'aaaaa\nabbba\nabcba\nabbba\naaaaa'),
         ('aaa', 'aaaaa\naaaaa\naaaaa\naaaaa\naaaaa'),
         ('54321', '555555555\n544444445\n543333345\n543222345\n543212345\n543222345\n543333345\n544444445\n555555555')]


side = [(None, None), ('', ''), ('*#', ' # \n***'),
        ('abc', '  c  \n bbb \naaaaa'), ('aaa', '  a  \n aaa \naaaaa'),
        ('54321', '    1    \n   222   \n  33333  \n 4444444 \n555555555')]


visible = [(None, -1), ('', -1), ('*#', 9),
           ('abc', 25), ('aaa', 25), ('54321', 81)]


total = [(None, -1), ('', -1), ('*#', 10),
         ('abc', 35), ('aaa', 35), ('54321', 165)]


@pytest.mark.parametrize('chars, res', above)
def test_from_above(chars, res):
    """Test view pyramid from above."""
    assert watch_pyramid_from_above(chars) == res


@pytest.mark.parametrize('chars, res', side)
def test_from_side(chars, res):
    """Test view pyramid from the side."""
    assert watch_pyramid_from_the_side(chars) == res


@pytest.mark.parametrize('chars, res', visible)
def test_visible(chars, res):
    """Test count visible characters."""
    assert count_visible_characters_of_the_pyramid(chars) == res


@pytest.mark.parametrize('chars, res', total)
def test_total(chars, res):
    """Test count all characters."""
    assert count_all_characters_of_the_pyramid(chars) == res

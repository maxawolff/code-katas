"""Test module for your_order_pleas.py."""

import pytest

test_values = [("is2 Thi1s T4est 3a", "Thi1s is2 3a T4est"),
               ("tw2o o1ne", "o1ne tw2o"),
               ("thr3ee 1one two2", "1one two2 thr3ee"),
               ("one1", "one1"),
               ("on1e t2wo the3e", "on1e t2wo the3e")]


@pytest.mark.parametrize('sentence, result', test_values)
def test_order(sentence, result):
    """."""
    from your_order_please import order
    assert order(sentence) == result

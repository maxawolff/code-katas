"""Test file for forbes.py."""
from forbes import billionaires, json_to_dict


def test_forbes_returns_correct_names():
    """Test that the names of the billionares are correct."""
    bill_info = billionaires()
    assert 'Phil Knight' in bill_info['oldest']
    assert 'Mark Zuckerberg' in bill_info['youngest']


def test_forbes_returns_correct_net_worth():
    """Test that the names of the billionares are correct."""
    bill_info = billionaires()
    assert 24400000000 in bill_info['oldest']
    assert 44600000000 in bill_info['youngest']


def test_forbes_returns_correct_industry():
    """Test that the names of the billionares are correct."""
    bill_info = billionaires()
    assert 'Nike' in bill_info['oldest']
    assert 'Facebook' in bill_info['youngest']


def test_json_read_correctly_as_dict():
    """Test that json file is correctly turned into list of dicts."""
    data = json_to_dict('billionaires.json')
    assert isinstance(data, list)
    assert isinstance(data[0], dict)

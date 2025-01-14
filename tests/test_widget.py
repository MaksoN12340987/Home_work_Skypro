import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "vareble, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Ivan Vasilivitch 7000792289606361", "Ivan Vasilivitch 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", ""),
    ],
)
def test_mask_account_card(vareble, expected):
    assert mask_account_card(vareble) == expected

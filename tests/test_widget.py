import pytest

from src.widget import mask_account_card
from src.decorators import log, predicate_is_str


@log(predicate_is_str, "Невозможно продолжить, передайте строку", ".log")
def print_result_to_file(to_mask):
    return mask_account_card(to_mask)


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
    assert print_result_to_file(vareble) == expected

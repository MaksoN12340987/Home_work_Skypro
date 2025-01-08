import pytest


from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card
from src.decorators import log, predicate_not_none, predicate_is_str


def test_get_mask_card_number_is_str():
    with pytest.raises(ValueError, match="Невозможно продолжить, передайте строку"):
        mask_account_card(1)


def test_get_mask_card_number_not_none():
    with pytest.raises(ValueError, match="Невозможно продолжить с типом элемента None"):
        mask_account_card(None)


# @pytest.mark.parametrize(
#     "to_mask, expected", [
#         (
#             "Visa Platinum 7000792289606361",
#             """Function is <function mask_account_card at 0x000001D7101E85E0>
#             Visa Platinum 7000 79** **** 6361 """
#         )
#         (
#             "Счет 73654108430135874305",
#             "Function is <function fulfilment at 0x000002B50C3A9620>\nСчет **4305"
#         ),
#     ])
# def test_proc_mask_account_card(to_mask, expected):
#     assert mask_account_card(to_mask) == expected

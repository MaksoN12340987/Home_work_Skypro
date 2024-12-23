# import pytest

# import src.widget, src.processing


# @pytest.mark.parametrize(
#     "value_number, expected",
#     [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361 "),("Счет 73654108430135874305", "Счет **4305")]
# )
# def test_mask_account_card(value_number, expected):
#     assert src.widget.mask_account_card(value_number) == expected

# def test_mask_account_card(account_number):
#     assert src.widget.mask_account_card(account_number) == "Счет **4305"

# import pytest

# from src.masks import get_mask_account, get_mask_card_number


# # The expected result is positiv
# def test_get_mask_card_number(card_number):
#     assert get_mask_card_number(card_number, 14) == "Visa Platinum 7000 79** **** 6361"


# def test_get_mask_account(account_number):
#     assert get_mask_account(account_number, 5) == "Счет **4305"


# # The expected result is negative
# def test_negative_get_mask_card_number(card_number):
#     with pytest.raises(ValueError):
#         assert get_mask_card_number(card_number, None) == ""


# def test_negative_get_mask_account(account_number):
#     with pytest.raises(ValueError):
#         assert get_mask_account(account_number, None) == ""

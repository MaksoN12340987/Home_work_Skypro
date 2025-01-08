import pytest


from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card
from src.decorators import log


# @pytest.mark.parametrize("message, element, start",
#     ("Невозможно продолжить, передайте строку", 1, 5),
#     ("Невозможно продолжить с типом элемента None", None, 5)
# )
def test_get_mask_card_number_is_str():
    with pytest.raises(ValueError, match="Невозможно продолжить, передайте строку"):
        get_mask_account(1, 5)


def test_get_mask_card_number_not_none():
    with pytest.raises(ValueError, match="Невозможно продолжить с типом элемента None"):
        get_mask_account(None, 5)
import pytest

# from src.masks import get_mask_account, get_mask_card_number
# from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "to_mask, mesage",
    [(1, "Невозможно продолжить, передайте строку"), (None, "Невозможно продолжить, передайте строку")],
)
def test_proc_mask_account_card(to_mask, mesage):
    with pytest.raises(ValueError, match=mesage):
        mask_account_card(to_mask)

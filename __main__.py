from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card
from src.decorators import log, predicate_not_none, predicate_is_str

if __name__ == "__main__":
    mask_account_card("Visa Platinum 7000792289606361")
    mask_account_card("Счет 73654108430135874305")

    print(filter_by_state())
    print(sort_by_date())

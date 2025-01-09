from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))

    print(filter_by_state())
    print(sort_by_date())

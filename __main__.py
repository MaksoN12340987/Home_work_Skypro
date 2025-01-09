from src.decorators import log, predicate_is_str
from src.widget import mask_account_card

if __name__ == "__main__":
    @log(predicate_is_str, "Невозможно продолжить, передайте строку")
    def print_result_to_console(to_mask):
        return mask_account_card(to_mask)


    @log(predicate_is_str, "Невозможно продолжить, передайте строку", ".log")
    def print_result_to_file(to_mask):
        return mask_account_card(to_mask)

    print_result_to_console("Visa Platinum 7000792289606361")
    print_result_to_file("Visa Platinum 7000792289606361")
    print_result_to_console("Счет 73654108430135874305")
    print_result_to_file("Счет 73654108430135874305")

from src.decorators import log, predicate_is_list, predicate_is_str
from src.external_api import conversion_from_usd_eur_in_rub
from src.processing import filter_by_state
from src.widget import mask_account_card

if __name__ == "__main__":

    # Function for outputting the result of work to the console
    @log(predicate_is_str, "Невозможно продолжить, передайте строку")
    def print_result_to_console(to_mask):
        return mask_account_card(to_mask)

    # print result to console
    print_result_to_console("Visa Platinum 7000792289606361")
    print_result_to_console("Счет 73654108430135874305")

    # print result to file widget.log
    mask_account_card("Visa Platinum 7000792289606361")
    mask_account_card("Счет 73654108430135874305")

    @log(predicate_is_list, "Невозможно продолжить, передайте список словарей")
    def print_result_to_console(list, key="EXECUTED"):
        return filter_by_state(list, key)

    bank_operation = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-13T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-13T08:20:00.419441"},
    ]
    print_result_to_console(bank_operation)
    print_result_to_console(bank_operation, "CANCELED")

    print(conversion_from_usd_eur_in_rub(100, "USD", "https://api.apilaye.com/exchangerates_data/convert"))

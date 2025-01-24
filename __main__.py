import logging

from src.decorators import log, predicate_is_list, predicate_is_str
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state
from src.utils import conversion_json_to_object
from src.widget import mask_account_card

logger_main = logging.getLogger("main")
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_main.addHandler(file_handler)
logger_main.setLevel(logging.INFO)


def main() -> None:
    logger_main.info("Get started main")

    # Function for outputting the result of work to the console
    @log(predicate_is_str, "Невозможно продолжить, передайте строку")
    def print_result_to_console(to_mask: str = "") -> str:
        return mask_account_card(to_mask)

    # print result to console
    print_result_to_console("Visa Platinum 7000792289606361")
    print_result_to_console("Счет 73654108430135874305")

    # print result to file widget.log
    mask_account_card("Visa Platinum 7000792289606361")
    mask_account_card("Счет 73654108430135874305")

    @log(predicate_is_list, "Невозможно продолжить, передайте список словарей")
    def result_to_console(list: list = [], key: str = "EXECUTED") -> list:
        return filter_by_state(list, key)

    bank_operation = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-13T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-13T08:20:00.419441"},
    ]
    result_to_console(bank_operation)
    result_to_console(bank_operation, "CANCELED")

    # Демонстрация логирования
    print(get_mask_card_number("", 3))
    print(get_mask_account("", 3))

    print(conversion_json_to_object("data/n.json"))
    print(conversion_json_to_object("data/broken.json"))


if __name__ == "__main__":
    main()

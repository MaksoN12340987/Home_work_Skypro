import logging


logging.basicConfig(level=logging.INFO,
                    format='\n%(asctime)s %(levelname)s %(name)s %(lineno)d: \n%(message)s',
                    datefmt='%H:%M:%S %d-%m-%Y',
                    filename=f"log/{__name__}.log",
                    filemode='w')
file_logger = logging.getLogger(__name__)


# Functional part
def get_mask_card_number(card_number: str = "", start: int = 0) -> str:
    """принимает на вход номер карты, индекс первой цыфры номера карты и возвращает маску номера
    по правилу User Name XXXX XX** **** XXXX"""
    file_logger.info("Get started get_mask_card_number")
    out_format = card_number[:start]
    split = start + 3
    temp = range(start + 6, start + 12)

    for i in range(len(card_number)):
        if i >= start:
            if i in temp:
                out_format += "*"
                if i != len(card_number) - 1:
                    if i == split:
                        out_format += " "
                        split += 4
            else:
                out_format += card_number[i]
                if i != len(card_number) - 1:
                    if i == split:
                        out_format += " "
                        split += 4
    if card_number == "":
        file_logger.warning(f'''Возвращаем пустую строку, на вход получили: "{card_number}"''')
    return out_format


def get_mask_account(bank_account: str = "", start: int = 0) -> str:
    """принимает на вход номер счета и возвращает маску номера по правилу Name **XXXX"""
    file_logger.info("Get started get_mask_account")
    out_format = ""

    out_format += bank_account[:start] + "**" + bank_account[-4:]
    if bank_account == "":
        file_logger.warning(f'''Возвращаем пустую строку, на вход получили: "{bank_account}"''')
    return out_format

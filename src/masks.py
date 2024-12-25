# Functional part
def get_mask_card_number(card_number: str = "", start: int = 0) -> str:
    """принимает на вход номер карты, индекс первой цыфры номера карты и возвращает маску номера
    по правилу User Name XXXX XX** **** XXXX"""
    if start == None:
        raise ValueError("Невозможно найти элемент None")
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
    return out_format


def get_mask_account(bank_account: str = "", start: int = 0) -> str:
    """принимает на вход номер счета и возвращает маску номера по правилу Name **XXXX"""
    if start == None:
        raise ValueError("Невозможно найти элемент None")
    out_format = ""

    out_format += bank_account[:start] + "**" + bank_account[-4:]

    return out_format

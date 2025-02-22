# from src.decorators import log, predicate_is_str
from src.masks import get_mask_account, get_mask_card_number


# @log(predicate_is_str, "Невозможно продолжить, передайте строку", "log/widget.log")
def mask_account_card(to_mask: str = "") -> str:
    """Принимает строку с именем держателя и номером карты или номер счёта
    и возвращает Имя держателя и замаскированный номер карты или номер счёта"""
    index = 0
    temp = ""
    try:
        for i in range(len(to_mask)):
            if to_mask[i] == " ":
                if temp.isalpha():
                    temp = ""
                    i += 1
                    index = i
            temp += to_mask[i]

        if to_mask[:index] == "Счет ":
            return get_mask_account(to_mask, index)
        else:
            return get_mask_card_number(to_mask, index)
    except Exception:
        return to_mask

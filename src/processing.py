# from src.decorators import log, predicate_is_list


# Bank transactions sorting function
# @log(predicate_is_list, "Невозможно продолжить, передайте строку", "log/processing.log")
def filter_by_state(
    to_sort: list = [], state_key: str = "EXECUTED", key: str = "state", type_json: bool = False
) -> list:
    """Принимает список словарей и ключ: state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий словари соответствующих ключу"""
    finally_list = []
    if state_key == "":
        state_key = "EXECUTED"
    elif state_key == None:
        raise ValueError("Невозможно отсортировать список по пустому ключу")
    if type_json:
        for i in range(len(to_sort)):
            if to_sort[i].get("operationAmount", {}).get("currency", {}).get(key, "") == state_key:
                finally_list.append(to_sort[i])
    else:
        for i in range(len(to_sort)):
            if to_sort[i].get(key, "") == state_key:
                finally_list.append(to_sort[i])

    return finally_list


# Sort list by date
# @log(predicate_is_list, "Невозможно продолжить, передайте строку", "log/processing.log")
def sort_by_date(operation_list: list = [], date: bool = True) -> list:
    """Принимает список словарей и параметр сортировки (по умолчанию "True" — убывание).
    Функция возвращает новый список, отсортированный по дате (date)"""
    operation_list.sort(key=lambda operation_list: operation_list["date"][: 9 + 11 :], reverse=date)
    return operation_list

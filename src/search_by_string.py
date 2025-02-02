import re


def search_in_list_by_string(bank_operations: list[dict] = [], search_string: str = "") -> list:
    result = []
    for i in range(len(bank_operations)):
        if re.findall(search_string, bank_operations[i].get("description", ""), flags=re.IGNORECASE):
            result.append(bank_operations[i])
    return result

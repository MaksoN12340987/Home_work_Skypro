def filter_by_currency(list_operations: list = [], currency: str = ""):
    for i in range(len(list_operations)):
        if list_operations[i].get("operationAmount").get("currency").get("code") == currency:
            yield list_operations[i]


def transaction_descriptions(list_operation: list = []):
    i = 0
    while list_operation:
        yield list_operation[i].get("description")
        i += 1


def card_number_generator(start: int = 0, stop: int = 0):
    sample = "0000000000000000"
    while start <= stop:
        sample = sample[: 16 - len(str(start))] + str(start)
        yield sample[:4] + " " + sample[4:8] + " " + sample[9:13] + " " + sample[12:]
        start += 1

def filter_by_currency(list_operations: list = [], currency: str = ""):
    for i in range(len(list_operations)):
        if list_operations[i].get("operationAmount").get("currency").get("code") == currency:
            print(i)
            yield list_operations[i]
            if i == len(list_operations):
                break
            

def transaction_descriptions():
    pass


def card_number_generator(start: int = 0, stop: int = 0):
    sample = "0000000000000000"
    end = stop - start
    count = 0
    while start <= stop:
        sample = sample[:16 - len(str(start))] + str(start)
        yield sample[:4] + " " + sample[4:8] + " " + sample[9:13] + " " + sample[12:]
        start += 1
        if count > end:
            break

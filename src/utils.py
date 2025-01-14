import json

from external_api import conversion_from_usd_eur_in_rub


def convert_json_to_object(file_name="") -> list:
    try:
        with open(file_name, "r") as f:
            data_bank_operation = json.load(f)
    except FileNotFoundError:
        data_bank_operation = []
    except Exception:
        data_bank_operation = []
    return data_bank_operation


def transaction_amount(dict_transaction:dict = {}) -> float:
    currency = dict_transaction.get("operationAmount").get("currency").get("code")
    transaction_amount = dict_transaction.get("operationAmount").get("amount")
    
    if currency != "RUB":
        return conversion_from_usd_eur_in_rub(transaction_amount, currency)
    else:
        return transaction_amount

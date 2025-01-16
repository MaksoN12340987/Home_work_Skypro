import json

from src.external_api import conversion_from_usd_eur_in_rub


def conversion_json_to_object(file_name="") -> list:
    """Принимает на вход путь до файла .json, который читает и
    возвращает список"""
    try:
        with open(file_name, "r") as f:
            data_bank_operation = json.load(f)
    except FileNotFoundError:
        data_bank_operation = []
    except Exception:
        data_bank_operation = []
    return data_bank_operation


def transaction_amount(dict_transaction: dict = {}) -> float:
    """Принимает на вход словарь транзакции, определяет тип валюты и
    возвращает сумму транзакции"""
    currency = dict_transaction.get("operationAmount", {}).get("currency", {}).get("code", None)
    transaction_amount = dict_transaction.get("operationAmount", {}).get("amount", None)

    if currency != "RUB":
        return conversion_from_usd_eur_in_rub(transaction_amount, currency)
    else:
        return float(transaction_amount)

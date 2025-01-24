import json
import logging

from src.external_api import conversion_from_usd_eur_in_rub


logger_utils = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)
logger_utils.setLevel(logging.INFO)


def conversion_json_to_object(file_name="") -> list:
    """Принимает на вход путь до файла .json, который читает и
    возвращает список"""
    logger_utils.info("Get started conversion_json_to_object")
    try:
        with open(file_name, "r") as f:
            data_bank_operation = json.load(f)

    except FileNotFoundError:
        logger_utils.warning("File not found, return []")
        data_bank_operation = []

    except Exception:
        logger_utils.warning("Exceptional error, return []")
        data_bank_operation = []

    return data_bank_operation


def transaction_amount(dict_transaction: dict = {}) -> float:
    """Принимает на вход словарь транзакции, определяет тип валюты и
    возвращает сумму транзакции"""
    logger_utils.info("Get started transaction_amount")
    currency = dict_transaction.get("operationAmount", {}).get("currency", {}).get("code", None)
    transaction_amount = dict_transaction.get("operationAmount", {}).get("amount", None)

    if currency != "RUB":
        return conversion_from_usd_eur_in_rub(transaction_amount, currency)
    else:
        logger_utils.info("And the currency is already RUB")
        return float(transaction_amount)

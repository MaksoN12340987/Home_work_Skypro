import json
import logging

from src.external_api import conversion_from_usd_eur_in_rub


logging.basicConfig(level=logging.INFO,
                    format='\n%(asctime)s %(levelname)s %(name)s %(lineno)d: \n%(message)s',
                    datefmt='%H:%M:%S %d-%m-%Y',
                    filename=f"log/{__name__}.log",
                    filemode='w')
file_logger = logging.getLogger(__name__)


def conversion_json_to_object(file_name="") -> list:
    """Принимает на вход путь до файла .json, который читает и
    возвращает список"""
    file_logger.info("Get started conversion_json_to_object")
    try:
        with open(file_name, "r") as f:
            data_bank_operation = json.load(f)
    except FileNotFoundError:
        file_logger.warning("File not found, return []")
        data_bank_operation = []
    except Exception:
        file_logger.warning("Exceptional error, return []")
        data_bank_operation = []
    return data_bank_operation


def transaction_amount(dict_transaction: dict = {}) -> float:
    """Принимает на вход словарь транзакции, определяет тип валюты и
    возвращает сумму транзакции"""
    file_logger.info("Get started transaction_amount")
    currency = dict_transaction.get("operationAmount", {}).get("currency", {}).get("code", None)
    transaction_amount = dict_transaction.get("operationAmount", {}).get("amount", None)

    if currency != "RUB":
        return conversion_from_usd_eur_in_rub(transaction_amount, currency)
    else:
        return float(transaction_amount)

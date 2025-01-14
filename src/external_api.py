import json
import os

import requests
from dotenv import load_dotenv


def conversion_from_usd_eur_in_rub(
    transaction_sum=0,
    currency: str = "",
    url="https://api.apilayer.com/exchangerates_data/convert",
    filename: str = ".log/external_api.log",
) -> float:
    """Принимает на вход сумму в валюте и наименование валюты "RUB" или "USD"
    Возвращает число типа "float" - валюта, конвертированная в рубли
    Также имеет 2 дополнительных параметра:
    - url ссылка на апи
    - filename путь к файлу для записи лога ошибок"""
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if currency == "USD":
        payload = {"to": "RUB", "from": "USD", "amount": str(transaction_sum)}
    elif currency == "EUR":
        payload = {"to": "RUB", "from": "EUR", "amount": str(transaction_sum)}
    else:
        raise ValueError('''Укажите валюту в нужном формате "USD" или "EUR"''')

    headers = {"apikey": api_key}

    try:
        temp = requests.get(url, headers=headers, params=payload)
        result = json.loads(temp.text).get("result")
    except requests.exceptions.ConnectionError:
        print("Connection Error. Please check your network connection.")
    except Exception:
        print("Error, invalid data or not correct url")

    if result == None:
        with open(filename, "a") as file:
            file.write(f"ERROR:\n{temp.text}\n")
        raise ValueError("Error, invalid data or not correct url")

    return result

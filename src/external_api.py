import json
import os

import requests
from dotenv import load_dotenv


def conversion_from_usd_eur_in_rub(
    transaction_sum=0, currency="", url="https://api.apilayer.com/exchangerates_data/convert"
) -> float:
    """Принимает на вход сумму в валюте и наименование валюты "RUB" или "USD"
    Возвращает число типа "float" - валюта, конвертированная в рубли
    Также имеет 1 доп параметр:
    - url ссылка на апи"""
    result = None

    if currency == "USD":
        payload = {"to": "RUB", "from": "USD", "amount": str(transaction_sum)}
    elif currency == "EUR":
        payload = {"to": "RUB", "from": "EUR", "amount": str(transaction_sum)}
    else:
        raise ValueError('''Укажите валюту в нужном формате "USD" или "EUR"''')

    try:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        headers = {"apikey": api_key}
        temp = requests.get(url, headers=headers, params=payload)
        result = json.loads(temp.text).get("result")
    except Exception:
        raise ValueError("Error, invalid data or not correct url")
    if not result:
        raise ValueError("Error, invalid data or not correct url")
    return result

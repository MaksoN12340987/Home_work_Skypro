import os

import json
import requests
from dotenv import load_dotenv



def conversion_from_usd_eur_in_rub(transaction_sum = 0, currency:str = "") -> float:
    load_dotenv()
    api_key = os.getenv('API_KEY')
    url = "https://api.apilayer.com/exchangerates_data/convert"

    if currency == "USD":
        payload = {
            "to": "RUB",
            "from": "USD",
            "amount": str(transaction_sum)
        }
    elif currency == "EUR":
        payload = {
            "to": "RUB",
            "from": "EUR",
            "amount ": str(transaction_sum)
        }
    else:
        raise ValueError('''Укажите валюту в нужном формате "USD" или "EUR"''')
    
    headers= {
        "apikey": api_key
    }
    
    try:
        temp = requests.get(url, headers=headers, params=payload, timeout=5)
        result = json.loads(temp.text).get("result")
    except requests.exceptions.Timeout:
        print("Request timed out. Please check your internet connection.")
    except requests.exceptions.RequestException:
        print("An error occurred. Please try again later.")
    
    return result

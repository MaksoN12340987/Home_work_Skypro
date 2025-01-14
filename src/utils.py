import json


def convert_json_to_object(file_name=""):
    try:
        with open(file_name, "r") as f:
            data_bank_operation = json.load(f)
    except FileNotFoundError:
        data_bank_operation = []
    except Exception:
        data_bank_operation = []
    return data_bank_operation


def conversion_from_usd_eur_in_rub():
    pass

import pytest
from unittest.mock import patch

from src.utils import conversion_json_to_object, transaction_amount


def test_conversion_json_to_object_ok(operations_json):
    assert conversion_json_to_object("data/operations.json") == operations_json


@pytest.mark.parametrize("file_path, expected", [("", []), ("data/broken.json", [])])
def test_conversion_json_to_object(file_path, expected):
    assert conversion_json_to_object(file_path) == expected


@pytest.mark.parametrize("file_path, expected", [({}, 0.00)])
def test_transaction_amount(file_path, expected):
    assert transaction_amount(file_path) == expected


@patch("requests.get")
def test_transaction_amount_euro(mock_api, return_api):
    mock_api.return_value.json.return_value = return_api
    assert (
        str(
            type(
                transaction_amount(
                    {
                        "id": 1991514.0,
                        "state": "EXECUTED",
                        "date": "2020-01-27T04:12:56Z",
                        "amount": 21762.0,
                        "currency_name": "Euro",
                        "currency_code": "EUR",
                        "from": "Счет 09809186102982283517",
                        "to": "Счет 97244687605159972750",
                        "description": "Перевод со счета на счет",
                    }
                )
            )
        )
        == "<class 'float'>"
    )


def test_transaction_amount_rub():
    assert str(type(transaction_amount({
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        }))) == "<class 'float'>"

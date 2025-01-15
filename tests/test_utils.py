from unittest.mock import patch, Mock

import pytest
import requests

from src.utils import conversion_json_to_object, transaction_amount


def test_conversion_json_to_object_path(operations_json):
    assert conversion_json_to_object("data/operations.json") == operations_json


@pytest.mark.parametrize(
    "key, expected",
    [
        ("", []),
        (None, []),
        (12456, []),
    ],
)
def test_conversion_json_to_object(log_operations, key, expected):
    assert conversion_json_to_object(key) == expected


@pytest.mark.parametrize(
    "dict_transaction, expected",
    [
        (
            {
                "id": 154927927,
                "state": "EXECUTED",
                "date": "2019-11-19T09:22:25.899614",
                "operationAmount": {"amount": "30153.72", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 7810846596785568",
                "to": "Счет 43241152692663622869",
            },
            "<class 'float'>",
        ),
        (
            {
                "id": 619287771,
                "state": "EXECUTED",
                "date": "2019-08-19T16:30:41.967497",
                "operationAmount": {"amount": "81150", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Счет 17691325653939384901",
                "to": "Счет 49304996510329747621",
            },
            "<class 'float'>",
        ),
    ],
)
def test_transaction_amount(dict_transaction, expected):
    assert str(type(transaction_amount(dict_transaction))) == expected


@patch("requests.get")
def test_transaction_amount_usd(mock_api, return_api, operations_json):
    mock_api.return_value.json.return_value = return_api
    assert str(type(transaction_amount(operations_json[2]))) == "<class 'float'>"
    mock_api.assert_called()

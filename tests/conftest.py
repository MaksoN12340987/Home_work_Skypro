import pytest

import __main__.py

@pytest.fixture()
def card_number():
    return "Visa Platinum 7000792289606361"

@pytest.fixture()
def account_number():
    return "Счет 73654108430135874305"

@pytest.fixture()
def list_data_bank_operation():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-13T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-13T08:20:00.419441"}
    ]

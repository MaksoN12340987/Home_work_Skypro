import pytest

from src.utils import conversion_json_to_object, transaction_amount


def test_conversion_json_to_object_ok(operations_json):
    assert conversion_json_to_object("data/operations.json") == operations_json


@pytest.mark.parametrize("file_path, expected", [("", []), ("data/broken.json", [])])
def test_conversion_json_to_object(file_path, expected):
    assert conversion_json_to_object(file_path) == expected


@pytest.mark.parametrize("file_path, expected", [({}, 0.00)])
def test_transaction_amount(file_path, expected):
    assert transaction_amount(file_path) == expected

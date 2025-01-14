import pytest

from src.utils import conversion_from_usd_eur_in_rub, convert_json_to_object


def test_convert_json_to_object(operations_json):
    assert convert_json_to_object("data/operations.json") == operations_json


@pytest.mark.parametrize(
    "key, expected",
    [
        ("", []),
        (None, []),
        (12456, []),
    ],
)
def test_convert_json_to_object(log_operations, key, expected):
    assert convert_json_to_object(key) == expected

import pytest

from src.file_interpretation import conversion_csv_to_object, conversion_xlsx_to_object


def test_conversion_csv_to_object_path():
    assert conversion_csv_to_object("data/transactions.csv").shape == (1000, 1)


@pytest.mark.parametrize(
    "key, expected",
    [
        ("", ""),
        (None, ""),
        (12456, ""),
    ],
)
def test_conversion_csv_to_object_no_valid(key, expected):
    assert conversion_csv_to_object(key) == expected


def test_conversion_xlsx_to_object_path():
    assert conversion_xlsx_to_object("data/transactions_excel.xlsx").shape == (1000, 9)


@pytest.mark.parametrize(
    "key, expected",
    [
        ("", ""),
        (None, ""),
        (12456, ""),
    ],
)
def test_conversion_xlsx_to_object_no_valid(key, expected):
    assert conversion_xlsx_to_object(key) == expected

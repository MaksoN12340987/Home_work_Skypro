import pytest

from src.external_api import conversion_from_usd_eur_in_rub


@pytest.mark.parametrize(
    "sum, key, expected",
    [(100, "USD", "<class 'float'>"), (100, "EUR", "<class 'float'>"), ("100", "EUR", "<class 'float'>")],
)
def test_convert_json_to_object(sum, key, expected):
    assert str(type(conversion_from_usd_eur_in_rub(sum, key))) == expected


# The expected result is negative
@pytest.mark.parametrize(
    "sum, key, expected", [(10, None, "Invalid data."), (10, 121321424, "Invalid data."), (10, [], "Invalid data.")]
)
def test_convert_json_to_object_valueError(sum, key, expected):
    with pytest.raises(ValueError):
        assert conversion_from_usd_eur_in_rub(sum, key) == expected


@pytest.mark.parametrize(
    "transaction_sum, currency, url, mesage",
    [
        (
            1,
            "EUR",
            "https://api.apilaye.com/exchangerates_data/convert",
            "Connection Error. Please check your network connection.\n",
        ),
        (
            "Help",
            "EUR",
            "https://api.apilayer.com/exchangerates_data/convert",
            "Error, invalid data or not correct url\n",
        ),
    ],
)
def test_conversion_from_usd_eur_in_rub_err(transaction_sum, currency, url, mesage, capsys):
    conversion_from_usd_eur_in_rub(transaction_sum, currency, url)
    captured = capsys.readouterr()
    assert captured.out == mesage


@pytest.mark.parametrize(
    "transaction_sum, currency, url, mesage",
    [("Help", "EUR", "https://api.apilayer.com/exchangerates_data/convert", "Error, invalid data or not correct url")],
)
def test_conversion_from_usd_eur_in_rub_err_invalid(transaction_sum, currency, url, mesage):
    with pytest.raises(ValueError, match=mesage):
        conversion_from_usd_eur_in_rub(transaction_sum, currency, url)

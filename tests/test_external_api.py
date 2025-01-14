import pytest

from src.external_api import conversion_from_usd_eur_in_rub


@pytest.mark.parametrize(
    "sum, key, expected",
    [(100, "USD", "<class 'float'>"), (100, "EUR", "<class 'float'>"), ("100", "EUR", "<class 'float'>")],
)
def test_conversion_from_usd_eur_in_rub(sum, key, expected):
    assert str(type(conversion_from_usd_eur_in_rub(sum, key))) == expected


# The expected result is negative
@pytest.mark.parametrize(
    "sum, key, expected", [(10, None, "Invalid data."), (10, 121321424, "Invalid data."), (10, [], "Invalid data.")]
)
def test_conversion_from_usd_eur_in_rub_valueError(sum, key, expected):
    with pytest.raises(ValueError):
        assert conversion_from_usd_eur_in_rub(sum, key) == expected


@pytest.mark.parametrize(
    "transaction_sum, currency, url, mesage",
    [
        (10, "RUB", "https://api.apilayer.com/exchangerates_data/convert", '''Укажите валюту в нужном формате "USD" или "EUR"'''),
        ("A", "EUR", "https://api.apilayer.com/exchangerates_data/convert", "Error, invalid data or not correct url")
    ]
)
def test_conversion_from_usd_eur_in_rub_err_invalid(transaction_sum, currency, url, mesage):
    with pytest.raises(ValueError, match=mesage):
        conversion_from_usd_eur_in_rub(transaction_sum, currency, url)

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# filter_by_currency
def test_filter_by_currency_usd(log_operations, result_log_operations_usd):
    usd_transactions = filter_by_currency(log_operations, "USD")

    for i in range(3):
        assert next(usd_transactions) == result_log_operations_usd[i]


def test_filter_by_currency_rub(log_operations, result_log_operations_rub):
    usd_transactions = filter_by_currency(log_operations, "RUB")

    for i in range(2):
        assert next(usd_transactions) == result_log_operations_rub[i]


# transaction_descriptions
def test_transaction_descriptions(log_operations, result_discription):
    discription = transaction_descriptions(log_operations)

    for i in range(5):
        assert next(discription) == result_discription[i]


# card_number_generator
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 4, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]),
        (
            99999997,
            100000000,
            ["0000 0000 9999 9997", "0000 0000 9999 9998", "0000 0000 9999 9999", "0000 0001 0000 0000"],
        ),
    ],
)
def test_generator_card_number(start, stop, expected):
    card_number = card_number_generator(start, stop)

    for i in range(4):
        assert next(card_number) == expected[i]


# NEGATIVE test
def test_negative_filter_by_currency_usd(log_operations, result_log_operations_usd):
    with pytest.raises(Exception):
        usd_transactions = filter_by_currency(log_operations, "USD")
        for i in range(5):
            assert next(usd_transactions) == result_log_operations_usd[i]


def test_negative_transaction_descriptions(log_operations, result_discription):
    with pytest.raises(Exception):
        discription = transaction_descriptions(log_operations)
        for i in range(7):
            assert next(discription) == result_discription[i]


def test_negative_generator_card_number_1_4(result_generator_card_number_1_4):
    with pytest.raises(Exception):
        card_number = card_number_generator(1, 4)
        for i in range(6):
            assert next(card_number) == result_generator_card_number_1_4[i]

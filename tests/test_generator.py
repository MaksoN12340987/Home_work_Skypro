import pytest


from src.generators import filter_by_currency, transaction_descriptions, card_number_generator



def test_filter_by_currency_usd(log_operations, result_log_operations_usd):
    usd_transactions = filter_by_currency(log_operations, "USD")
    for i in range(3):
        assert next(usd_transactions) == result_log_operations_usd[i]


def test_filter_by_currency_rub(log_operations, result_log_operations_rub):
    usd_transactions = filter_by_currency(log_operations, "RUB")
    for i in range(2):
        assert next(usd_transactions) == result_log_operations_rub[i]


def test_generator_card_number(result_generator_card_number):
    card_number = card_number_generator(1, 4)
    for i in range(4):
        assert next(card_number) == result_generator_card_number[i]
    
    
import pytest

from src.processing import filter_by_state, sort_by_date

@pytest.mark.parametrize("key, expected",[
    ("EXECUTED", [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ("CANCELED", [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
])
def test_proc_filter_by_state(input_filter_by_state, key, expected):
    assert filter_by_state(input_filter_by_state, key) == expected


def test_proc_sort_by_date_true(list_data_bank_operation, output_list_data_bank_operation_true):
    assert sort_by_date(list_data_bank_operation, True) == output_list_data_bank_operation_true

def test_proc_sort_by_date_false(list_data_bank_operation, output_list_data_bank_operation_false):
    assert sort_by_date(list_data_bank_operation, False) == output_list_data_bank_operation_false

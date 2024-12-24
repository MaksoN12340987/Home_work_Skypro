import pytest

from src.processing import filter_by_state, sort_by_date

@pytest.mark.parametrize("key",[
    ("EXECUTED")
])
def test_proc_filter_by_state(input_filter_by_state, key, output_filter_by_state_EXECUTED):
    assert filter_by_state(input_filter_by_state, key) == output_filter_by_state_EXECUTED


@pytest.mark.parametrize("reverse",[
    (False)
])
def test_proc_sort_by_date(list_data_bank_operation, reverse, output_list_data_bank_operation):
    assert sort_by_date(list_data_bank_operation, reverse) == output_list_data_bank_operation

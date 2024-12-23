import pytest

from src.processing import filter_by_state, sort_by_date

@pytest.mark.parametrize("key",[
    (""),
    ("EXECUTED")
    ])
def proc_filter_by_state():
    assert filter_by_state(input_filter_by_state, key) == output_filter_by_state_EXECUTED
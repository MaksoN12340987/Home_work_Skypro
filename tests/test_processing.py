import pytest

from src.processing import filter_by_state, sort_by_date


# The expected result is positiv
@pytest.mark.parametrize(
    "key, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            "",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_proc_filter_by_state(input_list_to_filter, key, expected):
    assert filter_by_state(input_list_to_filter, key) == expected


def test_sort_by_date_true(bank_operation: list = [], output_data_bank_operation_true: list = []):
    assert sort_by_date(bank_operation, True) == output_data_bank_operation_true


def test_sort_by_date_false(list_data_bank_operation: list = [], output_list_data_bank_operation_false: list = []):
    assert sort_by_date(list_data_bank_operation, False) == output_list_data_bank_operation_false


# The expected result is negative
def test_filter_by_state(input_list_to_filter):
    with pytest.raises(ValueError):
        assert filter_by_state(input_list_to_filter, None) == [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]

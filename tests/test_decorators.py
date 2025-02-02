import pytest

from src.decorators import log, predicate_is_str
from src.widget import mask_account_card


@log(predicate_is_str, "Невозможно продолжить, передайте строку")
def print_result_to_console(to_mask):
    return mask_account_card(to_mask)


@pytest.mark.parametrize(
    "to_mask, mesage",
    [
        (
            "Visa Platinum 7000792289606361",
            "Start function print_result_to_console\nVisa Platinum 7000 79** **** 6361\nThe function has completed\n",
        ),
        (
            "Счет 73654108430135874305",
            "Start function print_result_to_console\nСчет **4305\nThe function has completed\n",
        ),
    ],
)
def test_print_result_to_console(to_mask, mesage, capsys):
    print_result_to_console(to_mask)
    captured = capsys.readouterr()
    assert captured.out == mesage


# @pytest.mark.parametrize(
#     "to_mask, mesage",
#     [(1, "Невозможно продолжить, передайте строку"), (None, "Невозможно продолжить, передайте строку")],
# )
# def test_proc_mask_account_card(to_mask, mesage):
#     with pytest.raises(ValueError, match=mesage):
#         mask_account_card(to_mask)

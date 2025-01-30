from src.search_by_string import search_in_list_by_string
from src.file_interpretation import conversion_csv_to_object
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card


def executive_function_output_main(
    function_choice=conversion_csv_to_object,
    file_path: str = "",
    user_key: str = "",
    user_choice_sort: bool = False,
    user_choice_sort_date: bool = False,
    user_choice_rub: str = "",
    user_choice_name_discription: str = "",
) -> str:
    """_summary_

    Args:
        function_choice (_type_): _description_
        file_path (_type_): _description_
        user_key (_type_): _description_
        user_choice_sort (_type_): _description_
        user_choice_sort_date (_type_): _description_
        user_choice_rub (_type_): _description_
        user_choice_name_discription (_type_): _description_

    Returns:
        _type_: _description_
    """
    intermediate_result = filter_by_state(function_choice(file_path), user_key)

    if user_choice_sort:
        intermediate_result = sort_by_date(intermediate_result, user_choice_sort_date)

    if user_choice_rub:
        if file_path == "data/operations.json":
            intermediate_result = filter_by_state(intermediate_result, user_choice_rub, "code", True)
        else:
            intermediate_result = filter_by_state(intermediate_result, user_choice_rub, "currency_code")

    if user_choice_name_discription == "да":
        search_query = input("Введите слово, по которому выполнить поиск: ")
        intermediate_result = search_in_list_by_string(intermediate_result, search_query)

    # Conclusion of the result
    result = ""
    for i in range(len(intermediate_result)):

        result += f"\n{intermediate_result[i].get("date", "")[:10]} ".replace("-", ".")
        result += f"{intermediate_result[i].get("description", "")}"
        result += f"\n{mask_account_card(intermediate_result[i].get("from", ""))} -> "
        result += f"{mask_account_card(intermediate_result[i].get("to", ""))}"
        if file_path != "data/operations.json":
            result += f"\nСумма: {intermediate_result[i].get("amount", "")} "
            result += f"{intermediate_result[i].get("currency_code", "")}\n"
        else:
            result += (
                f"\nСумма: {intermediate_result[i].get("operationAmount", {}).get("amount", "")} "
                + f"{intermediate_result[i].get("operationAmount", {}).get("currency", {}).get("code", "")}\n"
            )

    return result

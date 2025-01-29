from src.search_by_string import search_in_list_by_string
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card


def executive_function_output_main(
    function_choice,
    file_path,
    user_key,
    user_choice_sort,
    user_choice_sort_date,
    user_choice_rub,
    user_choice_name_discription,
):
    """_summary_

    Args:
        function_choice (_type_): _description_
        file_path (_type_): _description_
        user_key (_type_): _description_
        user_choice_date (_type_): _description_
        user_choice_sort (_type_): _description_
        user_choice_rub (_type_): _description_
        user_choice_name_discription (_type_): _description_

    Returns:
        _type_: _description_
    """
    intermediate_result = filter_by_state(function_choice(file_path), user_key)

    if user_choice_sort:
        intermediate_result = sort_by_date(intermediate_result, user_choice_sort_date)

    if user_choice_rub:
        intermediate_result = filter_by_state(intermediate_result, user_choice_rub, "currency_code")

    if user_choice_name_discription == "да":
        search_query = input("Введите слово, по которому выполнить поиск: ")
        intermediate_result = search_in_list_by_string(intermediate_result, search_query)

    # Conclusion of the result
    result = ""
    for i in range(len(intermediate_result)):

        result += f"\n{intermediate_result[i].get("date", "")[:10]} ".replace("-", ".")
        result += f"{intermediate_result[i].get("description", "")}"
        result += f"\n{mask_account_card(intermediate_result[i].get("from", ""))} -> {mask_account_card(intermediate_result[i].get("to", ""))}"
        result += (
            f"\nСумма: {intermediate_result[i].get("amount", "")} {intermediate_result[i].get("currency_code", "")}\n"
        )

    return result

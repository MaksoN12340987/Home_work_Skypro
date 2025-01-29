from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card


def executive_function_output_main(
    function_choice,
    file_path,
    user_key,
    user_choice_date,
    user_choice_sort,
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
    if user_choice_date != "да" and user_choice_date != "нет":
        user_choice_date = "нет"
    elif user_choice_sort == "да":
        if user_choice_sort == "по возрастанию":
            user_choice_sort = False
        else:
            user_choice_sort = True

    if user_choice_rub != "по возрастанию" and user_choice_rub != "по убыванию":
        user_choice_rub = True

    if user_choice_sort != "по возрастанию" and user_choice_sort != "по убыванию":
        user_choice_sort = True

    if user_choice_name_discription == "да":
        search_query = input("Введите слово, по которому выполнить поиск: ")
        intermediate_result = sort_by_date(filter_by_state(function_choice(file_path), user_key), user_choice_sort)
    else:
        return sort_by_date(filter_by_state(function_choice(file_path), user_key), user_choice_sort)

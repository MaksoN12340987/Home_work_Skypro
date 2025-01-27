import logging

from src.executive import executive_function_output_main
from src.utils import conversion_json_to_object
from src.file_interpretation import conversion_csv_to_object, conversion_xlsx_to_object

logger_main = logging.getLogger("main")
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_main.addHandler(file_handler)
logger_main.setLevel(logging.INFO)


def main() -> None:
    logger_main.info("Get started main")

    user_choice = (
        input(
            "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
            + """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла

    Ваш выбор: """
        )
        .lower()
        .replace(".", "")
    )
    if user_choice == "1":
        function_choice = conversion_json_to_object
        file_path = "data/operations.json"
    elif user_choice == "2":
        function_choice = conversion_csv_to_object
        file_path = "data/transactions.csv"
    elif user_choice == "3":
        function_choice = conversion_xlsx_to_object
        file_path = "data/transactions_excel.xlsx"
    else:
        print("Хм, кажется такого варианта у меня пока нет(")

    if function_choice:
        triger = True
        while triger:
            user_key = input(
                "По какому статусу необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
                + "\nВведите статус: "
            ).upper()
            if user_key == "EXECUTED" or user_key == "CANCELED" or user_key == "PENDING":
                triger = False

        if not triger:
            user_choice_date = input("Отсортировать операции по дате? Да/Нет\n").lower()
            user_choice_sort = input("Отсортировать по возрастанию или по убыванию?\n").lower()
            user_choice_rub = input("Выводить только рублевые тразакции? Да/Нет?\n").lower()
            user_choice_name_discription = input(
                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
            ).lower()

            print(
                executive_function_output_main(
                    function_choice,
                    file_path,
                    user_key,
                    user_choice_date,
                    user_choice_sort,
                    user_choice_rub,
                    user_choice_name_discription,
                )
            )


# .to_dict("records")

if __name__ == "__main__":
    main()

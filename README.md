# Проект домашней работы по реализации фукционала работы с банковскими данными


## Запуск проекта
Запустите следующую команду в терминале, находясь в корневой дирректории проекта, чтобы увидеть результат работы некоторых функций:
```
python .\__main__.py
```

### Требование для запуска:
- python - v3.12
- python-dotenv - v1.0.1
- requests - v2.32.3
- logging - v0.4.9.6


## Пакет src:
В модуле widget.py создана функция mask_account_card, которая принимает строку с именем держателя и номером карты или номер счёта и возвращает Имя держателя и замаскированный номер карты или номер счёта
Формат передачи:
*"Visa Platinum 7000792289606361"*
"Счет 73654108430135874305"

*Формат вывода:*
"Visa Platinum 7000 79** **** 6361"
"Счет **4305"

### Модуль src\utils.py 
Умеет конвертировать в объект Пайтон данные из файла по переданному пути в функцию:
- conversion_json_to_object

Также у этого модуля имеется функция ```transaction_amount```, которая принимает на вход словарь транзакции, определяет тип валюты и возвращает сумму транзакциию
Функция ```transaction_amount``` связана с модулем __Home_work_Skypro\src\external_api.py__, с функцией :
- conversion_from_usd_eur_in_rub\
Которая умеет:
- [X] gринимать на вход сумму в валюте 
- [X] наименование валюты "RUB" или "USD"
- [X] возвращать число типа "float" - валюта, конвертированная в рубли
- [X] также имеет 1 доп параметр:- url ссылка на апи

### Новый функционал сортировки

В пакете src появилась функця filter_by_state, которая принимает список словарей и опционально значение для ключа **state** (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ **state**
 соответствует указанному значению.


## Итеративный вывод

В пакет src добавлен модкль generators, в нем реализованны вункции:
- filter_by_currency принимает на вход список словарей, представляющих транзакции, а возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)
- transaction_descriptions принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
- card_number_generator, который выдает номера банковских карт в формате "XXXX XXXX XXXX XXXX", где X — цифра номера карты.


## Добавлено логирование модулей

По умолчанию, в файл .log выводятся информация о выполнении функции, а при возникновании ошибок, информация об ошибке и входные данные

Установка вровня логирования производится в каждом модуле, установив параметр:
```
.setLevel(logging.INFO)
```


## Тестирование 
В пакете test появились модули тестирования, каждый модуль, согласно названию, тестирует модули программы из пакета src

Для запуска тестирование требуется:
- библиотека pytest pytest = "^8.3.4"
- библиотека pytest-cov = "^6.0.0"

В корневом каталоге присутствует дирректория htmlcov, в которой располагается модуль index.html - в нем отражена статистика по тестированию проекта. А также появился модуль test\generators.py, он тестирует модуль src\generators.py
Ввведите:
```
pytest --cov
```
в виртуальном окружении корневого каталога программы, чтобы увидеть колличество тестов, статусы прохождения тестов и покрытие.

******************************************************************************************************************

# Homework project on implementing functionality for working with banking data

## Running the project
Run the following command in the terminal, being in the root directory of the project, to see the result of some functions:
```
python .\__main__.py
```

### Requirement for running:
- python - v3.12
- python-dotenv - v1.0.1
- requests - v2.32.3
- logging - v0.4.9.6

## Package src:
In the widget.py module, a function mask_account_card is created that takes a string with the holder's name and card number or account number and returns the Holder's name and the masked card number or account number
Transmission format:
*"Visa Platinum 7000792289606361"*
"Account 73654108430135874305"

*Output format:*
"Visa Platinum 7000 79** **** 6361"
"Account **4305"

### Module src\utils.py
Can convert data from a file to a Python object using the path passed to the function:
- conversion_json_to_object

This module also has a function ```transaction_amount```, which takes a transaction dictionary as input, determines the currency type and returns the transaction amount
The function ```transaction_amount``` is associated with the module __Home_work_Skypro\src\external_api.py__, with the function:
- conversion_from_usd_eur_in_rub\
Which can:
- [X] accept an amount in currency as input
- [X] currency name "RUB" or "USD"
- [X] return a "float" number - currency converted to rubles
- [X] also has 1 additional parameter:- url link to api

### New sorting functionality

The src package now has a filter_by_state function that accepts a list of dictionaries and optionally a value for the **state** key (default 'EXECUTED'). The function returns a new list of dictionaries containing only those dictionaries whose **state** key

matches the specified value.

## Iterative output

A module generators has been added to the src package, it implements the following functions:
- filter_by_currency takes a list of dictionaries representing transactions as input and returns an iterator that outputs transactions one by one, where the transaction currency matches the specified one (for example, USD)
- transaction_descriptions takes a list of dictionaries with transactions and returns a description of each transaction in turn
- card_number_generator, which outputs bank card numbers in the format "XXXX XXXX XXXX XXXX", where X is the card number digit.

## Added module logging

By default, the .log file displays information about the function execution, and if errors occur, information about the error and input data

Setting the logging level is done in each module by setting the parameter:
```
.setLevel(logging.INFO)
```

## Testing
Testing modules have appeared in the test package, each module, according to its name, tests program modules from the src package

To run testing, you need:
- pytest library pytest = "^8.3.4"
- pytest-cov library = "^6.0.0"

The root directory contains the htmlcov directory, which contains the index.html module - it displays the project testing statistics. There is also a module test\generators.py, it tests the module src\generators.py
Enter:
```
pytest --cov
```
in the virtual environment of the program root directory to see the number of tests, test pass statuses and coverage.

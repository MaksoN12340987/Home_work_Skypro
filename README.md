# Проект домашней работы по реализации фукционала работы с банковскими данными

### В прокте реализована функция маскировки номера карты и номера счёта - mask_account_card

## Для работы потребуется виртуальное окружение poetry и python версии 3.13 и выше

### Пакет src:
В модуле widget.py создана функция mask_account_card, которая принимает строку с именем держателя и номером карты или номер счёта и возвращает Имя держателя и замаскированный номер карты или номер счёта
Формат передачи:
*"Visa Platinum 7000792289606361"*
"Счет 73654108430135874305"

*Формат вывода:*
"Visa Platinum 7000 79** **** 6361"
"Счет **4305"

## Новый функционал сортировки

В пакете src появилась функця filter_by_state, которая принимает список словарей и опционально значение для ключа **state** (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ **state**
 соответствует указанному значению.


## Итеративный вывод

В пакет src добавлен модкль generators, в нем реализованны вункции:
- filter_by_currency принимает на вход список словарей, представляющих транзакции, а возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)
- transaction_descriptions принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
- card_number_generator, который выдает номера банковских карт в формате "XXXX XXXX XXXX XXXX", где X — цифра номера карты.


## Тестирование 
В пакете test появились модули тестирования, каждый модуль, согласно названию, тестирует модули программы из пакета src

Для запуска тестирование требуется:
- библиотека pytest pytest = "^8.3.4"
- библиотека pytest-cov = "^6.0.0"
В корневом каталоге присутствует дирректория htmlcov, в которой располагается модуль index.html - в нем отражена статистика по тестированию проекта. А также появился модуль test\generators.py, он тестирует модуль src\generators.py
Ввведите "pytest --cov", находясь в виртуальном окружении корневого каталога программы, чтобы увидеть колличество тестов, статусы прохождения тестов и покрытие.


# Homework project on the implementation of functionality for working with bank data

### The project implements the function of masking the card number and account number - mask_account_card

## To work, you will need the poetry virtual environment and python version 3.13 and higher

### Src package:
In the widget.py module, the mask_account_card function is created, which accepts a string with the cardholder name and card number or account number and returns the Cardholder name and the masked card number or account number
*Transmission format:*
"Visa Platinum 7000792289606361"
"Account 73654108430135874305"

*Output format:*
"Visa Platinum 7000 79** **** 6361"
"Account **4305"

## New sorting function

The src package now has a filter_by_state function that takes a list of dictionaries and optionally a value for the **state** key (default 'EXECUTED'). The function returns a new list of dictionaries containing only those dictionaries whose **state** key matches the specified value.


## Iterative output

A module generators has been added to the src package, it implements the following functions:
- filter_by_currency takes a list of dictionaries representing transactions as input and returns an iterator that outputs transactions one by one, where the transaction currency matches the specified one (for example, USD)
- transaction_descriptions takes a list of dictionaries with transactions and returns a description of each transaction in turn
- card_number_generator, which outputs bank card numbers in the format "XXXX XXXX XXXX XXXX", where X is the card number digit.


## Testing

The test package now has testing modules, each module, as the name suggests, tests program modules from the src package

To run testing, you need:
- pytest library pytest = "^8.3.4"
- pytest-cov library = "^6.0.0"
The root directory contains the htmlcov directory, which contains the index.html module - it displays the project testing statistics. Also, the test\generators.py module has appeared, it tests the src\generators.py module. Enter "pytest --cov" while in the virtual environment of the program's root directory to see the number of tests, test statuses, and coverage.

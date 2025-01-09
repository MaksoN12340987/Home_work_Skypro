from functools import wraps


def log(predicate, error_mesage_type, filename: str = ""):
    '''Декоратор log принимает функцию предикат, сообщение об ошибке и
    путь к файлу. Функция предикат может проверять входные данные функции.
    В случае ошибки выводится сообщение error_mesage_type.
    Декоратор отмечает начало работы функции, выводит результат и
      сообщает об окончании работы'''
    def decorator_time_name_error(function):
        @wraps(function)
        def execution(operand):
            if not predicate(operand):
                with open(filename, "a") as file:
                    file.write(f"{function} ERROR:\n{error_mesage_type}\nInputs: {operand}\n")
                raise ValueError(error_mesage_type)

            elif filename != "":
                resault = function(operand)
                with open(filename, "a") as file:
                    file.write(f"{function} ok\n")

            else:
                print(f"Start " + f"{function}"[1:-23])
                resault = print(function(operand))
                print("The function has completed")
            return resault

        return execution

    return decorator_time_name_error


def predicate_is_str(is_str):
    return isinstance(is_str, str)

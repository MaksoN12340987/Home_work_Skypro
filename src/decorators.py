from functools import wraps


def log(predicate_str, error_mesage_type, filename: str = ""):
    def decorator_time_name_error(function):
        @wraps(function)
        def execution(operand):
            if not predicate_str(operand):
                with open(filename, "a") as file:
                    file.write(f"{function} ERROR:\n{error_mesage_type}\nInputs: {operand}\n")
                raise ValueError(error_mesage_type)

            elif filename != "":
                resault = function(operand)
                with open(filename, "a") as file:
                    file.write(f"{function} ok\n")

            else:
                resault = function(operand)
                print(f"Function is {function}\n{resault}")
            return resault

        return execution

    return decorator_time_name_error


def predicate_is_str(is_str):

    return isinstance(is_str, str)

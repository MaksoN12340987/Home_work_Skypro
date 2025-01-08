from time import time
from functools import wraps


def log(predicate_none, error_mesage_none, predicate_str, error_mesage_str, filename: str = ""):
    def decorator_time_name_error(function):
        @wraps(function)
        def execution(to_mask):
            call = time()
            if filename != "":
                if predicate_str(to_mask):
                    raise ValueError(error_mesage_str)
                elif predicate_none(to_mask):
                    raise ValueError(error_mesage_none)
                else:
                    with open(filename, "a") as file:
                        file.write(f"Call in {call}\n")
                    resault = function(to_mask)
                    with open(filename, "a") as file:
                        file.write(f"Function is {function}\n")
            else:
                if predicate_str(to_mask):
                    raise ValueError(error_mesage_str)
                elif predicate_none(to_mask):
                    raise ValueError(error_mesage_none)
                else:
                    resault = function(to_mask)
                    print(f"Function is {function}{resault}")
            return resault
        return execution
    return decorator_time_name_error


def predicate_is_str(is_str):
    return type(is_str) != str


def predicate_not_none(is_valeu):
    return is_valeu == None

from time import time
from functools import wraps



def log(predicate_none, error_mesage_none, predicate_str, error_mesage_str, filename:str = ""):
    def decorator_time_name_error(function):
        @wraps(function)
        def execution(bank_account, start):
            if filename != "":
                if predicate_str(bank_account):
                    raise ValueError(error_mesage_str)
                elif predicate_none(bank_account):
                    raise ValueError(error_mesage_none)
                else:
                    resault = function(bank_account, start)
            else:
                if predicate_str(bank_account):
                    raise ValueError(error_mesage_str)
                elif predicate_none(bank_account):
                    raise ValueError(error_mesage_none)
                else:
                    print(f"Call in {call}")
                    print(f"Function is {function}")
                    resault = function(bank_account, start)
            return resault
        return execution
    return decorator_time_name_error


def predicate_is_str(is_str):
    return type(is_str) != str


def predicate_not_none(is_valeu):
    return is_valeu == None

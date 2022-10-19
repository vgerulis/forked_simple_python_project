from typing import Callable, Optional


def timer(fn: Callable) -> Callable:
    # TODO: Log how much time has passed
    pass


def calculator_logger(fn: Callable) -> Callable:
    # TODO: Log function name and it's args and kwargs
    pass


def input_parser(fn: Callable) -> Callable:
    def convert_to_int(*args) -> Optional[int]:
        # TODO: Enable this function to work with multiple args and kwargs
        try:
            return fn(args[0], int(args[1]))
        except Exception:
            print(f"Cannot convert input of type {type(args[1])} to an int")
            return None

    return convert_to_int

from typing import Callable, Optional
import logging
logging.basicConfig(filename="output.log", level=logging.INFO)


def calculator_logger(fn: Callable) -> Callable:
    def calculator_logger(*args, **kwargs):
        logging.info(f"Running a function {fn.__name__} with args: {args} and kwargs: {kwargs}")
        return fn(*args, **kwargs)
    return calculator_logger

# def timer(fn: Callable) -> Callable:
#     # TODO: Log how much time has passed
#     pass

def input_parser(fn: Callable) -> Callable:
    def convert_to_int(*args) -> Optional[int]:
        # TODO: Enable this function to work with multiple args and kwargs
        try:
            return fn(args[0], int(args[1]), int(args[2]))
        except Exception:
            print(f"Cannot convert input of type {type(args[1])} {type(args[2])} to an int")
            return None

    return convert_to_int

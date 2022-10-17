from typing import Any, Optional


def convert_to_int(x: Any) -> Optional[int]:
    try:
        return int(x)
    except Exception:
        print(f"Cannot convert input of type {type(x)} to an int")
        return None

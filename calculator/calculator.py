from calculator.utils.helpers import convert_to_int


class Calculator:
    def __init__(self) -> None:
        self._memory = 0

    @property
    def memory(self) -> int:
        return self._memory

    def clear(self) -> int:
        self._memory = 0
        return self._memory

    def add(self, a: int) -> int:
        converted_a = convert_to_int(a)
        if converted_a:
            self._memory += converted_a
        return self._memory

    def sub(self, a: int) -> int:
        converted_a = convert_to_int(a)
        if converted_a:
            self._memory -= converted_a
        return self._memory

    def mul(self, a: int) -> int:
        converted_a = convert_to_int(a)
        if converted_a:
            self._memory *= converted_a
        return self._memory

    def pow(self, a: int) -> int:
        converted_a = convert_to_int(a)
        if converted_a:
            self._memory = self._memory**a
        return self._memory

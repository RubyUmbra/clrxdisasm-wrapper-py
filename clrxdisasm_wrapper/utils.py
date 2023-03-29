import os
from contextlib import contextmanager


class Bits:
    def __init__(self, num: int = 0, size: int = 0):
        self.num: int = num
        self.size: int = size

    def push_end(self, value: int, size: int):
        self.num <<= size
        self.num |= value & ((1 << size) - 1)
        self.size += size

    def pop_end(self, size: int) -> int:
        value = self.num & ((1 << size) - 1)
        self.num >>= size
        self.size -= size
        return value

    def __str__(self):
        return f"0b{self.num:0{self.size}b}"


@contextmanager
def temp_file(filename: str):
    try:
        yield filename
    finally:
        os.remove(filename)

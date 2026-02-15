from typing import List
from typing import Protocol


# Stack class with high coupling to list
class Stack:
    def __init__(self, storage: list):
        self._storage = storage


# Decoupled Stack class

class StorageProtocol(Protocol):
    def append(self, item: object) -> None: ...


class DecoupledStack:
    def __init__(self, storage: StorageProtocol):
        self._storage = storage


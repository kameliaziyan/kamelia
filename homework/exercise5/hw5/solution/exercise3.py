import time
from typing import Any, Optional


class _Node:
    def __init__(self, key: str, value: Any, timestamp: float) -> None:

        self.key = key
        self.value = value
        self.timestamp = timestamp
        self.prev: Optional["_Node"] = None
        self.next: Optional["_Node"] = None


class _DoublyLinkedList:
    def __init__(self) -> None:

        self._head = _Node("", None, 0)
        self._tail = _Node("", None, 0)
        self._head.next = self._tail
        self._tail.prev = self._head

    def add_to_front(self, node: _Node) -> None:

        first_node = self._head.next
        node.prev = self._head
        node.next = first_node

        if first_node is not None:
            first_node.prev = node

        self._head.next = node

    def remove(self, node: _Node) -> None:
        if node is None:
            return

        prev_node = node.prev
        next_node = node.next

        if prev_node is None or next_node is None:
            return

        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None

    def move_to_front(self, node: _Node) -> None:

        self.remove(node)
        self.add_to_front(node)

    def remove_last(self) -> Optional[_Node]:
        last_node = self._tail.prev

        if_node = self._tail.prev

        if last_node is None or last_node is self._head:
            return None

        self.remove(last_node)
        return last_node

    def clear(self) -> None:
        self._head.next = self._tail
        self._tail.prev = self._head


class MyLruCache:

    def __init__(self, maxsize: int, ttl: float) -> None:

        if maxsize <= 0:
            raise ValueError("maxsize must be > 0")
        if ttl <= 0:
            raise ValueError("ttl must be > 0")

        self.maxsize = maxsize
        self.ttl = ttl
        self._cache: dict[str, _Node] = {}
        self._linked_list = _DoublyLinkedList()

    def get(self, key: str) -> Any | None:
        node = self._cache.get(key)

        if node is None:
            return None

        if self._is_expired(node):
            self._linked_list.remove(node)
            self._cache.pop(key, None)
            return None

        self._linked_list.move_to_front(node)
        return node.value

    def set(self, key: str, value: Any) -> None:

        existing_node = self._cache.get(key)
        if existing_node is not None:
            existing_node.value = value
            existing_node.timestamp = time.time()
            self._linked_list.move_to_front(existing_node)
            return

        if len(self._cache) >= self.maxsize:
            lru_node = self._linked_list.remove_last()
            if lru_node is not None:
                self._cache.pop(lru_node.key, None)

        new_node = _Node(key, value, time.time())
        self._cache[key] = new_node
        self._linked_list.add_to_front(new_node)

    def clear(self) -> None:

        self._cache.clear()
        self._linked_list.clear()

    def __len__(self) -> int:

        return len(self._cache)

    def __contains__(self, key: str) -> bool:

        node = self._cache.get(key)

        if node is None:
            return False

        if self._is_expired(node):
            self._linked_list.remove(node)
            self._cache.pop(key, None)
            return False

        return True

    def _is_expired(self, node: _Node) -> bool:
        return (time.time() - node.timestamp) > self.ttl

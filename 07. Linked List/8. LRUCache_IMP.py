"""
LRU Cache (Medium)
Source: https://leetcode.com/problems/lru-cache/

An ordered dictionary combines O(1) key lookup with recency ordering. Reads
and writes move a key to the newest end; overflow evicts the oldest key.

Time: O(1) average for get and put | Space: O(capacity)
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._values: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._values:
            return -1
        self._values.move_to_end(key)
        return self._values[key]

    def put(self, key: int, value: int) -> None:
        if self._capacity <= 0:
            return
        if key in self._values:
            self._values.move_to_end(key)
        self._values[key] = value
        if len(self._values) > self._capacity:
            self._values.popitem(last=False)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1

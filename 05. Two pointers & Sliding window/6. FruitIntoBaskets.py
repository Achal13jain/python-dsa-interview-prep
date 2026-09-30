"""
Fruit Into Baskets (Medium)
Source: https://leetcode.com/problems/fruit-into-baskets/

Find the longest contiguous subarray containing at most two distinct values.
Use a variable-size sliding window and shrink it whenever a third type enters.

Time: O(n) | Space: O(1), because the map contains at most three fruit types.
"""

from typing import Dict, List


def total_fruit(fruits: List[int]) -> int:
    counts: Dict[int, int] = {}
    left = 0
    best = 0

    for right, fruit in enumerate(fruits):
        counts[fruit] = counts.get(fruit, 0) + 1
        while len(counts) > 2:
            left_fruit = fruits[left]
            counts[left_fruit] -= 1
            if counts[left_fruit] == 0:
                del counts[left_fruit]
            left += 1
        best = max(best, right - left + 1)

    return best


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        return total_fruit(fruits)


if __name__ == "__main__":
    assert total_fruit([]) == 0
    assert total_fruit([1, 2, 1]) == 3
    assert total_fruit([0, 1, 2, 2]) == 3

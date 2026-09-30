"""
Koko Eating Bananas (Medium)
Source: https://leetcode.com/problems/koko-eating-bananas/

Binary-search the eating speed. The hours required decrease monotonically as
the speed increases, so feasibility identifies which half to keep.

Time: O(n log(max(piles))) | Space: O(1)
"""

from typing import List


def min_eating_speed(piles: List[int], hours: int) -> int:
    if not piles:
        return 0

    left, right = 1, max(piles)
    while left < right:
        speed = (left + right) // 2
        required = sum((pile + speed - 1) // speed for pile in piles)
        if required <= hours:
            right = speed
        else:
            left = speed + 1
    return left


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return min_eating_speed(piles, h)


if __name__ == "__main__":
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30

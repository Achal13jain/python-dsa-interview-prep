"""
Subarray Product Less Than K (Medium)
Source: https://leetcode.com/problems/subarray-product-less-than-k/

For positive integers, expand a sliding window and shrink it until its product
is below k. Every suffix ending at the right edge is then valid.

Time: O(n) | Space: O(1)
"""

from typing import List


def num_subarray_product_less_than_k(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    product = 1
    left = 0
    count = 0
    for right, value in enumerate(nums):
        product *= value
        while product >= k:
            product //= nums[left]
            left += 1
        count += right - left + 1
    return count


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        return num_subarray_product_less_than_k(nums, k)


if __name__ == "__main__":
    assert num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8
    assert num_subarray_product_less_than_k([1, 2, 3], 0) == 0

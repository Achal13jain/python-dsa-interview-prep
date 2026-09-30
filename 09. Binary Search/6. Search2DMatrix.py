"""
Search a 2D Matrix (Medium)
Source: https://leetcode.com/problems/search-a-2d-matrix/

Treat the matrix as one sorted array and map a virtual index back to its row
and column during binary search.

Time: O(log(m*n)) | Space: O(1)
"""

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows, columns = len(matrix), len(matrix[0])
    left, right = 0, rows * columns - 1
    while left <= right:
        middle = (left + right) // 2
        value = matrix[middle // columns][middle % columns]
        if value == target:
            return True
        if value < target:
            left = middle + 1
        else:
            right = middle - 1
    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return search_matrix(matrix, target)


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(matrix, 3)
    assert not search_matrix(matrix, 13)

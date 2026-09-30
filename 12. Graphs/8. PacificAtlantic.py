"""
Pacific Atlantic Water Flow (Medium)
Source: https://leetcode.com/problems/pacific-atlantic-water-flow/

Search in reverse from each ocean: water can reach a neighbor in the reverse
search when that neighbor is at least as high. Cells reached by both searches
can flow to both oceans.

Time: O(m*n) | Space: O(m*n)
"""

from collections import deque
from typing import Deque, List, Set, Tuple


Cell = Tuple[int, int]


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    if not heights or not heights[0]:
        return []

    rows, columns = len(heights), len(heights[0])

    def reachable(starts: Set[Cell]) -> Set[Cell]:
        seen = set(starts)
        queue: Deque[Cell] = deque(starts)
        while queue:
            row, column = queue.popleft()
            for next_row, next_column in (
                (row + 1, column),
                (row - 1, column),
                (row, column + 1),
                (row, column - 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and (next_row, next_column) not in seen
                    and heights[next_row][next_column] >= heights[row][column]
                ):
                    seen.add((next_row, next_column))
                    queue.append((next_row, next_column))
        return seen

    pacific = {(row, 0) for row in range(rows)} | {(0, column) for column in range(columns)}
    atlantic = {(row, columns - 1) for row in range(rows)} | {
        (rows - 1, column) for column in range(columns)
    }
    return [[row, column] for row, column in sorted(reachable(pacific) & reachable(atlantic))]


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        return pacific_atlantic(heights)


if __name__ == "__main__":
    grid = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    assert len(pacific_atlantic(grid)) == 7

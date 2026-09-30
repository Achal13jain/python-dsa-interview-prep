"""
Binary Tree Right Side View (Medium)
Source: https://leetcode.com/problems/binary-tree-right-side-view/

Run breadth-first search one level at a time and record the last node visited
at each level.

Time: O(n) | Space: O(w), where w is the maximum tree width.
"""

from __future__ import annotations

from collections import deque
from typing import Deque, List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result: List[int] = []
    queue: Deque[TreeNode] = deque([root])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            rightmost = node.val
        result.append(rightmost)
    return result


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return right_side_view(root)


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3, right=TreeNode(4)))
    assert right_side_view(root) == [1, 3, 4]

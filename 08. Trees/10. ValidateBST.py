"""
Validate Binary Search Tree (Medium)
Source: https://leetcode.com/problems/validate-binary-search-tree/

Traverse iteratively while carrying strict lower and upper bounds. Every node
must lie inside the bounds inherited from its ancestors.

Time: O(n) | Space: O(h)
"""

from __future__ import annotations

from typing import Optional, Tuple


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


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    stack: list[Tuple[TreeNode, float, float]] = []
    if root:
        stack.append((root, float("-inf"), float("inf")))

    while stack:
        node, lower, upper = stack.pop()
        if not lower < node.val < upper:
            return False
        if node.right:
            stack.append((node.right, node.val, upper))
        if node.left:
            stack.append((node.left, lower, node.val))
    return True


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return is_valid_bst(root)


if __name__ == "__main__":
    assert is_valid_bst(TreeNode(2, TreeNode(1), TreeNode(3)))
    assert not is_valid_bst(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))

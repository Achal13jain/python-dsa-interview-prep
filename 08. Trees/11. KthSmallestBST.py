"""
Kth Smallest Element in a BST (Medium)
Source: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

An inorder traversal of a BST visits values in sorted order. Stop when the
k-th node is popped from the explicit traversal stack.

Time: O(h + k) | Space: O(h)
"""

from __future__ import annotations

from typing import Optional


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


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    if k <= 0:
        raise ValueError("k must be positive")

    stack: list[TreeNode] = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    raise ValueError("k exceeds the number of tree nodes")


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return kth_smallest(root, k)


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, right=TreeNode(2)), TreeNode(4))
    assert kth_smallest(root, 1) == 1
    assert kth_smallest(root, 3) == 3

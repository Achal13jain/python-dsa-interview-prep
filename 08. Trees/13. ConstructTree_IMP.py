"""
Construct Binary Tree from Preorder and Inorder Traversal (Medium)
Source: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Build the tree iteratively. A stack tracks ancestors whose inorder position
has not yet been consumed, avoiding Python recursion-depth failures.

Time: O(n) | Space: O(n)
"""

from __future__ import annotations

from typing import List, Optional


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


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
        return None
    if len(preorder) != len(inorder):
        raise ValueError("preorder and inorder must have equal lengths")

    root = TreeNode(preorder[0])
    stack = [root]
    inorder_index = 0

    for value in preorder[1:]:
        node = stack[-1]
        if node.val != inorder[inorder_index]:
            node.left = TreeNode(value)
            stack.append(node.left)
            continue

        while stack and stack[-1].val == inorder[inorder_index]:
            node = stack.pop()
            inorder_index += 1
        node.right = TreeNode(value)
        stack.append(node.right)
    return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return build_tree(preorder, inorder)


if __name__ == "__main__":
    tree = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert tree and tree.val == 3 and tree.left and tree.left.val == 9
    assert tree.right and tree.right.left and tree.right.left.val == 15

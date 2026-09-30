"""
Copy List with Random Pointer (Medium)
Source: https://leetcode.com/problems/copy-list-with-random-pointer/

Create a copy for each original node, map originals to copies, then connect
the copied next and random pointers in a second pass.

Time: O(n) | Space: O(n)
"""

from __future__ import annotations

from typing import Dict, Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        next: Optional[Node] = None,
        random: Optional[Node] = None,
    ) -> None:
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    copies: Dict[Optional[Node], Optional[Node]] = {None: None}
    node = head
    while node:
        copies[node] = Node(node.val)
        node = node.next

    node = head
    while node:
        copy = copies[node]
        copy.next = copies[node.next]  # type: ignore[union-attr]
        copy.random = copies[node.random]  # type: ignore[union-attr]
        node = node.next
    return copies[head]


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        return copy_random_list(head)


if __name__ == "__main__":
    first = Node(7)
    second = Node(13)
    first.next = second
    second.random = first
    copied = copy_random_list(first)
    assert copied is not first and copied.val == 7
    assert copied.next is not second and copied.next.random is copied

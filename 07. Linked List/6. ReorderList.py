"""
Reorder List (Medium)
Source: https://leetcode.com/problems/reorder-list/

Split the list at its midpoint, reverse the second half, then weave the two
halves together. The nodes are rearranged in place.

Time: O(n) | Space: O(1)
"""

from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None
    previous = None
    while second:
        following = second.next
        second.next = previous
        previous = second
        second = following

    first = head
    second = previous
    while second:
        first_next = first.next
        second_next = second.next
        first.next = second
        second.next = first_next
        first = first_next
        second = second_next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        reorder_list(head)


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reorder_list(head)
    values = []
    while head:
        values.append(head.val)
        head = head.next
    assert values == [1, 4, 2, 3]

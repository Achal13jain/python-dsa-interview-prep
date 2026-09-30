"""
Implement Queue Using Stacks (Easy)
Source: https://leetcode.com/problems/implement-queue-using-stacks/

Use an input stack for pushes and an output stack for pops. Transfer elements
only when the output stack is empty, giving amortized O(1) operations.

Time: O(1) amortized per operation | Space: O(n)
"""

from typing import List


class MyQueue:
    def __init__(self) -> None:
        self._input: List[int] = []
        self._output: List[int] = []

    def push(self, value: int) -> None:
        self._input.append(value)

    def _move_if_needed(self) -> None:
        if not self._output:
            while self._input:
                self._output.append(self._input.pop())

    def pop(self) -> int:
        self._move_if_needed()
        return self._output.pop()

    def peek(self) -> int:
        self._move_if_needed()
        return self._output[-1]

    def empty(self) -> bool:
        return not self._input and not self._output


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert not queue.empty()

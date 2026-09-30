"""
Evaluate Reverse Polish Notation (Medium)
Source: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Push numbers onto a stack. For an operator, pop the right and left operands,
evaluate them, and push the result. Division truncates toward zero.

Time: O(n) | Space: O(n)
"""

from typing import List


def eval_rpn(tokens: List[str]) -> int:
    stack: List[int] = []
    for token in tokens:
        if token not in {"+", "-", "*", "/"}:
            stack.append(int(token))
            continue

        right = stack.pop()
        left = stack.pop()
        if token == "+":
            stack.append(left + right)
        elif token == "-":
            stack.append(left - right)
        elif token == "*":
            stack.append(left * right)
        else:
            quotient = abs(left) // abs(right)
            stack.append(-quotient if (left < 0) != (right < 0) else quotient)
    return stack[-1]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return eval_rpn(tokens)


if __name__ == "__main__":
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["7", "-3", "/"]) == -2

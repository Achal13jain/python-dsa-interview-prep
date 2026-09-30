"""
Daily Temperatures (Medium)
Source: https://leetcode.com/problems/daily-temperatures/

Keep indices in a decreasing monotonic stack. A warmer temperature resolves
all colder unresolved days at the top of the stack.

Time: O(n) | Space: O(n)
"""

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack: List[int] = []

    for day, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            previous_day = stack.pop()
            answer[previous_day] = day - previous_day
        stack.append(day)
    return answer


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return daily_temperatures(temperatures)


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([]) == []

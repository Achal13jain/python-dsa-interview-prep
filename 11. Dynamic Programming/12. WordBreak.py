"""
Word Break (Medium)
Source: https://leetcode.com/problems/word-break/

Let dp[i] mean that s[:i] can be segmented. For each reachable boundary,
check only word lengths that occur in the dictionary.

Time: O(n * L * W) in the worst case | Space: O(n + dictionary size)
L is the number of distinct word lengths and W is slicing/comparison cost.
"""

from typing import List, Set


def word_break(text: str, word_dict: List[str]) -> bool:
    words: Set[str] = set(word_dict)
    lengths = {len(word) for word in words if word}
    reachable = [False] * (len(text) + 1)
    reachable[0] = True

    for end in range(1, len(text) + 1):
        for length in lengths:
            start = end - length
            if start >= 0 and reachable[start] and text[start:end] in words:
                reachable[end] = True
                break
    return reachable[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return word_break(s, wordDict)


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"])
    assert not word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert word_break("", ["a"])

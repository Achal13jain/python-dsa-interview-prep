# Python DSA Interview Prep

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Problems](https://img.shields.io/badge/Problems-121-success)
![Core 120](https://img.shields.io/badge/Core_120-120%2F120-5468FF)
![Topics](https://img.shields.io/badge/Topics-15-orange)
![License](https://img.shields.io/badge/License-MIT-green)
[![Quality checks](https://github.com/Achal13jain/python-dsa-interview-prep/actions/workflows/quality.yml/badge.svg)](https://github.com/Achal13jain/python-dsa-interview-prep/actions/workflows/quality.yml)

> **⭐ Star this repo if it helps you crack your interview!**

**121 solved problems across 15 topics**, organized by the patterns and data
structures that appear most often in Python interviews. Each solution includes
an approach and complexity analysis; priority questions are marked `_IMP`.

Browse the filterable [DSA Prep Atlas](https://dsa-prep-atlas.pages.dev/) or
follow the [Core 120 roadmap](./ROADMAP.md) for the planned learning sequence.

---

## 📖 Guides

| Resource | Purpose |
|----------|---------|
| [🌐 Visual Index](https://dsa-prep-atlas.pages.dev/) | Browse all problems in a filterable UI |
| [PATTERNS.md](./PATTERNS.md) | Signal → technique cheat-sheet — "which pattern do I use?" |
| [DATA_STRUCTURES.md](./DATA_STRUCTURES.md) | Requirement → data-structure chooser |
| [ROADMAP.md](./ROADMAP.md) | Follow the curated path from 98 to 120 problems |

---

## ✅ Core 120 Progress

**Core 120 progress:** 120 / 120 problems (100%) — complete, plus 1 bonus problem.

The original 98-problem collection and the Core 120 expansion are complete.
One additional Basics problem is included as a bonus, for 121 total solutions.

| # | Topic | Easy | Medium | Hard | Total |
|---|-------|------|--------|------|-------|
| 01 | Basic and Maths | 6 | 3 | 0 | 9 |
| 02 | Array and Prefix Sum | 8 | 9 | 0 | 17 |
| 03 | Strings | 4 | 4 | 1 | 9 |
| 04 | Hashing | 1 | 4 | 0 | 5 |
| 05 | Two Pointers & Sliding Window | 1 | 5 | 1 | 7 |
| 06 | Stack & Queue | 1 | 5 | 1 | 7 |
| 07 | Linked List | 3 | 5 | 0 | 8 |
| 08 | Trees | 5 | 6 | 2 | 13 |
| 09 | Binary Search | 1 | 4 | 2 | 7 |
| 10 | Greedy Problems | 1 | 5 | 0 | 6 |
| 11 | Dynamic Programming | 2 | 9 | 1 | 12 |
| 12 | Graphs | 2 | 7 | 0 | 9 |
| 13 | Heap & Priority Queue | 0 | 2 | 2 | 4 |
| 14 | Backtracking | 0 | 4 | 1 | 5 |
| 15 | Trie | 0 | 2 | 1 | 3 |
| | **Total** | **35** | **74** | **12** | **121** |

> **Note:** TreeNode.py in the Trees folder is a shared helper class, not a problem.  
> Counts and website mappings are verified automatically in CI: 121 solution files across 15 topic folders.

---

## 📚 Topics Covered

### 1. Basic and Maths
LCM & GCD · Divisors · XOR properties · Power and modular exponentiation · Sieve of Eratosthenes · Perfect squares

### 2. Array and Prefix Sum
Two Sum · 3Sum · Kadane's (max subarray) · Prefix sum · Product of array except self · Merge sorted arrays · Move zeroes

### 3. Strings
Valid parentheses · Longest substring without repeating · Minimum window substring · Longest palindromic substring · Group anagrams

### 4. Hashing
Frequency counting · Longest consecutive sequence · Custom data structure design · Count distinct elements in window · Valid Sudoku

### 5. Two Pointers & Sliding Window
Two sum (sorted) · Sliding window maximum · Maximum consecutive ones · Character replacement · Permutation in string · Fruit baskets · Subarray product

### 6. Stack & Queue
Next greater element · Min stack · Largest rectangle in histogram · Rotten Oranges · Daily temperatures · Reverse Polish notation · Queue using stacks

### 7. Linked List
Reverse · Loop detection (Floyd's) · Merge sorted lists · Middle element · Remove nth from end · Reorder list · Random pointers · LRU cache

### 8. Trees
In/Pre/Post-order traversal · Level-order · Height · Diameter · LCA · Path sum · Max path sum · Subtree check · Serialize & Deserialize · BST validation · Kth smallest · Right-side view · Construct from traversals

### 9. Binary Search
Standard binary search · Search in rotated sorted array · Book allocation · Aggressive cows · Peak element · Search a 2D matrix · Koko eating bananas

### 10. Greedy Problems
Monster battle · Minimum platforms · Job sequencing · Merge intervals · Gas station · Fractional knapsack

### 11. Dynamic Programming
Fibonacci · Climbing stairs · Coin change · LIS · LCS · 0/1 Knapsack · Partition equal sum · Max product subarray · Edit distance · Unique paths · House robber · Word break

### 12. Graphs
BFS template · DFS (recursive + iterative) · Number of Islands · Clone Graph · Course Schedule · Network Delay Time · Number of Provinces · Pacific Atlantic water flow · Minimum spanning tree

### 13. Heap & Priority Queue
Kth largest element · Top K frequent elements · Merge K sorted lists · Find median from data stream

### 14. Backtracking
Subsets · Permutations · Combination sum · N-Queens · Word search

### 15. Trie
Implement Trie (prefix tree) · Add and search wildcard words · Word Search II

---

## 🗂️ Repository Structure

```
├── 01. Basic and maths/        (9 problems)
├── 02. Array and prefix_sum/   (17 problems)
├── 03. Strings/                (9 problems)
├── 04. Hashing/                (5 problems)
├── 05. Two pointers & Sliding window/  (7 problems)
├── 06. Stack & Queue/          (7 problems)
├── 07. Linked List/            (8 problems)
├── 08. Trees/                  (13 problems + TreeNode.py helper)
├── 09. Binary Search/          (7 problems)
├── 10. Greedy Problems/        (6 problems)
├── 11. Dynamic Programming/    (12 problems)
├── 12. Graphs/                 (9 problems)
├── 13. Heap and Priority Queue/ (4 problems)
├── 14. Backtracking/           (5 problems)
├── 15. Trie/                   (3 problems)
├── tests/                       — behavior and catalog consistency checks
├── index.html                  — filterable visual index
├── PATTERNS.md                 — signal → technique cheat-sheet
├── DATA_STRUCTURES.md          — requirement → data-structure chooser
└── ROADMAP.md                  — path to the Core 120 collection
```

---

## 🎯 How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/Achal13jain/python-dsa-interview-prep.git
   cd python-dsa-interview-prep
   ```
2. **Navigate to a topic folder** and open any `.py` file.
3. **Read or run the solution** — some files include a `if __name__ == "__main__":` sample block, and the rest can be tested by calling the function/class directly.
4. **Focus on `_IMP` files** for quick interview prep — these are the priority revision picks in this repo.
5. **Read PATTERNS.md** to recognise which technique to apply when you see a problem signal.

### Run the quality checks

No third-party packages are required:

```bash
python -m unittest discover -s tests -v
```

The suite checks solution behavior, Python 3.9 syntax, duplicate or missing
catalog entries, README counts, website mappings, and documentation redirects.
GitHub Actions runs the same checks on Python 3.9 and 3.13 for every push and
pull request.

---

## 💡 Problem Markers

- **`_IMP`** — Important priority picks for interview revision.
- **Regular files** — Core problems for building solid fundamentals.

---

## 📖 Recommended Learning Path

### Beginner
```
Basic and Maths → Array & Prefix Sum → Strings → Hashing
```

### Intermediate
```
Two Pointers & Sliding Window → Stack & Queue → Linked List
```

### Advanced
```
Trees → Binary Search → Greedy → Dynamic Programming
→ Graphs → Heap & Priority Queue → Backtracking → Trie
```

### Fast-track Interview Prep (2–3 weeks)
Focus on all **`_IMP`** files across every topic. They cover the patterns most likely to appear in a 45-minute interview round.

---

## 🤝 Contributing

Found an issue or want to improve a solution?

1. Fork the repository.
2. Add or improve a solution using the documented problem template.
3. Update the website catalog when adding a new problem.
4. Run `python -m unittest discover -s tests -v`.
5. Submit a pull request.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

## 📝 License

MIT — free to use for learning and interview preparation.

---

## 👨‍💻 Author

**Achal Jain** · [github.com/Achal13jain](https://github.com/Achal13jain)

---

*Last updated: September 2026*

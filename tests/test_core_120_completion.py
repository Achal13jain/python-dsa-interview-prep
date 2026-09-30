"""Behavior tests for the final Core 120 roadmap batches."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    if spec is None or spec.loader is None:
        raise ImportError(relative_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


fruit = load_module("fruit", "05. Two pointers & Sliding window/6. FruitIntoBaskets.py")
product = load_module(
    "product_less_than_k",
    "05. Two pointers & Sliding window/7. SubarrayProductLessThanK.py",
)
temperatures = load_module("temperatures", "06. Stack & Queue/5. DailyTemperatures_IMP.py")
rpn = load_module("rpn", "06. Stack & Queue/6. EvaluateRPN.py")
queue_module = load_module("queue_module", "06. Stack & Queue/7. ImplementQueueUsingStacks.py")
reorder = load_module("reorder", "07. Linked List/6. ReorderList.py")
copy_random = load_module("copy_random", "07. Linked List/7. CopyListRandomPointer_IMP.py")
lru = load_module("lru", "07. Linked List/8. LRUCache_IMP.py")
validate_bst = load_module("validate_bst", "08. Trees/10. ValidateBST.py")
kth_bst = load_module("kth_bst", "08. Trees/11. KthSmallestBST.py")
right_view = load_module("right_view", "08. Trees/12. RightSideView.py")
construct_tree = load_module("construct_tree", "08. Trees/13. ConstructTree_IMP.py")
matrix_search = load_module("matrix_search", "09. Binary Search/6. Search2DMatrix.py")
koko = load_module("koko", "09. Binary Search/7. KokoEatingBananas.py")
word_break_module = load_module("word_break_module", "11. Dynamic Programming/12. WordBreak.py")
pacific = load_module("pacific", "12. Graphs/8. PacificAtlantic.py")
mst = load_module("mst", "12. Graphs/9. MinimumSpanningTree_IMP.py")


class SlidingWindowCompletionTests(unittest.TestCase):
    def test_fruit_into_baskets(self) -> None:
        self.assertEqual(0, fruit.total_fruit([]))
        self.assertEqual(3, fruit.total_fruit([1, 2, 1]))
        self.assertEqual(4, fruit.total_fruit([1, 2, 3, 2, 2]))

    def test_subarray_product_less_than_k(self) -> None:
        self.assertEqual(8, product.num_subarray_product_less_than_k([10, 5, 2, 6], 100))
        self.assertEqual(0, product.num_subarray_product_less_than_k([1, 2, 3], 1))
        self.assertEqual(6, product.num_subarray_product_less_than_k([1, 1, 1], 2))


class StackQueueCompletionTests(unittest.TestCase):
    def test_daily_temperatures(self) -> None:
        self.assertEqual(
            [1, 1, 4, 2, 1, 1, 0, 0],
            temperatures.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
        )
        self.assertEqual([0, 0, 0], temperatures.daily_temperatures([3, 2, 1]))

    def test_reverse_polish_notation_and_exact_division(self) -> None:
        self.assertEqual(22, rpn.eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
        self.assertEqual(-2, rpn.eval_rpn(["7", "-3", "/"]))
        self.assertEqual(10**30, rpn.eval_rpn([str(3 * 10**30), "3", "/"]))

    def test_queue_using_stacks(self) -> None:
        queue = queue_module.MyQueue()
        self.assertTrue(queue.empty())
        queue.push(1)
        queue.push(2)
        self.assertEqual(1, queue.peek())
        self.assertEqual(1, queue.pop())
        queue.push(3)
        self.assertEqual(2, queue.pop())
        self.assertEqual(3, queue.pop())
        self.assertTrue(queue.empty())


class LinkedListCompletionTests(unittest.TestCase):
    def test_reorder_list_for_even_and_odd_lengths(self) -> None:
        for values, expected in (([1, 2, 3, 4], [1, 4, 2, 3]), ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])):
            head = None
            for value in reversed(values):
                head = reorder.ListNode(value, head)
            reorder.reorder_list(head)
            actual = []
            while head:
                actual.append(head.val)
                head = head.next
            self.assertEqual(expected, actual)

    def test_copy_random_list_is_a_deep_copy(self) -> None:
        nodes = [copy_random.Node(value) for value in (7, 13, 11)]
        nodes[0].next = nodes[1]
        nodes[1].next = nodes[2]
        nodes[1].random = nodes[0]
        nodes[2].random = nodes[1]

        copied = copy_random.copy_random_list(nodes[0])

        self.assertIsNot(copied, nodes[0])
        self.assertEqual(7, copied.val)
        self.assertIs(copied.next.random, copied)
        self.assertIs(copied.next.next.random, copied.next)

    def test_lru_cache_eviction_and_update(self) -> None:
        cache = lru.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(1, cache.get(1))
        cache.put(3, 3)
        self.assertEqual(-1, cache.get(2))
        cache.put(1, 10)
        cache.put(4, 4)
        self.assertEqual(-1, cache.get(3))
        self.assertEqual(10, cache.get(1))


class TreeCompletionTests(unittest.TestCase):
    def test_validate_bst(self) -> None:
        valid = validate_bst.TreeNode(2, validate_bst.TreeNode(1), validate_bst.TreeNode(3))
        invalid = validate_bst.TreeNode(5, validate_bst.TreeNode(1), validate_bst.TreeNode(4, validate_bst.TreeNode(3), validate_bst.TreeNode(6)))
        self.assertTrue(validate_bst.is_valid_bst(valid))
        self.assertFalse(validate_bst.is_valid_bst(invalid))
        self.assertFalse(validate_bst.is_valid_bst(validate_bst.TreeNode(1, right=validate_bst.TreeNode(1))))

    def test_bst_operations_handle_deep_trees(self) -> None:
        size = 1_500
        root = validate_bst.TreeNode(0)
        node = root
        for value in range(1, size):
            node.right = validate_bst.TreeNode(value)
            node = node.right
        self.assertTrue(validate_bst.is_valid_bst(root))

        kth_root = kth_bst.TreeNode(0)
        node = kth_root
        for value in range(1, size):
            node.right = kth_bst.TreeNode(value)
            node = node.right
        self.assertEqual(size - 1, kth_bst.kth_smallest(kth_root, size))

    def test_right_side_view(self) -> None:
        root = right_view.TreeNode(1)
        root.left = right_view.TreeNode(2, right=right_view.TreeNode(5))
        root.right = right_view.TreeNode(3, right=right_view.TreeNode(4))
        self.assertEqual([1, 3, 4], right_view.right_side_view(root))
        self.assertEqual([], right_view.right_side_view(None))

    def test_construct_tree_and_deep_input(self) -> None:
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        root = construct_tree.build_tree(preorder, inorder)
        self.assertEqual(3, root.val)
        self.assertEqual(9, root.left.val)
        self.assertEqual(20, root.right.val)
        self.assertEqual(15, root.right.left.val)

        values = list(range(1_500))
        deep_root = construct_tree.build_tree(values, values)
        node = deep_root
        for value in values:
            self.assertEqual(value, node.val)
            node = node.right


class SearchDpGraphCompletionTests(unittest.TestCase):
    def test_search_matrix(self) -> None:
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(matrix_search.search_matrix(matrix, 3))
        self.assertFalse(matrix_search.search_matrix(matrix, 13))
        self.assertFalse(matrix_search.search_matrix([], 1))

    def test_koko_eating_bananas(self) -> None:
        self.assertEqual(4, koko.min_eating_speed([3, 6, 7, 11], 8))
        self.assertEqual(30, koko.min_eating_speed([30, 11, 23, 4, 20], 5))
        self.assertEqual(0, koko.min_eating_speed([], 5))

    def test_word_break(self) -> None:
        self.assertTrue(word_break_module.word_break("leetcode", ["leet", "code"]))
        self.assertTrue(word_break_module.word_break("applepenapple", ["apple", "pen"]))
        self.assertFalse(word_break_module.word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_pacific_atlantic(self) -> None:
        heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
        original = [row[:] for row in heights]
        expected = {(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)}
        self.assertEqual(expected, {tuple(cell) for cell in pacific.pacific_atlantic(heights)})
        self.assertEqual(original, heights)

    def test_minimum_spanning_tree(self) -> None:
        edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
        self.assertEqual(19, mst.minimum_spanning_tree(4, edges))
        self.assertEqual(-1, mst.minimum_spanning_tree(3, [[0, 1, 2]]))
        self.assertEqual(0, mst.minimum_spanning_tree(0, []))


if __name__ == "__main__":
    unittest.main()

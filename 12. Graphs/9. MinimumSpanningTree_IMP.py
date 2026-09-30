"""
Minimum Spanning Tree with Kruskal's Algorithm (Medium)
Source: https://cp-algorithms.com/graph/mst_kruskal_with_dsu.html

Sort edges by weight and add an edge only when it joins two different
components. Union-Find detects cycles efficiently. Return -1 if disconnected.

Time: O(E log E) | Space: O(V)
"""

from typing import List


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node: int) -> int:
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, first: int, second: int) -> bool:
        first_root = self.find(first)
        second_root = self.find(second)
        if first_root == second_root:
            return False
        if self.rank[first_root] < self.rank[second_root]:
            first_root, second_root = second_root, first_root
        self.parent[second_root] = first_root
        if self.rank[first_root] == self.rank[second_root]:
            self.rank[first_root] += 1
        return True


def minimum_spanning_tree(vertex_count: int, edges: List[List[int]]) -> int:
    if vertex_count <= 1:
        return 0

    disjoint_set = DisjointSet(vertex_count)
    total_weight = 0
    edges_used = 0
    for first, second, weight in sorted(edges, key=lambda edge: edge[2]):
        if disjoint_set.union(first, second):
            total_weight += weight
            edges_used += 1
            if edges_used == vertex_count - 1:
                return total_weight
    return -1


if __name__ == "__main__":
    sample_edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
    assert minimum_spanning_tree(4, sample_edges) == 19
    assert minimum_spanning_tree(3, [[0, 1, 2]]) == -1

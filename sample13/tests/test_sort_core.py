import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import unittest
from sort_core import (
    bubble_sort,
    quick_sort,
    merge_sort,
    insertion_sort,
    selection_sort
)


class TestSortCore(unittest.TestCase):
    """排序核心逻辑模块单元测试"""

    def setUp(self):
        self.test_cases = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 1, 2], [1, 2, 3]),
            ([5, 3, 8, 1, 9, 2], [1, 2, 3, 5, 8, 9]),
            ([1, 1, 1], [1, 1, 1]),
            ([4, 2, 4, 2], [2, 2, 4, 4]),
            ([10, -1, 0, 3, -5], [-5, -1, 0, 3, 10]),
        ]

    def _test_sort_function(self, sort_func, name):
        for input_arr, expected in self.test_cases:
            with self.subTest(case=f"{name}({input_arr})"):
                result = sort_func(input_arr)
                self.assertEqual(result, expected)
                # 验证不修改原列表
                self.assertEqual(len(input_arr), len(expected))

    def test_bubble_sort(self):
        self._test_sort_function(bubble_sort, "bubble_sort")

    def test_quick_sort(self):
        self._test_sort_function(quick_sort, "quick_sort")

    def test_merge_sort(self):
        self._test_sort_function(merge_sort, "merge_sort")

    def test_insertion_sort(self):
        self._test_sort_function(insertion_sort, "insertion_sort")

    def test_selection_sort(self):
        self._test_sort_function(selection_sort, "selection_sort")


if __name__ == '__main__':
    unittest.main()
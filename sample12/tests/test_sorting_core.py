import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import unittest
from sorting_core import generate_array, bubble_sort_steps, quick_sort_steps, get_sorted_array

class TestSortingCore(unittest.TestCase):

    def test_generate_array_default_size(self):
        arr = generate_array()
        self.assertEqual(len(arr), 30)

    def test_generate_array_custom_size(self):
        arr = generate_array(size=10)
        self.assertEqual(len(arr), 10)

    def test_generate_array_values_in_range(self):
        arr = generate_array(size=50, min_val=1, max_val=100)
        for v in arr:
            self.assertTrue(1 <= v <= 100)

    def test_bubble_sort_steps_returns_list(self):
        arr = [3, 1, 2]
        steps = bubble_sort_steps(arr)
        self.assertIsInstance(steps, list)

    def test_bubble_sort_steps_final_sorted(self):
        arr = [5, 3, 8, 1, 2]
        steps = bubble_sort_steps(arr)
        final_array = steps[-1][0]
        self.assertEqual(final_array, sorted(arr))

    def test_bubble_sort_steps_highlights(self):
        arr = [2, 1]
        steps = bubble_sort_steps(arr)
        # 至少有一个步骤有高亮
        has_highlight = any(len(h) > 0 for _, h in steps)
        self.assertTrue(has_highlight)

    def test_quick_sort_steps_returns_list(self):
        arr = [3, 1, 2]
        steps = quick_sort_steps(arr)
        self.assertIsInstance(steps, list)

    def test_quick_sort_steps_final_sorted(self):
        arr = [5, 3, 8, 1, 2]
        steps = quick_sort_steps(arr)
        final_array = steps[-1][0]
        self.assertEqual(final_array, sorted(arr))

    def test_quick_sort_steps_highlights(self):
        arr = [2, 1, 3]
        steps = quick_sort_steps(arr)
        has_highlight = any(len(h) > 0 for _, h in steps)
        self.assertTrue(has_highlight)

    def test_get_sorted_array(self):
        arr = [4, 2, 7, 1]
        sorted_arr = get_sorted_array(arr)
        self.assertEqual(sorted_arr, [1, 2, 4, 7])

    def test_get_sorted_array_does_not_mutate_original(self):
        arr = [4, 2, 7, 1]
        original = arr[:]
        get_sorted_array(arr)
        self.assertEqual(arr, original)

    def test_bubble_sort_steps_single_element(self):
        arr = [42]
        steps = bubble_sort_steps(arr)
        self.assertEqual(len(steps), 1)
        self.assertEqual(steps[0][0], [42])

    def test_quick_sort_steps_single_element(self):
        arr = [42]
        steps = quick_sort_steps(arr)
        self.assertEqual(len(steps), 1)
        self.assertEqual(steps[0][0], [42])

    def test_bubble_sort_steps_empty_array(self):
        arr = []
        steps = bubble_sort_steps(arr)
        self.assertEqual(len(steps), 1)
        self.assertEqual(steps[0][0], [])

    def test_quick_sort_steps_empty_array(self):
        arr = []
        steps = quick_sort_steps(arr)
        self.assertEqual(len(steps), 1)
        self.assertEqual(steps[0][0], [])

if __name__ == '__main__':
    unittest.main()
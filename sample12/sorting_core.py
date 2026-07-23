import random

def generate_array(size=30, min_val=1, max_val=100):
    """生成指定大小的随机整数数组"""
    return [random.randint(min_val, max_val) for _ in range(size)]

def bubble_sort_steps(arr):
    """
    冒泡排序步骤生成器
    返回一个列表，每个元素为 (array_snapshot, highlighted_indices)
    """
    a = arr[:]
    n = len(a)
    steps = []
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            steps.append((a[:], [j, j + 1]))
    steps.append((a[:], []))
    return steps

def quick_sort_steps(arr):
    """
    快速排序步骤生成器
    返回一个列表，每个元素为 (array_snapshot, highlighted_indices)
    """
    a = arr[:]
    steps = []
    def _quick_sort(low, high):
        if low < high:
            pivot_idx = _partition(low, high)
            _quick_sort(low, pivot_idx - 1)
            _quick_sort(pivot_idx + 1, high)
    def _partition(low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
            steps.append((a[:], [j, high]))
        a[i + 1], a[high] = a[high], a[i + 1]
        steps.append((a[:], [i + 1, high]))
        return i + 1
    _quick_sort(0, len(a) - 1)
    steps.append((a[:], []))
    return steps

def get_sorted_array(arr):
    """返回排序后的数组副本"""
    return sorted(arr)
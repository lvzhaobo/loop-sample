"""
排序算法核心逻辑模块（纯函数，无副作用）
所有排序函数输入一个列表，返回排序后的新列表，不修改原列表。
"""

from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """冒泡排序"""
    result = arr[:]
    n = len(result)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """快速排序"""
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def merge_sort(arr: List[int]) -> List[int]:
    """归并排序"""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insertion_sort(arr: List[int]) -> List[int]:
    """插入排序"""
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def selection_sort(arr: List[int]) -> List[int]:
    """选择排序"""
    result = arr[:]
    n = len(result)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        if min_idx != i:
            result[i], result[min_idx] = result[min_idx], result[i]
    return result
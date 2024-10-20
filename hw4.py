import random
import timeit
import matplotlib.pyplot as plt

class SortIt:  # Class for comparing of 3 sorting types
    def merge_sort(self, arr):
        if len(arr) < 2:
            return arr   # Base case of recursion
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])  # rec for left sub array
        right = self.merge_sort(arr[mid:]) # rec for right sub array
        return self._merge(left, right)
    
    def _merge(self, left, right): # private method
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def insertion_sort()
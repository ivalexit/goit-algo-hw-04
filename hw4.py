import random
import timeit
import matplotlib.pyplot as plt

class Sorter:  # Class for comparing of 3 sorting types
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
    
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    def timsort(self, arr):  
        return sorted(arr)  #  built in combined sorting method 
    
class Benchmark:  # Class for testing and time measuring 

    def __init__(self, sorter):
        self.sorter = sorter
        self.results = {
            'sizes': [],
            'merge_sort': [],
            'timsort': []
        }

    def run(self, sizes):  # Starts comparing
        for size in sizes:
            data = self._generate_data(size)
            print(f"\nTest for the array size {size}")
            self.results['sizes'].append(size)

            merge_time = self._benchmark(self.sorter.merge_sort, data)
            insertion_time = self._benchmark(self.sorter.insertion_sort, data)
            timsort_time = self._benchmark(self.sorter.timsort, data)

            self.results['merge_sort'].append(merge_time)
            self.results['insertion_sort'].append(insertion_time)
            self.results['timsort'].append(timsort_time)

            print(f"Time for merge sort: {merge_time:.6f} sec.")
            print(f"Time for insertion sort: {insertion_time:.6f} sec.")
            print(f"Time for Timsort: {timsort_time:.6f} sec.")

    def _generate_data(self, size):
        return [random.randint(0, size * 10) for _ in range(size)]
    
    def _benchmark(self, sort_func, data):
        return timeit.timeit(lambda: sort_func(data.copy()), number=10)

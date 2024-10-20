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
    
    def plot_results(self):
        sizes = self.results['sizes']
        merge_times = self.results['merge_sort']
        insertion_times = self.results['insertion_sort']
        timsort_times = self.results['timsort']

        plt.figure(figsize=(10, 6))
        plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
        plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
        plt.plot(sizes, timsort_times, label='Timsort', marker='o')

        plt.xlabel('Array size')
        plt.ylabel('Execution time (sec)')
        plt.title('Comparing of algorithm execution time')
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    sorter = Sorter()
    benchmark = Benchmark(sorter)
    sizes = [10, 100, 1000, 10000]

    print('Comparing of algorithm sorting types:\n')
    benchmark.plot_results()

if __name__ == "__main__":
    main()
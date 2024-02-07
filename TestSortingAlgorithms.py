import unittest
import random
import time

class TestSortingAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.random_data = [random.randint(0, 10000) for _ in range(3000)]
        self.sorted_data = sorted(self.random_data)
        self.reverse_sorted_data = sorted(self.random_data, reverse=True)

    def test_gnome_sort(self):
        start_time = time.time()
        sorted_data = gnome_sort(self.random_data.copy())
        elapsed_time = time.time() - start_time
        self.assertEqual(sorted_data, self.sorted_data)
        print("Gnome Sort - Tiempo de ejecución para datos desordenados:", elapsed_time)

    def test_merge_sort(self):
        start_time = time.time()
        sorted_data = merge_sort(self.random_data.copy())
        elapsed_time = time.time() - start_time
        self.assertEqual(sorted_data, self.sorted_data)
        print("Merge Sort - Tiempo de ejecución para datos desordenados:", elapsed_time)

    def test_quick_sort(self):
        start_time = time.time()
        sorted_data = quick_sort(self.random_data.copy())
        elapsed_time = time.time() - start_time
        self.assertEqual(sorted_data, self.sorted_data)
        print("Quick Sort - Tiempo de ejecución para datos desordenados:", elapsed_time)

    def test_radix_sort(self):
        start_time = time.time()
        sorted_data = radix_sort(self.random_data.copy())
        elapsed_time = time.time() - start_time
        self.assertEqual(sorted_data, self.sorted_data)
        print("Radix Sort - Tiempo de ejecución para datos desordenados:", elapsed_time)

    def test_selection_sort(self):
        start_time = time.time()
        sorted_data = selection_sort(self.random_data.copy())
        elapsed_time = time.time() - start_time
        self.assertEqual(sorted_data, self.sorted_data)
        print("Selection Sort - Tiempo de ejecución para datos desordenados:", elapsed_time)

    def test_shell_sort(self):
        start_time = time.time()
        sorted_data = shell_sort(self.random_data.copy())
        elapsed_time = time.time() - start_time
        self.assertEqual(sorted_data, self.sorted_data)
        print("Shell Sort - Tiempo de ejecución para datos desordenados:", elapsed_time)

    def test_heap_sort(self):
        start_time = time.time()
        sorted_data = heap_sort(self.random_data.copy())
        elapsed_time = time.time() - start_time
        self.assertEqual(sorted_data, self.sorted_data)
        print("Heap Sort - Tiempo de ejecución para datos desordenados:", elapsed_time)

if __name__ == '__main__':
    unittest.main()

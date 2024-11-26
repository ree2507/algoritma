import random

# bubble sort

# Generate 50 random integers (0-100) with seed 40
random.seed(40)
data = [random.randint(0, 100) for _ in range(50)]

# Naive Method: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    print("Original Data (Naive):", data)
    sorted_data = bubble_sort(data.copy())
    print("Sorted Data using Naive Method (Bubble Sort):", sorted_data)

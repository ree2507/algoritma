import random

# Generate 50 random integers (0-100) with seed 40
random.seed(40)
data = [random.randint(0, 100) for _ in range(50)]

# Conquer Method: Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
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

if __name__ == "__main__":
    print("Original Data (Conquer):", data)
    sorted_data = merge_sort(data.copy())
    print("Sorted Data using Conquer Method (Merge Sort):", sorted_data)

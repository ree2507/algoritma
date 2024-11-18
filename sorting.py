# Reyhan Dany_F55123095
# Kelas: TI C

import time

# Bubble Sort Function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Quick Sort Function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Main Program
A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
B = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]

# Bubble Sort - List A
start_time = time.time()
sorted_A_bubble = bubble_sort(A.copy())
bubble_sort_time_A = time.time() - start_time

# Bubble Sort - List B
start_time = time.time()
sorted_B_bubble = bubble_sort(B.copy())
bubble_sort_time_B = time.time() - start_time

# Quick Sort - List A
start_time = time.time()
sorted_A_quick = quick_sort(A.copy())
quick_sort_time_A = time.time() - start_time

# Quick Sort - List B
start_time = time.time()
sorted_B_quick = quick_sort(B.copy())
quick_sort_time_B = time.time() - start_time

# Print Results
print("Sorted List using Bubble Sort:")
print(f"List A: {sorted_A_bubble}")
print(f"List B: {sorted_B_bubble}")
print("\nSorted List using Quick Sort:")
print(f"List A: {sorted_A_quick}")
print(f"List B: {sorted_B_quick}")

print("\nTime taken for Bubble Sort:")
print(f"List A: {bubble_sort_time_A:.6f} seconds")
print(f"List B: {bubble_sort_time_B:.6f} seconds")
print("\nTime taken for Quick Sort:")
print(f"List A: {quick_sort_time_A:.6f} seconds")
print(f"List B: {quick_sort_time_B:.6f} seconds")

# Compare Effectiveness
print("\nComparison:")
if bubble_sort_time_A < quick_sort_time_A:
    print("Bubble Sort is faster for List A.")
else:
    print("Quick Sort is faster for List A.")

if bubble_sort_time_B < quick_sort_time_B:
    print("Bubble Sort is faster for List B.")
else:
    print("Quick Sort is faster for List B.")

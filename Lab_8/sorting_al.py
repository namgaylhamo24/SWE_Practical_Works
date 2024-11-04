# Step 1: Implement Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)

# Step 2: Implement Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
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

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)

# Step 3: Implement Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)

# Step 4: Compare Performance
import time
import random

def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]

# Compare the algorithms
compare_sorting_algorithms(large_arr)

# Exercises
# Q1: Implement an in-place version of Quick Sort to improve its space efficiency.
def quick_sort_in_place(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Testing in-place quick sort
test_arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort_in_place(test_arr, 0, len(test_arr) - 1)
print("In-Place Quick Sort Result:", test_arr)

# Q2: Modify Bubble Sort to stop early if the list becomes sorted before all passes are complete.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Flag to check if a swap occurred in this pass
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they're in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # A swap occurred
        if not swapped:  # If no swaps happened, the list is already sorted
            break
    return arr

# Q3: Implement a hybrid sorting algorithm that uses Insertion Sort for small subarrays in Merge Sort or Quick Sort.
THRESHOLD = 10

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_merge_sort(arr, left, right):
    if right - left + 1 <= THRESHOLD:
        insertion_sort(arr, left, right)
    else:
        if left < right:
            mid = (left + right) // 2
            hybrid_merge_sort(arr, left, mid)
            hybrid_merge_sort(arr, mid + 1, right)
            merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    left_sub = arr[left:mid + 1]
    right_sub = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] <= right_sub[j]:
            arr[k] = left_sub[i]
            i += 1
        else:
            arr[k] = right_sub[j]
            j += 1
        k += 1
    
    while i < len(left_sub):
        arr[k] = left_sub[i]
        i += 1
        k += 1
    
    while j < len(right_sub):
        arr[k] = right_sub[j]
        j += 1
        k += 1

# Testing the Hybrid Merge Sort
test_arr = [64, 34, 25, 12, 22, 11, 90]
hybrid_merge_sort(test_arr, 0, len(test_arr) - 1)
print("Hybrid Merge Sort Result:", test_arr)

# Q4: Create a visualization of how each sorting algorithm works using a library like Matplotlib.

import matplotlib.pyplot as plt
import numpy as np
import random

# Function to visualize the sorting process
def visualize_sort(arr, algorithm_name):
    plt.figure(figsize=(10, 5))
    plt.title(f'{algorithm_name} Visualization')
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.pause(0.5)  

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            visualize_sort(arr, "Bubble Sort")
        if not swapped:
            break
    plt.show()

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            visualize_sort(arr, "Merge Sort")

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            visualize_sort(arr, "Merge Sort")

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            visualize_sort(arr, "Merge Sort")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        visualize_sort(arr, "Quick Sort")
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Function to generate a random array and visualize the sorting
def sort_and_visualize(algorithm):
    arr = [random.randint(1, 100) for _ in range(10)] 
    print(f'Original Array: {arr}')
    
    if algorithm == 'bubble':
        bubble_sort(arr.copy())
    elif algorithm == 'merge':
        visualize_sort(arr.copy(), "Merge Sort")
        merge_sort(arr.copy())
        plt.show()
    elif algorithm == 'quick':
        arr = quick_sort(arr.copy())
        visualize_sort(arr, "Quick Sort")
        plt.show()

# Sort and visualize each algorithm
sort_and_visualize('bubble')
sort_and_visualize('merge')
sort_and_visualize('quick')

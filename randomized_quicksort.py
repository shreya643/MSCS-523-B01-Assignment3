import random
import time


def iterative_randomized_quicksort(arr):
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = randomized_partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def iterative_deterministic_quicksort(arr):
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = deterministic_partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

def deterministic_partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

def compare_iterative_algorithms():
    test_cases = {
        "Random Array": [random.randint(0, 1000) for _ in range(1000)],
        "Sorted Array": list(range(1000)),
        "Reverse Sorted Array": list(range(1000, 0, -1)),
        "Array with Repeated Elements": [5] * 1000 + [10] * 500 + [1] * 500
    }

    for name, arr in test_cases.items():
        arr_randomized = arr[:]
        arr_deterministic = arr[:]

        start_time = time.time()
        iterative_randomized_quicksort(arr_randomized)
        randomized_duration = time.time() - start_time


        start_time = time.time()
        iterative_deterministic_quicksort(arr_deterministic)
        deterministic_duration = time.time() - start_time

        # Print results
        print(f"{name}:")
        print(f"  Iterative Randomized Quicksort time: {randomized_duration:.5f} seconds")
        print(f"  Iterative Deterministic Quicksort time: {deterministic_duration:.5f} seconds")
        print()
 
# Run the comparison
compare_iterative_algorithms()

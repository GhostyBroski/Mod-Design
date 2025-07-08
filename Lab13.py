# 1. Name:
#      Ash Jones
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      This is supposed to take an array of data, sorting it via a segregation sort recursively.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part had to be handling the end case, as well as making sure the pivot doesn't get lost or critically impacted by the recursive process. Thankfully, I was able to devise how this works for both. By switching indexes for the pivot in the appropriate places and looking for the right information, such as all(sorted_flags[left:right + 1]).
# 5. How long did it take for you to complete the assignment?
#      2 hrs 10 mins

def segregation_sort(arr):
    n = len(arr)
    sorted_flags = [False] * n

    print(arr)  # Initial display
    recursive_segregation_sort(arr, 0, n - 1, sorted_flags)

def recursive_segregation_sort(arr, left, right, sorted_flags):
    if left >= right or all(sorted_flags[left:right + 1]):
        return

    pivot_index = (left + right) // 2
    pivot_value = arr[pivot_index]
    up = left
    down = right

    while up <= down:
        while up <= right and (arr[up] <= pivot_value or sorted_flags[up]):
            up += 1
        while down >= left and (arr[down] >= pivot_value or sorted_flags[down]):
            down -= 1

        if up < down:
            arr[up], arr[down] = arr[down], arr[up]
            up += 1
            down -= 1
            print(arr)

    # Adjust pivot if it ended up out of order
    if pivot_index <= down and arr[pivot_index] > arr[down]:
        arr[pivot_index], arr[down] = arr[down], arr[pivot_index]
        print(arr)
        pivot_index = down
    elif pivot_index >= up and arr[pivot_index] < arr[up]:
        arr[pivot_index], arr[up] = arr[up], arr[pivot_index]
        print(arr)
        pivot_index = up

    mark_ordered(arr, sorted_flags, left, right)

    recursive_segregation_sort(arr, left, pivot_index - 1, sorted_flags)
    recursive_segregation_sort(arr, pivot_index + 1, right, sorted_flags)

def mark_ordered(arr, sorted_flags, start, end):
    for i in range(start, end + 1):
        left_ok = i == 0 or arr[i - 1] <= arr[i]
        right_ok = i == len(arr) - 1 or arr[i] <= arr[i + 1]
        if left_ok and right_ok:
            sorted_flags[i] = True

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def test_driver():
    test_cases = [
        {"input": None, "expected": "Error: Nothing to Sort"},
        {"input": [], "expected": "Error: Nothing to Sort"},
        {"input": [1, 3, 5], "expected": "Error: Already Sorted"},
        {"input": [1, 5, 3], "expected": [1, 3, 5]},
        {"input": [4, 7, 2, 5, 8], "expected": [2, 4, 5, 7, 8]},
        {"input": [2, 22, 5, 7, 9, 10, 8, 6, 110, 64], "expected": [2, 5, 6, 7, 8, 9, 10, 22, 64, 110]},
    ]

    for idx, case in enumerate(test_cases, 1):
        arr = case["input"]
        expected = case["expected"]

        print(f"\nTest Case {idx}:")

        if arr is None or arr == []:
            print("Error: Nothing to Sort" if expected == "Error: Nothing to Sort" else "❌ Unexpected result")
            continue

        if is_sorted(arr):
            print("Error: Already Sorted" if expected == "Error: Already Sorted" else "❌ Unexpected result")
            continue

        test_arr = arr.copy()
        segregation_sort(test_arr)

        if test_arr == expected:
            print("✅ Passed!")
        else:
            print("❌ Failed. Got:", test_arr)
            print("Expected:", expected)

test_driver()
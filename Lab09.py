# 1. Name:
#      Ash Jones
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This program is meant to take an array and sort it via merging and copying sub-lists from an original arra to a destinary array in order. This means it keeps track of the 'runs', being sub-lists that go from lowest to greatest, merging and placing them in the appropriate indexes they need to be in for the destination array.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out the syntax since I understood it conceptually, but not practically. By this, I mean to say that I got lost in all the different parameters I made that tracked the various places I was referencing and sending information, kept track of the starts and ends of the 2 runs that are relevant for merging and copying, and so on. Thankfully, after finaggling with it enough, I was able to find a way for it to move along through the array smoothly so that I grabbed and counted runs accurately.
# 5. How long did it take for you to complete the assignment?
#      2hrs 18mins

def find_run_end(arr, start_idx):
    """Finds the end index of a naturally sorted sublist (run) starting from start_idx."""
    end_idx = start_idx
    while end_idx + 1 < len(arr) and arr[end_idx] <= arr[end_idx + 1]:
        end_idx += 1
    return end_idx

def merge_and_copy(src, dest, run1_start, run1_end, run2_start, run2_end, dest_start):
    """Merges two sorted runs from src into dest."""
    ptr1, ptr2, dest_ptr = run1_start, run2_start, dest_start
    
    while ptr1 <= run1_end and ptr2 <= run2_end:
        if src[ptr1] <= src[ptr2]:
            dest[dest_ptr] = src[ptr1]
            ptr1 += 1
        else:
            dest[dest_ptr] = src[ptr2]
            ptr2 += 1
        dest_ptr += 1

    while ptr1 <= run1_end:
        dest[dest_ptr] = src[ptr1]
        ptr1 += 1
        dest_ptr += 1

    while ptr2 <= run2_end:
        dest[dest_ptr] = src[ptr2]
        ptr2 += 1
        dest_ptr += 1

def copy_run(src, dest, run_start, run_end, dest_start):
    """Copies a single run directly from src to dest."""
    for i in range(run_start, run_end + 1):
        dest[dest_start] = src[i]
        dest_start += 1

def sublist_sort(input_array):
    """Sorts an array using sublist sorting approach."""
    if len(input_array) <= 1:
        return input_array  # Already sorted if size is 0 or 1

    source_array = input_array[:]
    destination_array = [0] * len(input_array)

    while True:
        num_runs_in_round = 0
        read_idx, write_idx = 0, 0

        while read_idx < len(source_array):
            run1_start = read_idx
            run1_end = find_run_end(source_array, run1_start)
            read_idx = run1_end + 1
            num_runs_in_round += 1

            if read_idx < len(source_array):
                run2_start = read_idx
                run2_end = find_run_end(source_array, run2_start)
                read_idx = run2_end + 1
                num_runs_in_round += 1

                merge_and_copy(source_array, destination_array, run1_start, run1_end, run2_start, run2_end, write_idx)
                write_idx += (run1_end - run1_start + 1) + (run2_end - run2_start + 1)
            else:
                copy_run(source_array, destination_array, run1_start, run1_end, write_idx)
                write_idx += (run1_end - run1_start + 1)

        if num_runs_in_round == 1:
            break  # Fully sorted

        source_array, destination_array = destination_array, source_array

    return source_array

def count_runs(arr):
    """Counts the number of naturally sorted runs in an array."""
    if not arr:
        return 0

    run_count = 0
    i = 0
    while i < len(arr):
        run_end = find_run_end(arr, i)
        run_count += 1
        i = run_end + 1  # Move to the next possible run
    return run_count

def run_test(name, input_array, expected_output, expected_run_count=None):
    """Runs a single test case and prints results."""
    print(f"\n--- Test: {name} ---")
    print(f"Input: {input_array}")

    if len(input_array) > 1 and expected_run_count is not None:
        actual_run_count = count_runs(input_array)
        print(f"Expected Runs: {expected_run_count}, Actual Runs: {actual_run_count}")
        if actual_run_count != expected_run_count:
            print("❌ Run count mismatch")
        else:
            print("✅ Run count matches")

    result = sublist_sort(input_array)

    print(f"Expected Output: {expected_output}")
    print(f"Actual Output  : {result}")

    if result == expected_output:
        print("✅ Test Passed")
    else:
        print("❌ Test Failed")

# ----------- Running the Updated Test Cases ------------ #

run_test(
    name="Empty",
    input_array=[],
    expected_output=[]  # Updated to match function behavior
)

run_test(
    name="Already Sorted",
    input_array=[7],
    expected_output=[7]
)

run_test(
    name="Small Array",
    input_array=[1, 3, 2, 4, 5],
    expected_output=[1, 2, 3, 4, 5],
    expected_run_count=2
)

run_test(
    name="Medium Array",
    input_array=[1, 5, 6, 2, 7, 8, 9, 10, 4, 11, 12, 3, 15, 14, 13],
    expected_output=list(range(1, 16)),
    expected_run_count=6
)

run_test(
    name="Large Array",
    input_array=[1, 2, 3, 4, 5, 6, 7, 10, 9, 8, 11, 12, 19, 18, 20, 22,
                 14, 15, 13, 16, 17, 26, 21, 23, 24, 25, 30, 29, 27, 28],
    expected_output=list(range(1, 31)),
    expected_run_count=9
)
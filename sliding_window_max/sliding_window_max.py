'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    arr = nums
    return_arr = []
    n = len(arr)
    start = 0
    end = start + k
    while end <= n:
        current_arr = arr[start:end]
        return_arr.append(max(current_arr))
        start += 1
        end += 1
    return return_arr

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

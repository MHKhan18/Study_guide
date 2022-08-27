from typing import List


def merge_sort(array: List[int]) -> None:
    temp_array = [None] * len(array)
    merge_sort_util(array, temp_array, 0, len(array) - 1)


def merge_sort_util(
    array: List[int], temp_array: List[int], left_start: int, right_end: int
) -> None:

    if left_start >= right_end:
        return

    mid = (left_start + right_end) // 2
    merge_sort_util(array, temp_array, left_start, mid)
    merge_sort_util(array, temp_array, mid + 1, right_end)
    merge_halves(array, temp_array, left_start, right_end)


def merge_halves(
    array: List[int], temp_array: List[int], left_start: int, right_end: int
) -> None:

    left_end = (left_start + right_end) / 2
    right_start = left_end + 1

    left = left_start
    right = right_start
    index = left_start

    while left <= left_end and right <= right_end:
        if array[left] <= array[right]:
            temp_array[index] = array[left]
            left += 1
        else:
            temp_array[index] = array[right]
            right += 1

        index += 1

    while left <= left_end:
        temp_array[index] = array[left]
        index += 1
        left += 1

    while right <= right_end:
        temp_array[index] = array[right]
        index += 1
        right += 1

    for i in range(left_start, right_end + 1):
        array[i] = temp_array[i]

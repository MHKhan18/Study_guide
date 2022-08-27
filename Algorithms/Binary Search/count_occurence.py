from typing import List

from find_occurence import find_occurence


def count(nums: List[int], target: int):
    """
    nums : sorted list of int, can contain duplicates
    return: count of target in nums if exists, else -1
    runtime: O(log n)
    """

    first_index = find_occurence(nums, target, first=True)
    last_index = find_occurence(nums, target, last=True)

    if first_index > -1:
        return last_index - first_index + 1
    return -1


if __name__ == "__main__":

    nums = [2, 4, 10, 10, 10, 18, 20]

    print(count(nums, 10))
    print(count(nums, 9))

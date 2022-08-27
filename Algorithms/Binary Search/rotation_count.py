
from typing import List


def rotation_count(nums: List[int]) -> int:

    low, high = 0, len(nums)-1

    while low <= high:

        if nums[low] <= nums[high]:
            return low

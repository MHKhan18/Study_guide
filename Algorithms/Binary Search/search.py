
from typing import List

def binary_search(nums: List[int] , target: int):
    '''
        nums : sorted list of int
        return: index of target in nums if exists, else -1 
        runtime: O(log n)
    '''
    
    start , end = 0 , len(nums)-1

    while start <= end:

        mid = start + (end - start) // 2

        if target == nums[mid]:
            return mid 
        
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1

    
    return -1

if __name__ == "__main__":

    nums = [2 , 4, 10 , 18 , 20]

    print(binary_search(nums , 10))
    print(binary_search(nums , 9))
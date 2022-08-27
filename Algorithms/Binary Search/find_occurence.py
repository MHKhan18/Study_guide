from typing import List

def find_occurence(nums: List[int] , target: int , first = False , last = False):
    '''
        nums : sorted list of int that can contain duplicates
        return: first/last index of target in nums if exists, else -1 
        runtime: O(log n)
    '''
    result = -1
    start , end = 0 , len(nums)-1

    while start <= end:

        mid = start + (end - start) // 2

        if target == nums[mid]:
            result = mid
            if first: 
                end = mid - 1
            elif last:
                start = mid + 1
            else:
                return result
        
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1

    
    return result

if __name__ == "__main__":

    nums = [2 , 4, 10 , 10 , 10, 18 , 20]

    print(find_occurence(nums , 10 , first = True))
    print(find_occurence(nums , 10 , last = True))
    print(find_occurence(nums , 9 , first = True))
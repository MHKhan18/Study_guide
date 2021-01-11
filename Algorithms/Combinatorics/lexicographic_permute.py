
def next_permutation(nums):

    nums = list(nums)
    n = len(nums)

    def swap(i , j):
        nums[i] , nums[j] = nums[j] , nums[i]

    def reverse(s , e):
        while s < e:
            swap(s , e)
            s += 1
            e -= 1
    
    # decreasing sequence starts at k+1
    k = n-2
    while k >= 0 and nums[k] >= nums[k+1]:
        k -= 1
    
    if k < 0: # nums is decreasing
        return [] # no next permute possible

    # nums[j] is smallest number > nums[k] 
    j = n-1
    while nums[j] <= nums[k]:
        j -= 1
    
    swap(j , k)
    reverse(k+1 , n-1)

    return nums

def lexicographic_permute(nums):

    res = []
    nums.sort()
    res.append(nums)

    _next = next_permutation(nums)

    while _next != []:
        res.append(_next)
        _next = next_permutation(_next)

    return res



if __name__ == "__main__":
    arr1 = [1,2,3]
    print(lexicographic_permute(arr1))



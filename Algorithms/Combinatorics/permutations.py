
# number of permutations of |arr| == n: n!

import json 

def get_permutations(arr):
    res = []
    def directed_permutations(curr_i , curr_arr):  #O(n!)
        if curr_i == len(curr_arr)-1:
            res.append(str(curr_arr))  # list of lists require deep copy 
            return None
        for j in range(curr_i , len(curr_arr)):   # each element at first position
            curr_arr[curr_i] , curr_arr[j] = curr_arr[j] , curr_arr[curr_i]
            directed_permutations(curr_i+1 , curr_arr)
            curr_arr[curr_i] , curr_arr[j] = curr_arr[j] , curr_arr[curr_i] #backtrack
    
    directed_permutations(0 , arr)
    final_res = []
    for perm_str in res:
        final_res.append(json.loads(perm_str))
    return final_res

    

def main():
    lst = [7,3,5]
    permutations = get_permutations(lst)
    print(permutations)
   
main()



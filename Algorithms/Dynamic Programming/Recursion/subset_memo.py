'''
Created on Oct 4, 2017

@author: Brian Borowski

CS115 - Multiple ways to work with the subset sum problem
'''
import time

def subset(target, lst):
    '''Determines whether or not it is possible to create target sum using the
    values in the list. Values in list can be positive, negative, or zero.'''
    if target == 0:
        return True
    if lst == []:
        return False
    # return use_it or lose_it
    return subset(target - lst[0], lst[1:]) or subset(target, lst[1:])

def subset_memo_wrong(target, lst):
    '''Determines whether or not it is possible to create target sum using the
    values in the list. Values in list can be positive, negative, or zero.
    This is not the best way to memoize, since creating tuple slices is slow
    and memory-intensive.'''
    def subset_helper(target, tup, memo):
        if (target, tup) in memo:
            return memo[(target, tup)]

        if target == 0:
            result = True
        elif tup == ():
            result = False
        else:
            result = subset_helper(target - tup[0], tup[1:], memo) or \
                     subset_helper(target, tup[1:], memo)

        memo[(target, tup)] = result
        return result

    return subset_helper(target, tuple(lst), {})

def subset_memo(target, lst):
    '''Determines whether or not it is possible to create target sum using the
    values in the list. Values in list can be positive, negative, or zero.
    This is a better way to memoize, since the key is simply a tuple of two
    integers.'''
    last = len(lst) - 1
    def subset_helper(target, current, memo):
        if (target, current) in memo:
            return memo[(target, current)]

        if target == 0:
            result = True
        elif current > last:
            result = False
        else:
            result = subset_helper(target - lst[current], current + 1, memo) \
                  or subset_helper(target, current + 1, memo)

        memo[(target, current)] = result
        return result

    return subset_helper(target, 0, {})

def subset_with_values_memo(target, lst):
    '''Determines whether or not it is possible to create the target sum
    using values in the list. Values in the list can be positive, negative, or
    zero. The function returns a tuple of exactly two items. The first is a
    Boolean that indicates True if the sum is possible and False if it's not.
    The second element in the tuple is a list of all the values that add up
    to make the target sum.
    This function builds upon the basic memoized version, adding the ability
    to see what values add up to the target sum. The time to build the list
    of values is minimal.'''
    last = len(lst) - 1
    def subset_helper(target, current, memo):
        if (target, current) in memo:
            return memo[(target, current)]

        if target == 0:
            result = (True, [])
        elif current > last:
            result = (False, [])
        else:
            use_it = subset_helper(target - lst[current], current + 1, memo)
            if use_it[0]:
                result = (True, [lst[current]] + use_it[1])
            else:
                result = subset_helper(target, current + 1, memo)

        memo[(target, current)] = result
        return result
    return subset_helper(target, 0, {})



if __name__ == '__main__':
    start_time = time.time()
    print(subset(1000, list(range(24))))
    print('Computation time without memoization:', time.time() - start_time,
          'seconds')

    start_time = time.time()
    print(subset_memo_wrong(100000, list(range(550))))
    print('Computation time with memoization implemented poorly:',
          time.time() - start_time, 'seconds')

    start_time = time.time()
    print(subset_memo(100000, list(range(550))))
    print('Computation time with memoization:', time.time() - start_time,
          'seconds')

    start_time = time.time()
    print(subset_with_values_memo(100000, list(range(550))))
    print('Computation time with memoization:', time.time() - start_time,
          'seconds')

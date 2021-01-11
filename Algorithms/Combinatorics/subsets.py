
# number of subsets of set len n: 2^n
# BRGC -> Binary Reflected Gray Code
# one to one mapping from 2^n bit strings and subsets 

# using decrease by one approach
def powerset(lst):
    '''Returns the power set of the list, that is, the set of all subsets of the list.'''
    if lst == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]]+subset , lose_it)
    return lose_it + list(use_it)


def BRGC_rec(n):
    
    if n <= 0:
        return ["0"]
    
    if n == 1:
        return ["0" , "1"]

    l1 = BRGC_rec(n-1)

    res = []

    for code in l1:
        res.append("0" + code)

    for i in range(len(l1)-1 , -1 , -1): # reverse of l1
        code = l1[i]
        res.append("1" + code)

    return res


def BRGC_iter(n):

    if n <= 0:
        return []

    res = ["0" , "1"] # start with 1 bit pattern

    i = 2
    while i < (1 << n) : # each iteration generates 2i codes from i codes

        for j in range(i-1 , -1 , -1):
            res.append(res[j])
        
        for j in range(i):
            res[j] = "0" + res[j]

        for j in range(i , 2*i):
            res[j] = "1" + res[j]

        i <<= 1

    return res



if __name__ == "__main__":
    print(powerset([1,2,3]))
    print(BRGC_rec(3))
    print(BRGC_iter(3))
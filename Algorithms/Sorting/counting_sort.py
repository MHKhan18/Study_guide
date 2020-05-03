
def counting_sort(array, range_begin, range_end):
    
    working_array = []
    result_array = []

    for i in range(range_begin,range_end+1):
        working_array.append(0)
    
    for i in range(len(array)):
        result_array.append(0)
    
    for i in range(len(array)):
        working_array[array[i]] += 1
    # working_array[i] now contains the number of elements equal to i

    for i in range(1,len(working_array)):
        working_array[i] += working_array[i-1]
    # working_array[i] now contains the number of elements less than or equal to i

    for i in range(len(array)-1,-1,-1): # tranverse high to low to make stable sort
        result_array[working_array[array[i]]-1] = array[i]
        working_array[array[i]] -= 1

    #copy result into orignal
    for i in range(len(array)):
        array[i] = result_array[i]


tst = [2,5,3,0,2,3,0,3]
counting_sort(tst,0,5)
print(tst)

    



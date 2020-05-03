
''' Implements quicksort with Lumotou partition and last element as pivot
    Average-case running time : O(nlog n)
    Worst-case running time: O(n^2)
    In-place sorting'''


def quicksort(array,left,right):

    if left < right:
        q = partition(array,left,right)
        quicksort(array,left,q-1)
        quicksort(array,q+1,right)


def partition(array,left,right):
    
    pivot = array[right]
    less = left - 1
    for greater in range(left,right):
        if array[greater] <= pivot:
            less += 1
            swap(array,less,greater)
    
    swap(array,right,less+1)
    return less + 1


def swap(arr,i,j): # O(1)
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

tst = [2,8,7,1,3,5,6,4]
right = len(tst)-1
partition(tst,0,right)
print(tst)
quicksort(tst,0,right)
print(tst)




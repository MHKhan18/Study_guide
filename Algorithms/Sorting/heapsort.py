
def swap(arr,i,j): # O(1)
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def max_heapify(array,i,heap_size): # O(lgn)
    ''' Assuming both left subtree and right subtree are max heaps,
        restores the max heap property at index i '''
    
    left_child = 2*i + 1
    right_child = 2*i + 2

    if left_child < heap_size and array[left_child] > array[i]:
        largest = left_child
    else:
        largest = i

    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child
    
    if largest != i:
        swap(array,i,largest)
        max_heapify(array,largest,heap_size)


def build_max_heap(arr): # O(n)
    ''' Given an unordered array, builds a max heap
        Leaf nodes are max heaps [n/2] are leaf nodes'''
    heap_size = len(arr)
    internal_node = len(arr)//2 - 1
    for i in range(internal_node, -1, -1):
        max_heapify(arr,i,heap_size)


def heapsort(array):
    '''O(log n), in-place sorting algorithm'''
    build_max_heap(array)
    heap_size = len(array)
    for i in range(len(array)-1,0,-1):
        swap(array,0,i)
        heap_size -= 1
        max_heapify(array,0,heap_size)

# tst = [5,13,2,25,7,17,20,8,4]
# tst = [4,1,3,2,16,9,10,14,8,7]
# heapsort(tst)
# print(tst)


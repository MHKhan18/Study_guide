
class PriorityQueue():
    '''
        Elements are (node , key) tuple
        key is a number (distance)
        node is a capital English alphabet
        Assumption: all node are unique
    '''

    def __init__(self):
        self.heap = []
        self.node_index = {} #.node_indexs (node,key) to index in heap list
        self.n = 0 # num items in pq


    def __swap(self, index1 , index2):
        
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

        self.node_index[self.heap[index1]] = index1
        self.node_index[self.heap[index2]] = index2

    @staticmethod
    def __is_less(item1 , item2):

        return item1[1] < item2[1]

        
    def insert(self , item):
        '''Add a new element to the set.'''

        self.n += 1
        self.heap.append(item)  # place at the end
        self.node_index[self.heap[self.n - 1]] = self.n-1


        # fix order -- swim up

        child = self.n - 1
        parent = (child-1) // 2 
        
        while parent >= 0:

            parent_val = self.heap[parent]
            child_val = self.heap[child]
            
            if not PriorityQueue.__is_less(parent_val , child_val):
                self.__swap(parent , child)
                child = parent
                parent = (child - 1) // 2

            else: # min heap property is already in place up from this point
                break 



    def decrease_key(self , old_item , new_item):
        # swaps (node , prev_key) with (node , new_key) and restores heap invariant
        # assumption : new_key < prev_key

        cur_index = self.node_index[old_item]
        self.heap[cur_index] = new_item

        self.node_index.pop(old_item)
        self.node_index[self.heap[cur_index]] = cur_index

        # fix order -- swim up

        child = cur_index
        parent = (child-1) // 2 
        
        while parent >= 0:

            parent_val = self.heap[parent]
            child_val = self.heap[child]
            
            if not PriorityQueue.__is_less(parent_val , child_val):
                self.__swap(parent , child)
                child = parent
                parent = (child - 1) // 2

            else: # min heap property is already in place up from this point
                break 


    def delete_min(self):
        '''Return the element with the smallest key, and remove it from the set'''
      
        if self.n <= 0:
            return None
        
        result = self.heap[0]

        if self.n == 1:
            last = self.heap.pop()
            self.node_index.pop(last)
            self.node_index[last] = 0
            self.n -= 1
            return result
        
        last = self.heap.pop()
        self.node_index.pop(last)
        self.node_index[last] = 0
        self.n -= 1
        self.heap[0] = last

        # restore min heap invariant
        parent = 0

        while True:

            left_child = (2 * parent) + 1

            if left_child >= self.n:
                break # no next level
            
            right_child = left_child + 1
            
            # select min of left and right child
            min_child = left_child

            if right_child < self.n and PriorityQueue.__is_less(self.heap[right_child] , self.heap[left_child]):
                min_child = right_child

            # swim down
            if not PriorityQueue.__is_less(self.heap[parent] , self.heap[min_child]):
                self.__swap(parent , min_child)
                parent = min_child
            else:
                break # heap property is restored
        
        return result

    def get_size(self):

        return self.n



if __name__ == "__main__":

    pq1 = PriorityQueue()

    pq1.insert(('A' , 500))
    pq1.insert(('B' , 400))
    pq1.insert(('C' , 350))
    pq1.insert(('D' , 300))
    pq1.insert(('E' , 250))
    pq1.insert(('F' , 600))

    arr = pq1.heap
    print(arr)
    print(pq1.node_index)

    pq1.decrease_key(('F' , 600) , ('F' , 100))
    arr2 = pq1.heap
    print(arr2)
    print(pq1.node_index)

    for _ in range(6):
        print(pq1.delete_min())

    if pq1:
        print("hello!!")
    else:
        print("coercion woks")

    print(pq1.get_size())

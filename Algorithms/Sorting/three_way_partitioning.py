def partition(array, pivot_index):
    """partitions array into less than, equal to and greater than pivot element in-place"""

    pivot = array[pivot_index]

    # forward pass
    smaller = 0
    for i, num in enumerate(array):
        if num < pivot:
            array[i], array[smaller] = array[smaller], array[i]
            smaller += 1

    # backward pass
    larger = len(array) - 1
    for i in range(len(array) - 1, -1, -1):
        num = array[i]
        if num > pivot:
            array[i], array[larger] = array[larger], array[i]
            larger -= 1


if __name__ == "__main__":
    A = [0, 1, 2, 0, 2, 1, 1]
    partition(A, 1)
    print(A)

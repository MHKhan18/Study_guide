import math

# precondition:  0 <= arr[i] < 1
def bucket_sort(A):

    n = len(A)

    B = []
    for i in range(n):
        B.append([])

    # put each number into a bucket
    for i in range(n):
        B[math.floor(n * A[i])].append(A[i])

    # sort each bucket
    for i in range(n):
        B[i].sort()

    # concatenate the buckets
    j = 0
    for i in range(n):
        for num in B[i]:
            A[j] = num
            j += 1


if __name__ == "__main__":
    A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    bucket_sort(A)
    print(A)

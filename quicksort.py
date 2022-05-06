def partition(A, p, r):
    i = (p-1)
    pivot = A[r]

    for j in range(p, r):
        if A[j] <= pivot:

            i = i+1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]

    print("After next pass: ", end="")
    print(*A)
    return (i+1)


def quicksort(A, p, r):

    if len(A) == 1:

        return A

    if p < r:
        pi = partition(A, p, r)

        quicksort(A, p, pi-1)
        quicksort(A, pi+1, r)


A = [25, 32, 40, 17, 21, 45, 30, 28]
n = len(A)
quicksort(A, 0, n-1)

print("Sorted Array : ")
for i in range(n):
    print("%d" % A[i])

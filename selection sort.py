# Insertion sort
def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        print(f"After pass {i}: ", end=" ")
        print(*A)


# Selection sort

def selectionsort(A):
    for i in range(len(A)):
        min = A[i]
        pos = i

        for j in range(i, len(A)):
            if A[j] < min:
                pos = j
                min = A[j]

        # Swap
        A[i], A[pos] = A[pos], A[i]

        print(f"After pass {i + 1}: ", end=" ")
        print(*A)


print("\nEnter 1 for Insertion Sort\nEnter 2 for Selection Sort\n")
choice = int(input("Enter your choice: "))
A = list(map(int, input("\nEnter the Array: ").split()))
if choice == 1:
    print()
    insertionSort(A)
else:
    print()
    selectionsort(A)

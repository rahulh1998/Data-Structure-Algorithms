def helper(A, start, end):
    if start == end:
        return

    mid = (start + end) // 2

    # Sort left half
    helper(A, start, mid)
    # Sort right half
    helper(A, mid + 1, end)

    i = start
    j = mid + 1
    aux = []

    # Merge step
    while i <= mid and j <= end:
        if A[i] <= A[j]:
            aux.append(A[i])
            i += 1
        else:
            aux.append(A[j])
            j += 1

    # Copy remaining left half
    while i <= mid:
        aux.append(A[i])
        i += 1

    # Copy remaining right half
    while j <= end:
        aux.append(A[j])
        j += 1

    # Copy back to original array
    A[start:end+1] = aux


def MergeSort(A):
    if not A:
        return []
    helper(A, 0, len(A) - 1)
    return A


print(MergeSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

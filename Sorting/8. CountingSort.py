def counting_sort(arr):
    n = len(arr)
    min_element = arr[0]
    max_element = arr[0]
    frequency = {}

    for i in range(0, n):
        if arr[i] not in frequency:
            frequency[arr[i]] = 1
        else:
            frequency[arr[i]] += 1

    min_element = min(arr)
    max_element = max(arr)

    arr_index = 0
    for i in range(min_element, max_element + 1):
        if i in frequency:
            current_frequency = frequency[i];
            while current_frequency > 0:
                arr[arr_index] = i
                arr_index += 1
                current_frequency -= 1

    return arr

print(counting_sort([5,4,3,2,1]))
def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i = i + 1
        else: 
            sorted.append(right[j])
            j = j + 1
        sorted.extend(left[i:])
        sorted.extend(right[j:])
        return sorted


def selection_sort(item):
    for i in range(len(item)):
        min_index = i
        for j in range(i + 1, len(item)):
            if item[j] < item[min_index]:
                min_index = j
        if min_index != i:
            item[i], item[min_index] = item[min_index], item[i]
    return item
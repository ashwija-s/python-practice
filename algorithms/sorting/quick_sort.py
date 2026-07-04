def quick_sort(int_list):
    if not int_list:
        return []
    if len(int_list) <= 1:
        return int_list
    piv = int_list[0]
    l1 = []
    l2 = []
    l3 = []
    for i in int_list:
        if i < piv:
            l1.append(i)
        elif i == piv:
            l2.append(i)
        else:
            l3.append(i)
    s1 = quick_sort(l1)
    s3 = quick_sort(l3)
    return s1 + l2 + s3
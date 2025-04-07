def can_be_nested(list1, list2):
    min1 = list1[0]
    min2 = list2[0]
    max1 = list1[0]
    max2 = list2[0]
    for i in list1:
        if i < min1:
            min1 = i
    for j in list2:
        if j < min2:
            min2 = j
    for k in list1:
        if k > max1:
            max1 = k
    for l in list2:
        if l > max2:
            max2 = l
    return min1 > min2 & max1 < max2

print(can_be_nested([1,2,3,4],[0,6]))


def concatenate_lists(list1, list2, target):
    newList = list1 + list2
    
    return newList == target


print(concatenate_lists([1,2],[3,4],[1,2,3,4]))
print(concatenate_lists([2,3],[5,4],[1,2,3,4]))
print(concatenate_lists([1,2,3],[4,5,6],[1,2,3,4,5,6]))

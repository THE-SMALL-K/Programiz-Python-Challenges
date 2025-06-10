def two_sum(nums, target):
    newList = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[i+j] == target:
                newList.append(i)
                newList.append(i+j)
                return newList

        
print(two_sum([11,2,15,7],9))
print(two_sum([2,7,11,15],9))
print(two_sum([2,11,7,15],9))
print(two_sum([2,7,11,15],13))

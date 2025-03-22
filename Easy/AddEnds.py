def add_ends(numbers):
    sum = numbers[0] + numbers[len(numbers)-1]
    return sum
print(add_ends([1,2,3,4,5]))
print(add_ends([3,4]))
print(add_ends([3,4,5]))
    
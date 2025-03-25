def sum_of_odds(numbers):
    sum = 0
    for i in  numbers:
        if i%2 == 1:
            sum+=i
    return sum

print(sum_of_odds([1,2,3,4,5]))
print(sum_of_odds([1,10,11,14,20,31]))
def count_digits(numbers, is_even):
    list_odd = []
    list_even = []
    for i in numbers:
        count = count_evens(str(i))
        list_even.append(count)
        count = count_odds(str(i))
        list_odd.append(count)
    
    if is_even == True:
        return list_even
    else:
        return list_odd

def count_evens(nums):
    even_count = 0 
    for i in range(len(nums)):
        if int(nums[i])%2 == 0:
            even_count+=1
    return even_count

def count_odds(nums):
    odd_count = 0 
    for i in range(len(nums)):
        if int(nums[i])%2 != 0:
            odd_count+=1
    return odd_count

print(count_digits([1234,5678],True))
print(count_digits([1234,5678],False))
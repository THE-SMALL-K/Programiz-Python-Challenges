def is_disarium_number(num):
    s = str(num)
    list = []
    for i in s:
        list.append(i)
    sum = 0
    index = 1
    for i in list:
        a = int(i)
        sum+=a**index
        index+=1
    return sum == num
        

print(is_disarium_number(175))
print(is_disarium_number(89))
print(is_disarium_number(81))
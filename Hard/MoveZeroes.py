def move_zeroes_to_end(n):
    s = str(n)
    newList = []
    count = 0
    for i in s:
        if int(i) != 0:
            newList.append(int(i))
        else:
            count+=1
    for i in range(count):
        newList.append(0)
    n = ""
    for i in newList:
        n+=str(i)
    return int(n)

print(move_zeroes_to_end(1020304050))
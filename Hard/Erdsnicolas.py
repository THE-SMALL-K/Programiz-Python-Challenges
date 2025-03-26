def generate_erdsnicolas(n):
    i = 10
    count = 0
    list = []
    while count <= n:
        sum = 0
        s = str(i)
        for j in range(len(s)):
            sum+=int(s[j])
        if (i%sum == 0):
            list.append(i)
            count+=1
        i+=1
    return list

print(generate_erdsnicolas(5))
print(generate_erdsnicolas(6))
print(generate_erdsnicolas(10))
     
        
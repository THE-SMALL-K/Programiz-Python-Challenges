def is_weird(n):
    if n%2 !=0:
        return "Weird"
    elif (n%2 == 0 and (n >= 6 and n <=20)):
        return "Weird"
    elif (n%2 == 0 and (n >=2 and n<=5)):
        return "Not weird" 
    elif (n%2 == 0 and n > 20):
        return "Not weird"

print(is_weird(3))
print(is_weird(4))
print(is_weird(8))
print(is_weird(22))

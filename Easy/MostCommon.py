def most_common_character(s):
    common = ''
    max_count = 0
    for i in s:
        c = s.count(i)
        if c > max_count:
            max_count = c
            common = i
    return common

print(most_common_character("hello world"))
print(most_common_character("python programming"))


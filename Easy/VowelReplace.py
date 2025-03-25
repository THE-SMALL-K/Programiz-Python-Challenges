def replace_vowels(string, char):
    s = list(string)
    news = ""
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'u' or s[i] == 'o':
            s[i] = char
    for j in range(len(s)):
        news+=s[j]
    return news

print(replace_vowels("hello world", 'x'))
print(replace_vowels("vowels", 'x'))





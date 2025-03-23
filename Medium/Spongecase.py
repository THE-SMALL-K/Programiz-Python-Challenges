def to_spongecase(text):
    index = 1
    s = ""
    for i in text:
        if index%2 == 0:
            s+=i.upper()
        else:
            s+=i.lower()
        index+=1
    print(s)

to_spongecase("Programiz")
to_spongecase("programizpro123")
to_spongecase("learn to code")

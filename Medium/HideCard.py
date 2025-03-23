
def mask_credit_card(card_number):
    s = str(card_number)
    t = s[0:len(s)-4]
    list = []
    a = ""
    for i in t:
        list.append(t)

    for i in range(len(list)):
        list[i] = "*"
    for i in list:
        a+=i
    return a+s[len(s)-4:len(s)]
print(mask_credit_card(4444444444444444))
print(mask_credit_card(341207588526144))
print(mask_credit_card(345394636789829))






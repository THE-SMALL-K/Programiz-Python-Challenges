from datetime import datetime
def date_difference(date1,date2):
    list1 = []
    list2 = []
    list1.append(date1[0:4])
    list1.append(date1[5:7])
    list1.append(date1[8:10])

    list2.append(date2[0:4])
    list2.append(date2[5:7])
    list2.append(date2[8:10])

    years = int(list1[0]) - int(list2[0])
    months = int(list1[1]) - int(list2[1])
    days = int(list1[2]) - int(list2[2])

    print(str(years) + " years, " + str(months) + " months, " + str(days) + " days")


date_difference("2022-12-31","2000-01-01")
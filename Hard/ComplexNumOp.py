''''
def complex_operations(num1, num2):
    list1 = []
    for i in range(len(num1)):
        list1.append(num1[i])
    list1.remove("+")
    
    real1 = int(list1[0])
    immaginiary1 = int(list1[1])

    list2 = []
    for i in range(len(num2)):
        list2.append(num2[i])
    list2.remove("+")

    real2 = int(list2[0])
    immaginiary2 = int(list2[1])

    Addition(real1,immaginiary1,real2,immaginiary2)
    Subtract(real1,immaginiary1,real2,immaginiary2)
    Multiply(real1,immaginiary1,real2,immaginiary2)
    Divide(real1,immaginiary1,real2,immaginiary2)
    

def Addition(real_num1, im_num1,real_num2, im_num2):
    sum_real = real_num1 + real_num2
    sum_im = im_num1 + im_num2
    print(sum_real)
    print(sum_im)

def Subtract(real_num1, im_num1,real_num2, im_num2):
    diff_real = real_num1 - real_num2
    diff_im = im_num1 - im_num2
    print(diff_real)
    print(diff_im)

def Multiply(real_num1, im_num1,real_num2, im_num2):
    multi_real = real_num1 - real_num2
    multi_im = im_num1 - im_num2
def Divide(real_num1, im_num1,real_num2, im_num2):
    divide_real = real_num1 - real_num2
    divide_im = im_num1 - im_num2    

print(complex_operations("2+3j", "1+2j"))
'''
def complex_operations(num1, num2):
    list1 = []
    for i in range(len(num1)):
        list1.append(num1[i])
    list1.remove("+")
    
    real1 = int(list1[0])
    imaginary1 = int(list1[1])

    list2 = []
    for i in range(len(num2)):
        list2.append(num2[i])
    list2.remove("+")

    real2 = int(list2[0])
    imaginary2 = int(list2[1])

    a = str(Addition_real(real1,real2))
    b = str(Addition_im(imaginary1,imaginary2))

    c = str(Subtract_real(real1,real2))
    d = str(Substract_im(imaginary1,imaginary2))

    #Multiply(real1,imaginary1,real2,imaginary2)
    #Divide(real1,imaginary1,real2,imaginary2)
    return "{Addition:" + "(" + a + "+" + b + "j), Subtraction:" + "(" + c + "+" + d + "j)}"

def Addition_real(real_num1, real_num2):
    sum_real = real_num1 + real_num2
    return sum_real

def Addition_im(im_num1,im_num2):
    sum_im = im_num1 + im_num2
    return sum_im

def Subtract_real(real_num1,real_num2):
    diff_real = real_num1 - real_num2
    return diff_real
def Substract_im(im_num1, im_num2):
    diff_im = im_num1 - im_num2
    return diff_im
'''
def Multiply_real(real_num1, im_num1,real_num2, im_num2):
    multi_real = real_num1 - real_num2

def Divide(real_num1, im_num1,real_num2, im_num2):
    divide_real = real_num1 - real_num2
    divide_im = im_num1 - im_num2    
'''
print(complex_operations("2+3j", "1+2j"))

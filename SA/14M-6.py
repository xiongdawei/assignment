import random

number_list = [0,1,2,3,4,5,6,7,8,9]
operator = ['+','-','*','/']

num1,num2 = random.sample(number_list,1)[0], random.sample(number_list,1)[0]
print(num1,num2)
operatoor = random.randint(1,4)
if operatoor==1:
    print( num1 + num2)
elif operatoor ==2:
    print(num1-num2)
elif operatoor==3:
    print(num1*num2)
elif operatoor==4:
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print ('divide by zero')
import math
a = int(input("a = ",end = " "),end = " ")
b = int(input("b = ",end = " "),end = " ")
c = a+b
if c>100:
    c = math.sqrt(c,end = " ")
    print(c,end = " ")
else:
    c = c**2
    print(c,end = " ")
print("Программа выполнена",end = " ")

a = int(input("a = ",end = " "),end = " ")
b = int(input("b = ",end = " "),end = " ")
c = int(input("c = ",end = " "),end = " ")
if a<b+c and b<a+c and c<a+b:
    print("Треугольник существует",end = " ")
else:
    print("Треугольник не существует",end = " ")
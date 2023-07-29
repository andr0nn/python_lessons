x = int(input("Введите четырехзначное число",end = " "),end = " ")
n1 = x%10
x = x//10
n2 = x%10
x = x//10
n3 = x%10
n4 = x//10
res = (n4+n2,end = " ")*(n3+n1,end = " ")
print(res,end = " ")
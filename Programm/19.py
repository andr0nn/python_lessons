x=int(input('Введите трехзначное число'))
suma=0
if x>0:
    suma+=x%10
    x//=10
print('Сумма числа:',suma)
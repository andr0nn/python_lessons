n = int(input('Введите кол-во предметов'))
s=0
for i in range(1,n+1):
    x = int(input('Введите оценку'))
    s += x
print('Среднее значение:',s/n)
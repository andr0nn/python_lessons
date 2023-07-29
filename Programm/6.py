from random import randint
begin=True
correct=0
incorrect=0
lvl = int(input('Выберете уровень сложности: \n 1:Легкий \n 2:Средний \n 3:Сложный \n 4:Своя настройка \nСделайте ваш выбор: '))
if lvl==1:
    n1=2
    n2=9
    quant=5
elif lvl==2:
    n1=11
    n2=99
    quant=10
elif lvl==3:
    n1=101
    n2=999
    quant=15
elif lvl==4:
    n1=int(input('Введите нижнюю границу случайного числа'))
    n2=int(input('Введите верхнюю границу случайного числа'))
    quant=int(input('Введите кол-во вопросов'))
else:
    print('Неправильный выбор')
    begin=False
if begin==True:

    for i in range(1,quant+1):
        r1=randint(n1,n2)
        r2=randint(n1,n2)
        print(str(i)+")",r1,"*",r2,"=",end=" ")
        x = int(input())
        if x==r1*r2:
            print('Correct!')
            correct+=1
        else:
            print('Incorrect')
            incorrect+=1
    print('Correct:',correct)
    print('Incorrect:',incorrect)
    res = 12/quant*correct
    if res>=0 and res<=3:
        print('Начальный уровень')
    elif res>3 and res<=6:
        print('Достаточный уровень')
    elif res>6 and res<=9:
        print('Средний уровень')
    elif res>9 and res<=12:
        print('Высокий уровень')
    else:
        print('Error')

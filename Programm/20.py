login="andrey"
password="1528"
tries=5
input_login=""
input_password=""
while login != input_login and password != input_password and tries>0:
    input_login=input('Введите логин: ')
    input_password=input('Введите пароль: ')
    if input_login != login or input_password != password:
        print('Неверный логин или пароль. Попробуйте еще раз')
        tries -= 1
        print (tries)
    else:
        print('Добро пожаловать,',login)
if tries<=0:
    print('Кол-во попыток исчерпано')


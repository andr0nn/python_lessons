for i in range(0,8):
    for j in range(0,8):
        if (i+j)%2==0:
            print('*',end=" ")
        else:
            print('#',end=" ")
    print()

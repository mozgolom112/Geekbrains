#Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))

if (a <= b):
    if (b <= c):
        print(f'{a} < {b} < {c}')
    else:
        if (c <= a):     
            print(f'{c} < {a} < {b}')
        else:
            print(f'{a} < {c} < {b}')
elif (a <= c): 
    print(f'{b} < {a} < {c}')
else:
    if (c <= b):
        print(f'{c} < {b} < {a}')
    else:
        print(f'{b} < {c} < {a}')

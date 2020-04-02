print('Введите два числа')
try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
except:
    print('не верно введены числа')
if b != 0:
    c = a / b
    print('Частное равное {}'.format(c))
else: 
    print('Делить на ноль нельзя. Решений нет')
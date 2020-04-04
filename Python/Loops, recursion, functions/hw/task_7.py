# Задание 7. 
# Написать программу, доказывающую или проверяющую, 
# что для множества натуральных чисел выполняется 
# равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

def sum_of_natural(n : int):
    if n <=0:
        return 'Введите натуральное число'
    
    hypothesis = ( n * (n+1) ) /2
    count = 0
    i = 0

    while i < n or count > hypothesis:
        i += 1 
        count += i 
    if hypothesis == count:
        print(f'А вы на что надеялись)')
    else:
        print('На всякий не математический случай и кривой код')

sum_of_natural(5)
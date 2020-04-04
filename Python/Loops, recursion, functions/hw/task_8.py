# Задача 8. 
# Посчитать, сколько раз встречается определенная цифра 
# в введенной последовательности чисел. Количество вводимых 
# чисел и цифра, которую необходимо посчитать, задаются 
# вводом с клавиатуры.

def count_number(desired_number, *arg):
    if desired_number < 0 or desired_number > 10:
        print('Введите цифру, а не число')
        return 0
    
    if len(arg) == 0:
        print('Введите числа, в которых искать')
        return 0

    count = 0

    for num in arg:
        if num < 0:
            num *= -1 

        while num != 0:
            if num % 10 == desired_number:
                count += 1
            num //= 10
    return count

print(count_number(1))
#Задача 9. Среди натуральных чисел, которые были 
# введены, найти наибольшее по сумме цифр. 
# Вывести на экран это число и сумму его цифр.

def max_sum_num(*arg):
    if len(arg) == 0:
        print('Введите числа')
        return 0
    max_num = 0
    max_sum = 0

    current_sum = 0
    current_num = 0
    
    for num in arg:
        current_num = num
        current_sum = 0

        if num < 0: 
            num *= -1

        while num != 0:
            current_sum += num % 10
            num //= 10
        
        if (max_sum <= current_sum):
            max_sum = current_sum
            max_num = current_num

    print(f'Число с максимальной суммой цифр: {max_num} с суммой {max_sum}')



max_sum_num(5664, 3, 11111, 45674994, 9999, 0)
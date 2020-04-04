#Задание 4. 
#Найти сумму n элементов следующего 
# ряда чисел: 1, -0.5, 0.25, -0.125,… 
# Количество элементов (n) вводится с клавиатуры.

def sum_row(n : int):
    total = 1
    prev = 1
    if n <= 0:
        return 0

    while n > 1:
        prev *= (-0.5)
        total += prev
        n -= 1
    
    return total

print(sum_row(4))
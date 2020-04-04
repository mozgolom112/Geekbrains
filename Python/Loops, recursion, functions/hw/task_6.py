#Задача 6. 
# В программе генерируется случайное целое число от 0 до 100.
#  Пользователь должен его отгадать не более чем за 10 попыток.
#  После каждой неудачной попытки должно сообщаться, больше или
#  меньше введенное пользователем число, чем то, что загадано. 
# Если за 10 попыток число не отгадано, вывести ответ.

from random import randint

def guess_the_number():
    print('Число загадано от 0 до 100')
    prog_number = randint(0, 100)    
    attempts = 1
    
    while attempts != 11:
        user_number = int(input(f'Введите {attempts} число: '))
        if user_number == prog_number:
            break
        elif user_number < prog_number:
            print(f'Число {user_number} < загаднного')
        else:
            print(f'Число {user_number} > загаднного')
        attempts +=1
    
    if attempts < 11:
        print(f'Молодчик! Вы отгадали наше число за {attempts} попыток')
    else:
        print(f'Вы не отгадали число за 10 попыток. Загаданное число: {prog_number}\n' +
        'Почитайте, что такое бинарный поиск')

guess_the_number()
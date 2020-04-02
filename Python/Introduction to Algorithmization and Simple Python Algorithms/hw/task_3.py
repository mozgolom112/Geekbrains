# Задание 3
#Написать программу, которая генерирует в указанных пользователем границах:
#a. случайное целое число,
#b. случайное вещественное число,
#c. случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random #используем для рандома чисел. 


mode = input('a. случайное целое число,\n' +
            'b. случайное вещественное число,\n' +
            'c. случайный символ.\n' +
            'Введите режим работы: ')
print('\n')

if (mode == 'a' or mode == 1):
    print('Mode - a\n')
    print('Вводите только целые числа')
    try:
        left = int(input('Введите левую границу: '))
        right = int(input('Введите правую границу: '))
    except:
        pass

    if (left > right): #если пользователь не верно ввел значения
        temp = right
        right = left
        left = temp

    value = random.randint(left, right)
    print(f'Cлучайное целое число в диапазоне [{left},{right}]: {value}')

elif (mode == 'b' or mode == 2):
    print('Mode - b\n')
    print('Вводите вещественные числа\n')
    try:
        left = float(input('Введите левую границу: '))
        right = float(input('Введите правую границу: '))
    except:
        pass
    # проверка, что границы заданы правильно, не требуется, так как реализована поддержка внутри функции
    value = random.uniform(left, right) 
    print(f'Cлучайное целое число в диапазоне [{left},{right}]: {value}')
elif (mode == 'c' or mode == 3):
    print('Mode - c')
    print('Работает только для латинского алфавита нижнего регистра.\n' +
        'Выдает случайный символ, между двумя введенными пользователям.\n' +
        'Введите два символа\n')
    try:
        fst_char = str(input('Введите первый символ: ')).lower() # только получаем. Далее всю программу храним код и Unocode
        scd_char = str(input('Введите второй символ: ')).lower()
        
        #Проверка, одиночные ли символы
        if not (len(fst_char) == 1 and len(scd_char) == 1):
            print('Нужно ввести символы, а не строки')
    except:
        pass
    
    #далее использованы встроенные функции 
    # ord(str) - возвращает номер в unicode
    # chr(int) - возвращает символ по номеру из unicode
    # читай документацию
    
    # перевод сразу из символа в int
    try:
        fst_char = ord(fst_char)
        scd_char = ord(scd_char)
    except:
        pass

    #Проверка, являются ли символами из алфавита:
    if ( ( fst_char < ord('a') or fst_char > ord('z') ) or (scd_char < ord('a') or scd_char > ord('z') ) ):
        print('Введите символы только из латинского алфавита')
    else:
        if (fst_char < scd_char):
            value = random.randint(fst_char, scd_char)
        else:
            value = random.randint(scd_char, fst_char)
        print(f'Ваша случайная буква между \'{chr(fst_char)}\' и \'{chr(scd_char)}\' : \'{chr(value)}\'')  
else:
    print(f'Режима работы программы {mode} нет')
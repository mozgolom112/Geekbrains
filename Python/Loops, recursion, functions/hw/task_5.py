#Задание 5. Вывести на экран коды и символы таблицы ASCII, 
# начиная с символа под номером 32 и заканчивая 127-м включительно. 
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.


def print_ascii(start, end):
    if start < 0 or end < 0:
        return 'Код должен быть положительным числом'
    if start > end:
        temp = end
        end = start
        start = temp
   
    s = ''
    column = 10 # количество колонок
    delta = start % column

    for code in range(start, end + 1):
        if (code - delta) % column == 0:
            print(s)
            s = '\n'
        s = f'{s} {code} - {chr(code)}'
    print(s) #вывод того, что осталось

print_ascii(32, 127)
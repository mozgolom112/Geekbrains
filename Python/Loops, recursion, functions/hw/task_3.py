#Задание 3.
#Сформировать из введенного числа обратное по порядку 
#входящих в него цифр и вывести на экран. 
#Например, если введено число 3486, надо вывести 6843.

def inv_num(number):
    s = ''
    isnegative = False
    
    try:
        number = int(number)
    except:
        pass

    if number < 0:
        isnegative = True
        number *= -1
    
    if number != 0:
        while number != 0:
            s = f'{s}{number % 10}'
            number //= 10
        if isnegative:
            s = f'-{s}'
    else:
        s = '0'
    return s

print(inv_num(654))
print(inv_num(0))
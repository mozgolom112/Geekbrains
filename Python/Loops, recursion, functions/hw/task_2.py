#Задание 2. 
# Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, 
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

#преобразует число в строку, берем по символу и обратно переводим в int
def count_odd_even_str(number) -> dict: # вопрос, нужно ли использовать аннотацию к функции? 
    # https://qarchive.ru/38458_chto_oznachaet___oznachaet_v_opredelenijah_funktsii__python_
    count = {
        'odd' : 0,
        'even' : 0}
    #numbers = [int(c) for c in str(number).replace(' ','').replace('-','')]
    for num in str(number).replace(' ', '').replace('-',''):
        if int(num) % 2 == 0:
            count['even'] += 1
        else:
            count['odd'] += 1 
    return count

#математически откидываем цифры
def count_odd_even_math(number):
    count = {
        'odd' : 0,
        'even' : 0}
    try:
        number = int(number)
    except:
        return count
    
    if number < 0:
        number *= -1
        #так как -5 // 10 = -1
    
    if number != 0: #так как могут ввести 0
        while number != 0:
            if (number % 10) % 2 == 0:
                count['even'] += 1
            else:
                count['odd'] += 1 
            number //= 10
    else:
        count['even'] += 1
    return count


print(count_odd_even_str(000))
print(count_odd_even_math(000))

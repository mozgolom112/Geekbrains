def func(a, b) -> str:
    if (a==b):
        return f'{a}'
    elif (a > b): #по возрастанию
        return f'{a}, {func(a-1, b)}'
    elif (a < b): #по убыванию
        return f'{a}, {func(a+1, b)}' #f строки
print(func(8, 10000)) #глубина рекурсии 1000


x = float(input('Введите число x: '))
if (x == 0):
    result = 0
elif (x > 0):
    result = 2 * x - 10
else:
    result = 2 * abs(x) - 1
print(f'Результат: {result}')